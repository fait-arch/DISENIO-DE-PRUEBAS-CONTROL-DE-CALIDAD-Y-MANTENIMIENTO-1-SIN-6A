# vendingmachine.py
# Modelo de máquina expendedora para PyModel

balance = 0

def insert_coin(value):
    """Insertar una moneda (por ejemplo, 25, 50, 100 centavos)."""
    global balance
    balance += value

def select_item(price):
    """Seleccionar un producto y pagar su precio."""
    global balance
    assert balance >= price, "Saldo insuficiente"
    balance -= price

def refund():
    """Devolver el saldo restante."""
    global balance
    r = balance
    balance = 0
    return r

# Las acciones posibles del modelo
actions = (insert_coin, select_item, refund)
