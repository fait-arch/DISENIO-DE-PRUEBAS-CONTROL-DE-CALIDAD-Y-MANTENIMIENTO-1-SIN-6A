import random
from collections import defaultdict

class AnalizadorDefectos:
    def __init__(self):
        self.defectos_por_modulo = defaultdict(list)

    def registrar_defecto(self, modulo, severidad):
        self.defectos_por_modulo[modulo].append(severidad)

    def generar_reporte(self):
        print("=" * 50)
        print("📊 REPORTE DE DEFECTOS POR MÓDULO")
        print("=" * 50)
        for modulo, defectos in self.defectos_por_modulo.items():
            total = len(defectos)
            criticos = defectos.count("Crítico")
            print(f"\n🔹 {modulo}:")
            print(f"   Total: {total} defectos")
            print(f"   Críticos: {criticos} ({criticos/total*100:.1f}%)")
            # Principio de Pareto: 80% de problemas en 20% del código
            if criticos / total > 0.3:
                print(f"   ⚠️  MÓDULO DE ALTO RIESGO")

# Simulación de un proyecto
analizador = AnalizadorDefectos()

# Simular 50 defectos en diferentes módulos
modulos = ["Autenticación", "Pagos", "Reportes", "UI", "Base de Datos"]
severidades = ["Crítico", "Mayor", "Menor"]

for _ in range(50):
    modulo = random.choice(modulos)
    # Los módulos críticos (Autenticación, Pagos) tienen más defectos críticos
    if modulo in ["Autenticación", "Pagos"]:
        severidad = random.choices(severidades, weights=[0.5, 0.3, 0.2])[0]
    else:
        severidad = random.choices(severidades, weights=[0.1, 0.3, 0.6])[0]
    
    analizador.registrar_defecto(modulo, severidad)

analizador.generar_reporte()
