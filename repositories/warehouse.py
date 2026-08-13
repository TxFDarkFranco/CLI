class Almacenes:
    def __init__(self, symbol: str, name: str, quantity: int):
        self.symbol = symbol
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.symbol}, {self.name}, {self.quantity}"
