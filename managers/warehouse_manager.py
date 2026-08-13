from repositories.products import Products
from repositories.warehouse import almacenes


class WarehouseManager:
    def __init__(self):
        self.lista_warehouses = []
        self.lista_productos = {}

    def crear_almacen(self):
        symbol = input("Ingresa el identificador del almacen: ")
        name = input("Ingresa el nombre del almacen: ")
        quantity = int(input("Ingresa la capacidad del almacen: "))

        nuevo_almacen = almacenes(symbol, name, quantity)
        self.lista_warehouses.append(nuevo_almacen)
        print("Almacen creado")

    def ver_almacenes(self):
        if not self.lista_warehouses:
            print("No hay almacenes. Crea uno")
            return

        for index, almacen in enumerate(self.lista_warehouses):
            print(f"{index + 1}. {almacen}")

    def editar_almacenes(self):
        if not self.lista_warehouses:
            print("No hay almacenes para editar")
            return

        self.ver_almacenes()
        try:
            seleccion = int(input("Selecciona el numero del almacen para editar: ")) - 1
            if 0 <= seleccion < len(self.lista_warehouses):
                almacen = self.lista_warehouses[seleccion]
                print("Deja en blank si no quieres modificar nada")

                nuevo_symbol = input(
                    f"Nuevo identificador ({getattr(almacen, 'symbol', '')}): "
                )
                nuevo_name = input(f"Nuevo nombre ({getattr(almacen, 'name', '')}): ")
                nuevo_quantity = input(
                    f"Nueva capacidad ({getattr(almacen, 'quantity', '')}): "
                )

                if nuevo_symbol.strip():
                    almacen.symbol = nuevo_symbol
                if nuevo_name.strip():
                    almacen.name = nuevo_name
                if nuevo_quantity.strip():
                    almacen.quantity = nuevo_quantity

                print("Almacen actualizado correctamente.")
            else:
                print("Selección inválida")
        except ValueError:
            print("Entrada no válida. Introduce un número")

    def eliminar_almacenes(self):
        if not self.lista_warehouses:
            print("No hay almacenes para eliminar")
            return

        self.ver_almacenes()
        try:
            seleccion = int(input("Selecciona el numero del almacen a eliminar: ")) - 1
            if 0 <= seleccion < len(self.lista_warehouses):
                almacen_a_eliminar = self.lista_warehouses.pop(seleccion)

                if almacen_a_eliminar in self.lista_productos:
                    del self.lista_productos[almacen_a_eliminar]

                print(
                    f"Almacen '{almacen_a_eliminar}' y sus productos asociados fueron eliminados."
                )
            else:
                print("Selección inválida")
        except ValueError:
            print("Entrada inválida. Introduce un número")

    def insertar_productos(self):
        if not self.lista_warehouses:
            print("Asigna un almacen")
            return

        id = int(input("Ingresa el ID del producto: "))
        name = input("Ingresa el nombre del producto: ")
        categories = input("Ingresa la categoria del producto: ")
        sku = input("Ingresa el sku del producto: ")

        nuevo_producto = Products(id, name, categories, sku)

        for index, almacen in enumerate(self.lista_warehouses):
            print(f"{index + 1}, {almacen}")

        try:
            seleccion_almacen = int(input("Selecciona un almacen: ")) - 1

            if not (0 <= seleccion_almacen < len(self.lista_warehouses)):
                print("Selección inválida")
                return

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
        except ValueError:
            print("Entrada invalida. Introduce un numero")

    def ver_productos(self):
        if not self.lista_productos:
            print("No hay productos. Crea uno")
            return

        for index, product in enumerate(self.lista_productos):
            print(f"{index + 1}. {product}")
