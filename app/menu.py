from managers.products_manager import ProductManager


productm = ProductManager()



def menu():
    while True:
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                productm.insertar_productos()
                continue

            case "2":
                productm.ver_productos()
                continue

