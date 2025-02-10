import psycopg2
from Model.producto import Producto
from Model.connect import connect

#Controla la selección y actualización de productos en la base de datos

class ProductoDAO:
    #Selecciona todos los product con stock mayor a 0
    def selectAll(self):
        sql = """SELECT * FROM productos WHERE existencias > 0;"""
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

    #Actualiza el stock de un producto, asi restamos los producto que compramos
    def updateStock(self, id_producto, cantidad):
        sql = """UPDATE productos SET existencias = existencias - %s WHERE id_producto = %s;"""
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (cantidad, id_producto))
                    conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    #Selecciona un producto por su id
    def findById(self, id_producto):
        sql = """SELECT * FROM productos WHERE id_producto = %s;"""
        try:
            with connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (id_producto,))
                    row = cur.fetchone()
                    return Producto(*row)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None