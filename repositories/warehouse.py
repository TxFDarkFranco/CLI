class Almacenes:
    def init(self, symbol, name: str, quantity: int):
        self.symbol = symbol
        self.name = name
        self.quantity = quantity

    def str(self):
        return f"{self.symbol}, {self.name}, {self.quantity}"
