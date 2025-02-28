import psycopg2


import psycopg2

class DatabaseAdapter:
    def __init__(self, host='192.168.56.101', dbname='stickerdb', user='postgres', password='1234'):
        """
        Inicializa el adaptador de base de datos con los parámetros de conexión

        :param host: Dirección del servidor de base de datos
        :param dbname: Nombre de la base de datos
        :param user: Nombre de usuario
        :param password: Contraseña de usuario
        """
        self.connection_params = {
            'host': host,
            'dbname': dbname,
            'user': user,
            'password': password
        }
        self.connection = None

    def connect(self):
        """
        Establece una nueva conexión a la base de datos

        :return: True si la conexión se establece correctamente, False en caso contrario
        """
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            print("Connexió establerta correctament")
            return True
        except psycopg2.Error as e:
            print(f"Error en establir la connexió: {e}")
            return False

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            query_type = query.strip().upper().split()[0]

            if query_type == "SELECT":
                return self.fetch_all(cursor)
            elif query_type in ["INSERT", "UPDATE", "DELETE"]:
                self.connection.commit()
                return cursor.rowcount
            else:
                self.connection.commit()
                return True
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def fetch_all(self, cursor):
        """
        Obtiene todos los resultados de una consulta SELECT

        :param cursor: Cursor de la base de datos
        :return: Lista de resultados
        """
        try:
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener resultados: {e}")
            return []

    def fetch_one(self, cursor):
        """
        Obtiene un solo resultado

        :param cursor: Cursor de la base de datos
        :return: Un resultado o None
        """
        try:
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener resultado: {e}")
            return None

    def execute_select(self, query, params=None):
        """
        Ejecuta una consulta SELECT y devuelve los resultados

        :param query: Consulta SQL SELECT
        :param params: Parámetros para la consulta (opcional)
        :return: Lista de resultados
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return self.fetch_all(cursor)
        except Exception as e:
            print(f"Error al ejecutar SELECT: {e}")
            return []

    def execute_update(self, query, params=None):
        """
        Ejecuta una actualización y devuelve el número de filas afectadas

        :param query: Consulta SQL UPDATE
        :param params: Parámetros para la consulta (opcional)
        :return: Número de filas afectadas
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al ejecutar UPDATE: {e}")
            self.connection.rollback()
            return 0

    def execute_insert(self, query, params=None):
        """
        Ejecuta una inserción y devuelve el ID insertado si está disponible

        :param query: Consulta SQL INSERT
        :param params: Parámetros para la consulta (opcional)
        :return: ID insertado o número de filas
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()

            # Intentar obtener el ID insertado (específico para PostgreSQL)
            try:
                return cursor.fetchone()[0]  # Para consultas con RETURNING id
            except:
                return cursor.rowcount  # Si no hay RETURNING, devolver filas afectadas
        except Exception as e:
            print(f"Error al ejecutar INSERT: {e}")
            self.connection.rollback()
            return None

    def execute_delete(self, query, params=None):
        """
        Ejecuta una eliminación y devuelve el número de filas eliminadas

        :param query: Consulta SQL DELETE
        :param params: Parámetros para la consulta (opcional)
        :return: Número de filas eliminadas
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al ejecutar DELETE: {e}")
            self.connection.rollback()
            return 0

    def close(self):
        """
        Cierra la conexión a la base de datos
        """
        try:
            if self.connection:
                self.connection.close()
                print("Connexió tancada")
        except Exception as e:
            print(f"Error al tancar la connexió: {e}")