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

        @property
        def name(self):
            return "XXX" + self._name[-3:]
        
        @name.setter
        def name(self, new_name):
            self._name = new_name
        
        @name.deleter
        def name(self):
            del self._name
            print("Name deleted")
            
    def __str__(self):
        return f"{self.id}, {self.name}, {self.contact}, {self.gmail}, {self.product}, {self.price}"
