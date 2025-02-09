# DAO/PedidoDAO.py
import psycopg2
from Model.pedido import Pedido
from Model.connect import connect

class PedidoDAO:
    def insert(self, pedido):
        sql = """INSERT INTO pedidos (num_pedido, fecha_pedido, clie, rep, fab, producto, cant, importe)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (pedido.num_pedido, pedido.fecha_pedido, pedido.clie, pedido.rep, pedido.fab, pedido.producto, pedido.cant, pedido.importe))
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete(self, num_pedido):
        sql = "DELETE FROM pedidos WHERE num_pedido = %s;"
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (num_pedido,))
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)