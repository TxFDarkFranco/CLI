from .warehouse_manager import WarehouseManager
from .suppliers_manager import SuppliersManager
import json

productm = WarehouseManager()
supplierm = SuppliersManager()


def guardar_datos(productm=None, supplierm=None):
    if productm is None:
        productm = globals().get("productm")
    if supplierm is None:
        supplierm = globals().get("supplierm")

    datos = {"warehouse": [], "products": [], "suppliers": []}

    try:
        w_count = len(getattr(productm, "lista_warehouses", []))
        p_keys = len(getattr(productm, "lista_productos", {}))
        s_count = len(getattr(supplierm, "lista_suppliersmanager", []))
        print(f"DEBUG guardar_datos: warehouses={w_count}, products_keys={p_keys}, suppliers={s_count}")
    except Exception:
        print("DEBUG guardar_datos: error leyendo estructuras")

    # Guardar almacenes
    for almacen in getattr(productm, "lista_warehouses", []):
        datos["warehouse"].append(
            {
                "symbol": getattr(almacen, "symbol", None),
                "name": getattr(almacen, "name", None),
                "quantity": getattr(almacen, "quantity", None),
            }
        )

    # Guardar productos (asociados a almacenes)
    for warehouse_key, productos in getattr(productm, "lista_productos", {}).items():
        if isinstance(warehouse_key, str):
            warehouse_symbol = warehouse_key
            warehouse_name = warehouse_key
        else:
            warehouse_symbol = getattr(warehouse_key, "symbol", None)
            warehouse_name = getattr(warehouse_key, "name", None)

        for producto in productos:
            datos["products"].append(
                {
                    "warehouse": warehouse_symbol,
                    "warehouse_name": warehouse_name,
                    "id": getattr(producto, "id", None),
                    "name": getattr(producto, "name", None),
                    "categories": getattr(producto, "categories", None),
                    "sku": getattr(producto, "sku", None),
                }
            )

    # Guardar suppliers
    for supplier in getattr(supplierm, "lista_suppliersmanager", []):
        email = getattr(supplier, "gmail", None) or getattr(supplier, "email", None)
        datos["suppliers"].append(
            {
                "id": getattr(supplier, "id", None),
                "name": getattr(supplier, "name", None),
                "contact": getattr(supplier, "contact", None),
                "email": email,
                "product": getattr(supplier, "product", None),
                "price": getattr(supplier, "price", None),
            }
        )

    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print("Datos guardados en datos.json")
