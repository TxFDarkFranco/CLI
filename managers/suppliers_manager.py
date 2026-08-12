from repositories.suppliers import Suppliers

class SuppliersManager:
    def __init__(self):
        self.lista_suppliersmanager = []

    def crear_suppliers(self):
        id = input ("Ingresa el identificador de el Suplidor:")
        name = input ("Ingresa el Nombre del Suplidor:")
        contact = input ("Ingresa el numero de contacto del Suplidor:")
        gmail = input ("Ingresa el Correo electronico del Suplidor:")
        product = input ("Ingresa el Producto:")
        Price = input ("Ingresa el precio de compra:")

        nuevo_suplidor = Suppliers(id, name, contact, gmail, product, Price)
        self.lista_suppliersmanager.append(nuevo_suplidor)
        print ("Nuevo Suplidor Creado")


    def ver_suppliers(self):
        if not self.lista_suppliersmanager:
            print ("No hay suplidores. Crea uno")
            return
        
        for index, suplidor in enumerate(self.lista_suppliersmanager):
                    print(f"{index + 1}. {suplidor}")