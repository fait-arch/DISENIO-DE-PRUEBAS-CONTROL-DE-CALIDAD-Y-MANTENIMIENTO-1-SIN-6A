# Ahora se clasificaban los defectos
class Defecto:
    def __init__(self, tipo, severidad, componente):
        self.tipo = tipo  # "Lógico", "Sintaxis", "Integración"
        self.severidad = severidad  # "Crítico", "Mayor", "Menor"
        self.componente = componente

    def __repr__(self):
        return f"🐛 {self.tipo} [{self.severidad}] en {self.componente}"


# Ejemplo: Clasificación matemática de defectos
defectos = [
    Defecto("Lógico", "Crítico", "módulo_pago"),
    Defecto("Integración", "Mayor", "API_externa"),
    Defecto("UI", "Menor", "formulario_login")
]

# Distribución de defectos por severidad
from collections import Counter
distribucion = Counter([d.severidad for d in defectos])
print("📊 Distribución de defectos:", dict(distribucion))