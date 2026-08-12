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

        id = input("Ingresa el un ID del producto: ")
        name = input("Ingresa el nombre del producto: ")
        categories = input("Ingresa la categoria del producto: ")
        sku = input("Ingresa el sku del producto: ")

        nuevo_producto = Products(id, name, categories, sku)

        for index, almacen in enumerate(self.lista_warehouses):
            print(f"{index + 1}, {almacen}")

        seleccion_almacen = int(input("Ingresa tu eleccion")) - 1

        almacen_seleccionado = self.lista_warehouses[seleccion_almacen]

        if almacen_seleccionado not in self.lista_productos:
            self.lista_productos[almacen_seleccionado] = []

        existe = any(
            p.id == nuevo_producto.id
            for p in self.lista_productos[almacen_seleccionado]
        )

        if existe:
            print("El producto ya esta registrado en este almacen")
        else:
            self.lista_productos[almacen_seleccionado].append(nuevo_producto)
            print(f"Producto insertado con éxito en: {almacen_seleccionado}")

    def ver_productos(self):
        if not self.lista_productos:
            print("No hay productos. Crea uno")
            return

        for index, product in enumerate(self.lista_productos):
            print(f"{index + 1}. {product}")
