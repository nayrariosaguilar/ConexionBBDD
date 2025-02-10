from Model.DAOpedido import PedidoDAO
from Model.DAOProduct import ProductoDAO

#Intermediario entre el modelo y el main (la vista)
class PedidoController:
    def __init__(self):
        self.pedido_dao = PedidoDAO()
        self.producto_dao = ProductoDAO()

#Metodo para crear pedidos a partir de los productos seleccionados por el usuario
    def crearPedido(self, pedido):
        self.pedido_dao.insert(pedido)
        self.producto_dao.updateStock(pedido.producto, pedido.cant)

#Metodo para eliminar pedidos, cuando hayamos realizado la factura
    def eliminarPedido(self, num_pedido):
        self.pedido_dao.delete(num_pedido)

    def selectLastId(self):
        return self.pedido_dao.selectLastId()