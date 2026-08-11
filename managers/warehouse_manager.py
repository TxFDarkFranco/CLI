from repositories.products import Products
from repositories.warehouse import almacenes


class WarehouseManager:
    def __init__(self):
        self.lista_warehouses = []
        self.lista_productos = {}

    def crear_almacen(self):
        symbol = input("Ingresa el identificador del almacen: ")
        name = input("Ingresa el nombre del almacen: ")
        quantity = input("Ingresa la capacidad del almacen: ")

        nuevo_almacen = almacenes(symbol, name, quantity)
        self.lista_warehouses.append(nuevo_almacen)
        print("Almacen creado")

    def ver_almacenes(self):
        if not self.lista_warehouses:
            print("No hay almacenes. Crea uno")
            return

        for index, almacen in enumerate(self.lista_warehouses):
            print(f"{index + 1}. {almacen}")

    def insertar_productos(self):
        if not self.lista_warehouses:
            print("Asigna un almacen")
            return

        almacen = input()
        id = input("Ingresa el un ID del producto: ")
        name = input("Ingresa el nombre del producto: ")
        categories = input("Ingresa la categoria del producto: ")
        sku = input("Ingresa el sku del producto: ")

        nuevo_producto = Products(almacen, id, name, categories, sku)

        for index, almacen in enumerate(self.lista_warehouses):
            print(f"{index + 1}, {almacen}")

        seleccion_almacen = int(input("Ingresa tu eleccion")) - 1

        almacen_seleccionado = self.lista_warehouses[seleccion_almacen]
        if almacen_seleccionado not in self.lista_warehouses:
            print("No es valido")
            return

        if nuevo_producto in self.lista_productos:
            print("El producto ya esta registrado")
        else:
            self.lista_productos.append(nuevo_producto)


        

        



        # self.lista_productos.append(nuevo_producto)
        print("Producto insertado en almacen")



    def ver_productos(self):
        if not self.lista_productos:
            print("No hay productos. Crea uno")
            return

        for index, product in enumerate(self.lista_productos):
            print(f"{index + 1}. {product}")

