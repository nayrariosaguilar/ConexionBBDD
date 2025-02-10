import psycopg2
from Model.connect import connect

#Controla la inserción y eliminación de pedidos en la base de datos

class PedidoDAO:
    #Para añadir pedidos con productos a la base de datos
    def insert(self, pedido):
        sql = """INSERT INTO pedidos (num_pedido, fecha_pedido, clie, rep, fab, producto, cant, importe) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (pedido.num_pedido, pedido.fecha_pedido, pedido.clie, pedido.rep, pedido.fab, pedido.producto, pedido.cant, pedido.importe))
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    #La opción de eliminar pedido al finalizar compra
    def delete(self, num_pedido):
        sql = """DELETE FROM pedidos WHERE num_pedido = %s;"""
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (num_pedido,))
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    #Obtengo el ultimo id la tabla
    def selectLastId(self):
        sql = """SELECT MAX(num_pedido) FROM pedidos;"""
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    row = cur.fetchone()
                    return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)