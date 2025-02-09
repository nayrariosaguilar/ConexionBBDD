# main.py
from Controlador.ProductController import ProductoController
from Controlador.pedidoController import PedidoController
from Model.pedido import Pedido

def mostrar_productos(producto_controller):
    productos = producto_controller.obtener_productos_con_existencias()
    for producto in productos:
        print(producto)

def mostrar_cistella(cistella):
    if not cistella:
        print("La cistella està buida.")
    else:
        for item in cistella:
            print(item)


def generar_factura(pedido_controller, cistella):
    if not cistella:
        print("La cistella està buida.")
        return

    for pedido in cistella:
        pedido_controller.crear_pedido(pedido)

    print("Factura generada.")
    opcion = input("Vols esborrar la cistella (1) o seguir comprant (2)? ")
    if opcion == '1':
        cistella.clear()
        print("Cistella esborrada.")
    elif opcion == '2':
        print("Continua comprant.")


def main():
    producto_controller = ProductoController()
    pedido_controller = PedidoController()
    cistella = []

    while True:
        print("\nOpcions:")
        print("1- Comprar un producte")
        print("2- Mostrar la cistella de la compra")
        print("3- Generar factura")
        print("4- Sortir")
        opcion = input("Selecciona una opció: ")

        if opcion == '1':
            mostrar_productos(producto_controller)
            id_producto = input("Introdueix l'ID del producte que vols comprar: ")
            cantidad = int(input("Introdueix la quantitat: "))
            # Aquí pots afegir la lògica per obtenir els detalls del producte i crear un objecte Pedido
            # Suposant que tens un producte amb id_producto i una quantitat
            pedido = Pedido(1, '2023-10-10', 1, 1, 'FAB1', id_producto, cantidad, 1000)
            cistella.append(pedido)
            print("Producte afegit a la cistella.")
        elif opcion == '2':
            mostrar_cistella(cistella)
        elif opcion == '3':
            generar_factura(pedido_controller, cistella)
        elif opcion == '4':
            print("Sortint...")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")


if __name__ == '__main__':
    main()