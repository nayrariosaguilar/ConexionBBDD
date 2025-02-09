# Controller/PedidoController.py
from Model.DAOpedido import PedidoDAO
from Model.DAOProduct import ProductoDAO

class PedidoController:
    def __init__(self):
        self.pedido_dao = PedidoDAO()
        self.producto_dao = ProductoDAO()

    def crear_pedido(self, pedido):
        self.pedido_dao.insert(pedido)
        self.producto_dao.update_existencias(pedido.producto, pedido.cant)

    def eliminar_pedido(self, num_pedido):
        self.pedido_dao.delete(num_pedido)