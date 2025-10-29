'''
Ejemplo didáctico 
---------------------------------------------------
Tema:   "PyModel 1.0" (pequeña mini-impl. para aprender model-based testing)
Por:    fait-arch y ChatGPT GPT-5 mini

'''

from dataclasses import dataclass
from typing import Callable, Dict, List, Any, Tuple
import copy


# Acción: tiene nombre, guard (puede ejecutarse?) y efecto (modifica estado)
@dataclass
class Action:
    name: str
    guard: Callable[[Dict[str, Any]], bool]
    effect: Callable[[Dict[str, Any]], None]

# PyModel: mantiene estado inicial y lista de acciones; genera y ejecuta trazas
class PyModel:
    def __init__(self, start_state: Dict[str, Any], actions: List[Action]):
        self.start_state = start_state
        self.actions = actions

    def enabled_actions(self, state: Dict[str, Any]) -> List[Action]:
        return [a for a in self.actions if a.guard(state)]

    def generate_traces(self, max_depth: int = 4) -> List[List[str]]:
        traces: List[List[str]] = []

        def dfs(state: Dict[str, Any], path: List[str], depth: int):
            if depth == max_depth:
                traces.append(path.copy())
                return
            enabled = self.enabled_actions(state)
            if not enabled:
                traces.append(path.copy())
                return
            for a in enabled:
                stcopy = copy.deepcopy(state)
                # aplicar efecto (mutar stcopy)
                a.effect(stcopy)
                path.append(a.name)
                dfs(stcopy, path, depth + 1)
                path.pop()

        dfs(copy.deepcopy(self.start_state), [], 0)
        return traces

    def run_trace(self, trace: List[str]) -> Tuple[bool, Dict[str, Any]]:
        state = copy.deepcopy(self.start_state)
        name_to_action = {a.name: a for a in self.actions}
        try:
            for step in trace:
                a = name_to_action.get(step)
                if a is None:
                    raise RuntimeError(f"Acción desconocida: {step}")
                if not a.guard(state):
                    raise RuntimeError(f"Guard falló para {step} con estado {state}")
                a.effect(state)
            return True, state
        except Exception as e:
            return False, {"error": str(e), "state": state}

# Ejemplo concreto: una cola limitada (capacidad 2) 
MAX_CAPACITY = 2

def guard_enqueue(state):
    return len(state['q']) < MAX_CAPACITY

def effect_enqueue(state):
    # en ejemplo agregamos el siguiente número incremental
    next_val = (state.get('next', 1))
    state['q'].append(next_val)
    state['next'] = next_val + 1

def guard_dequeue(state):
    return len(state['q']) > 0

def effect_dequeue(state):
    state['q'].pop(0)

def guard_reset(state):
    return True

def effect_reset(state):
    state['q'].clear()
    state['next'] = 1

actions = [
    Action("enqueue", guard_enqueue, effect_enqueue),
    Action("dequeue", guard_dequeue, effect_dequeue),
    Action("reset", guard_reset, effect_reset),
]

start = {'q': [], 'next': 1}
model = PyModel(start, actions)

if __name__ == "__main__":
    print("Estado inicial:", start)
    traces = model.generate_traces(max_depth=4)
    print(f"\nTrazas generadas (máx profundidad 4): {len(traces)}")
    for i, t in enumerate(traces[:20], 1):  # mostramos hasta 20 trazas
        ok, final = model.run_trace(t)
        print(f"{i:02d}. {t} -> ok={ok}, final={final}")
    if len(traces) > 20:
        print(f"... (hay {len(traces)-20} trazas más)")