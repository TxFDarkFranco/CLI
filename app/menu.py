from managers.warehouse_manager import WarehouseManager
from managers.suppliers_manager import SuppliersManager
from managers.utils import guardar_datos

productm = WarehouseManager()
supplierstm = SuppliersManager()


def menu():
    print("=" * 25)
    print("Warehouse & Logistics Management System")
    print("=" * 25)
    print("1.Insertar productos")
    print("2.Ver productos")
    print("3.Crear alamacen")
    print("4.Ver alamcenes")
    print("5.Crear Suplidores")
    print("6.Ver Suplidores")
    print("7.Guardar datos")

    while True:
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                productm.insertar_productos()
                continue

            case "2":
                productm.ver_productos()
                continue

            case "3":
                productm.crear_almacen()
                continue

            case "4":
                productm.ver_almacenes()
                continue

            case "5":
                supplierstm.crear_suppliers()

            case "6":
                supplierstm.ver_suppliers()

            case "7":
                guardar_datos()
