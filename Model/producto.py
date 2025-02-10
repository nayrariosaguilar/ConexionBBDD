#clase POJO para simular un producto
class Producto:
    def __init__(self, id_fab, id_producto,descripcion, precio, existencias):
        self.id_fab = id_fab
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias

#Visualización de producto
    def __str__(self):
        return f"ID: {self.id_producto}, Descripción: {self.descripcion}, Precio: {self.precio}, Existencias: {self.existencias}, ID Fabricante: {self.id_fab}"