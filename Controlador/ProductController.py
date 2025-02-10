from  Model.DAOProduct import ProductoDAO

#AÑADIMOS CONTROLES A LAS OPERACIONES DE PRODUCTOS
class ProductoController:
    def __init__(self):
        self.producto_dao = ProductoDAO()

    def selectProductosConStock(self):
        return self.producto_dao.selectAll()

    def updateStock(self, producto, cantidad):
        self.producto_dao.updateStock(producto.id_producto, cantidad)
    def findById(self, id_producto):
        return self.producto_dao.findById(id_producto)