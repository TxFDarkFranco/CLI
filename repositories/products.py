class Products:
    def __init__(self, id: int, name: str, categories: str, sku: str):
        self.id = id
        self.name = name
        self.categories = categories
        self.sku = sku

    def __str__(self):
        return f"{self.id}, {self.name}, {self.categories}, {self.sku}"
