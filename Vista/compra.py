from datetime import datetime
from Controlador.ProductController import ProductoController
from Controlador.pedidoController import PedidoController
from Model.pedido import Pedido

#Metodo para mostrar los productos disponibles
def mostrar_productos(productoC):
    productos = productoC.selectProductosConStock()
    for producto in productos:
        print(producto)

#Metodo para mostrar la cesta de la compra
def mostrar_cistella(cesta):
    if not cesta:
        print("Cesta vacia")
    else:
        for item in cesta:
            print(item)
#Metodo para generar la factura
def generar_factura(pedidoC, cesta):
    if not cesta:
        print("Cesta vacia")
        return

    total = 0
    print("Factura generada.")
    for pedidoUser in cesta:
        print("Datos del emisor:")
        print("Cliente: ", pedidoUser.clie)
        print("Representante: ", pedidoUser.rep)

        print("Datos del receptor:")
        print("Número de pedido: ", pedidoUser.num_pedido)

        print("Datos del pedido:")
        print("Fecha del pedido: ", pedidoUser.fecha_pedido)
        print("Producto: ", pedidoUser.producto)
        print("Cantidad: ", pedidoUser.cant)

        print("Importe: ", pedidoUser.importe)
        total += pedidoUser.importe

    print("Total: ", total)

    opcion = input("Borrar cesta opción 1 o seguir comprando opción 2: ")

    if opcion == '1':
        cesta.clear()
        print("Cesta borrada.")
    elif opcion == '2':
        print("Seguir comprando.")

def main():
    productoC = ProductoController()
    pedidoC = PedidoController()
    cesta = []

    while True:
        print("\nOpcions:")
        print("1- Comprar un producto")
        print("2- Mostrar la cesta de la compra")
        print("3- Generar factura")
        print("4- Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_productos(productoC)
            id_producto = input("Introduce el id del producto: ")
            producto = productoC.findById(id_producto)
            if producto is None:
                print("El producto no existe, introduce uno válido")
                continue
                #generación de la id de producto de manera incremental
            id_pedido = pedidoC.selectLastId()+1

            try:
                #formulario para nuevo pedido
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

            #Primero creamos un pedidos con los datos proporcionados
            pedido = Pedido(numPedido, fecha_pedido, clie, rep, fab, id_producto, cantidad, importe)
            pedidoC.crearPedido(pedido)
            #Segundo paso IMPORTANTE actualizar las existencias
            pedidoC.updateStockPedido(pedido)
            #Por ultimo añadirlo a la cesta para luego mostrarlo
            cesta.append(pedido)
            print("Producte afegit a la cistella.")

        elif opcion == '2':
            mostrar_cistella(cesta)
        elif opcion == '3':
            generar_factura(pedidoC, cesta)
        elif opcion == '4':
            print("GRACIAS POR VISITAR NUESTRA TIENDA")
            break
        else:
            print("opción no válida")

if __name__ == '__main__':
    main()