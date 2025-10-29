'''
Modelo PyModel para una máquina expendedora simple.
Echo: fait-arch y ChatGPT 5 mini
'''

from vendingmachine import *

# Estados iniciales
def setup():
    global balance
    balance = 0

# Transiciones y propiedades
def property_balance_nonnegative():
    """El saldo nunca debe ser negativo."""
    assert balance >= 0

# Modelo de PyModel
class Model:
    """Implementación mínima de Model para pruebas locales."""
    def __init__(self, actions=None, properties=None, setup=None):
        self.actions = actions or []
        self.properties = properties or []
        self.setup = setup

    def run_setup(self):
        if callable(self.setup):
            self.setup()

    def __repr__(self):
        return f"Model(actions={len(self.actions)}, properties={len(self.properties)})"

VendingMachineModel = Model(
    actions=[insert_coin, select_item, refund],
    properties=[property_balance_nonnegative],
    setup=setup
)
