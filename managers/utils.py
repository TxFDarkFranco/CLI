from warehouse_manager import WarehouseManager
from suppliers_manager import SuppliersManager
import json

productm = WarehouseManager()
supplierm = SuppliersManager()


def guardar_datos():
    datos = {"warehouse": [], "products": [], "suppliers": []}

    for warehouses in productm.lista_warehouse:
        datos["warehouse"].append(
            {
                "symbol": warehouses.symbol,
                "name": warehouses.name,
                "quantity": warehouses.quantity,
            }
        )

    for warehouse, products in productm.lista_productos.items:
        for producto in products:
            datos["products"].append(
                {
                    "warehouse": warehouse.name,
                    "id": producto.id,
                    "name": producto.name,
                    "categories": producto.categories,
                    "sku": producto.sku,
                }
            )

    for supplier in supplierm.lista_suppliersmanager:
        datos["suppliers"].append(
            {
                "id": supplier.id,
                "name": supplier.name,
                "contact": supplier.contact,
                "gmail": supplier.gmail,
                "product": supplier.product,
                "price": supplier.price,
            }
        )

    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
