from datetime import datetime
from Controlador.ProductController import ProductoController
from Controlador.pedidoController import PedidoController
from Model.pedido import Pedido

def mostrar_productos(productoC):
    productos = productoC.selectProductosConStock()
    for producto in productos:
        print(producto)

def mostrar_cistella(cistella):
    if not cistella:
        print("La cistella està buida.")
    else:
        for item in cistella:
            print(item)

def generar_factura(pedidoC, cesta):
    if not cesta:
        print("La cistella està buida.")
        return

    for pedidoUser in cesta:
        pedidoC.crearPedido(pedidoUser)
    opcion = input("Borrar cesta opción 1 o seguir comprando opción 2: ")

    if opcion == '1':
        cesta.clear()
        print("Cistella esborrada.")
    elif opcion == '2':
        print("Continua comprant.")

def main():
    productoC = ProductoController()
    pedidoC = PedidoController()
    cistella = []

    while True:
        print("\nOpcions:")
        print("1- Comprar un producte")
        print("2- Mostrar la cistella de la compra")
        print("3- Generar factura")
        print("4- Sortir")
        opcion = input("Selecciona una opció: ")

        if opcion == '1':
            mostrar_productos(productoC)
            id_producto = input("Introduce el id del producto: ")
            producto = productoC.findById(id_producto)
            if producto is None:
                print("El producto no existe, introduce uno válido")
                continue
            id_pedido = pedidoC.selectLastId()+1
            try:
                cantidad = int(input("Introduce la cantidad: "))
                numPedido = id_pedido
                fecha_pedido = datetime.today().strftime('%Y-%m-%d')
                clie = int(input("Introduce el número de cliente: "))
                rep = int(input("Introduce el número de representante: "))
                fab = producto.id_fab
                importe = producto.precio * cantidad
            except ValueError:
                print("Introduce un valor válido.")
                continue

            pedido = Pedido(numPedido, fecha_pedido, clie, rep, fab, id_producto, cantidad, importe)
            cistella.append(pedido)
            print("Producte afegit a la cistella.")
        elif opcion == '2':
            mostrar_cistella(cistella)
        elif opcion == '3':
            generar_factura(pedidoC, cistella)
        elif opcion == '4':
            print("GRACIAS POR VISITAR NUESTRA TIENDA")
            break
        else:
            print("OPCIÓ INCORRECTA")

if __name__ == '__main__':
    main()