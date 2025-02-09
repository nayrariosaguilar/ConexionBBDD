import psycopg2

from Model.connect import connect


def select_product():
    """ Select stock from products table """

    sql = """SELECT * FROM productos
             WHERE existencias > 0;"""

    try:
        with  connect() as conn:
            with  conn.cursor() as cur:
                # execute the SELECT statement
                cur.execute(sql)

                # get the generated id back
                rows = cur.fetchall()
                for product_stock in rows:
                    print(product_stock)

                    # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return product_stock


if __name__ == '__main__':
    result = select_product()
    if result:
        print(f"🎯 Primer producto con stock tiene ID: {result}")
    else:
        print("⚠️ No se encontraron productos en stock o hubo un error.")