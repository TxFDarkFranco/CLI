from repositories.products import Products


class ProductManager:
    def __init__(self):
        self.lista_productos = []

    def insertar_productos(self):
        id = input("Ingresa el un ID del producto: ")
        name = input("Ingresa el nombre del producto: ")
        categories = input("Ingresa la categoria del producto: ")
        sku = input("Ingresa el sku del producto")

        nuevo_producto = Products(id, name, categories, sku)

        self.lista_productos.append(nuevo_producto)
        print("Producto insertado")
