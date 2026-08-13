class Suppliers:
    def __init__(
        self, id: int, name: str, contact: int, email: str, product: str, price: int
    ):
        self.id = id
        self.name = name
        self.contact = contact
        self.gmail = email
        self.product = product
        self.price = price

    def __str__(self):
        return f"{self.id}, {self.supplier}, {self.contact}, {self.gmail}, {self.product}, {self.price}"
