# Desarrollador en 1982
def dividir(a, b):
    return a / b  # ¿Qué podría salir mal? 🤷

# Spoiler: TODO podía salir mal
def defecto_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida."

print(defecto_division(10, 0))  # 💥 ZeroDivisionError
