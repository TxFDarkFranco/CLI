from managers.products_manager import ProductManager


productm = ProductManager()


opcion = input("Elige una opcion: ")


def menu():
    while True:
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                return productm.insertar_productos()
