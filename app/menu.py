from managers.suppliers_manager import SuppliersManager
from managers.warehouse_manager import WarehouseManager
from managers.utils import guardar_datos


def menu():
    productm = WarehouseManager()
    supplierstm = SuppliersManager()

    while True:
        print("\n" + "=" * 25)
        print("Warehouse & Logistics Management System")
        print("=" * 25)
        print("1. Insertar productos")
        print("2. Ver productos")
        print("3. Crear almacen")
        print("4. Ver almacenes")
        print("5. Crear suplidores")
        print("6. Ver suplidores")
        print("7. Editar almacenes")
        print("8. Eliminar almacenes")
        print("9. Salir")
        print("10. Guardar datos")

        opcion = input("\nElige una opcion: ")

        match opcion:
            case "1":
                productm.insertar_productos()
            case "2":
                productm.ver_productos()
            case "3":
                productm.crear_almacen()
            case "4":
                productm.ver_almacenes()
            case "5":
                supplierstm.crear_suppliers()
            case "6":
                supplierstm.ver_suppliers()
            case "7":
                productm.editar_almacenes()
            case "8":
                productm.eliminar_almacenes()
            case "9":
                print("Programa finalizado")
                break
            case "10":
                guardar_datos(productm, supplierstm)


