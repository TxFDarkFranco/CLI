class almacenes:
    def __init__(self, symbol: str, name: str, quantity: int, product: str):
        self.symbol = symbol
        self.name = name
        self.quantity = quantity
        self.product = product

    def __str__(self):
        return f"{self.symbol}, {self.name}, {self.quantity}, {self.product}"