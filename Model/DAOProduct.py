# DAO/ProductoDAO.py
import psycopg2
from Model.producto import Producto
from Model.connect import connect

class ProductoDAO:
    def select_all(self):
        sql = "SELECT * FROM productos WHERE existencias > 0;"
        productos = []
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        productos.append(Producto(*row))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return productos

    def update_existencias(self, id_producto, cantidad):
        sql = "UPDATE productos SET existencias = existencias - %s WHERE id_producto = %s;"
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (cantidad, id_producto))
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)