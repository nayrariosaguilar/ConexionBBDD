from  Model.DAOProduct import ProductoDAO

#AÑADIMOS CONTROLES A LAS OPERACIONES DE PRODUCTOS, itermediario entre el modelo y la vista
class ProductoController:
    def __init__(self):
        self.producto_dao = ProductoDAO()
#Para visualizar los productos disponibles
    def selectProductosConStock(self):
        return self.producto_dao.selectAll()
#Para visualizar los productos que no tienen stock
    def updateStock(self, producto, cantidad):
        self.producto_dao.updateStock(producto.id_producto, cantidad)
#Para ver los datos de un producto en concreto
    def findById(self, id_producto):
        return self.producto_dao.findById(id_producto)