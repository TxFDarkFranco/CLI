from managers.warehouse_manager import WarehouseManager

productm = WarehouseManager()


def menu():
    print("=" * 25)
    print("Warehouse & Logistics Management System")
    print("=" * 25)
    print("1.Insertar productos")
    print("2.Ver productos")
    print("3.Crear alamacen")
    print("4.Ver alamcenes")

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
