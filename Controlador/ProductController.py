# Controller/ProductoController.py
from  Model.DAOProduct import ProductoDAO

class ProductoController:
    def __init__(self):
        self.producto_dao = ProductoDAO()

    def obtener_productos_con_existencias(self):
        return self.producto_dao.select_all()

    def actualizar_existencias(self, id_producto, cantidad):
        self.producto_dao.update_existencias(id_producto, cantidad)