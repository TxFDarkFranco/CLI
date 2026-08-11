from repositories.products import Products

class WarehouseManager:
    def __init__(self):
        self.lista_warehouses = []
        self.lista_productos = {}


    def insertar_productos(self):
            if not self.lista_warehouses:
                print("Asigna un almacen")
                return
    
            id = input("Ingresa el un ID del producto: ")
            name = input("Ingresa el nombre del producto: ")
            categories = input("Ingresa la categoria del producto: ")
            sku = input("Ingresa el sku del producto: ")
    
            nuevo_producto = Products(id, name, categories, sku)
    
            self.lista_productos.append(nuevo_producto)
            print("Producto insertado")
    
    def ver_productos(self):
        if not self.lista_productos:
            print("No hay productos. Crea uno")
            return
            
        for index, product in enumerate(self.lista_productos):
            print(f"{index + 1}, {product}")

