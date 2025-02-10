#Clase POJO para simular un pedido
class Pedido:
    def __init__(self, num_pedido, fecha_pedido, clie, rep, fab, producto, cant, importe):
        self.num_pedido = num_pedido
        self.fecha_pedido = fecha_pedido
        self.clie = clie
        self.rep = rep
        self.fab = fab
        self.producto = producto
        self.cant = cant
        self.importe = importe

    def __str__(self):
        return f"Pedido: {self.num_pedido}, Fecha Pedido: {self.fecha_pedido}, Cliente: {self.clie}, Rep: {self.rep}, Fabricante: {self.fab}, Producto: {self.producto}, Cantidad: {self.cant}, Importe: {self.importe}"