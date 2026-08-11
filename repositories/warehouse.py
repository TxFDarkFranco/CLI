class Almacenes:
    def __init__(self, symbol, name: str, quantity: int):
        self.symbol = symbol
        self.name = name
        self.quantity = quantity

    def _str_(self):
        return f"{self.symbol}, {self.name}, {self.quantity}"