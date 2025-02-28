class DatabaseAdapter:
    def __init__(self, connection):
        self.connection = connection

    def execute_query(self, query, params=None):
        """
        Método general para ejecutar consultas
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            # Detectar el tipo de consulta
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
        """
        try:
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener resultados: {e}")
            return []

    def fetch_one(self, cursor):
        """
        Obtiene un solo resultado
        """
        try:
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener resultado: {e}")
            return None

    def execute_select(self, query, params=None):
        """
        Ejecuta una consulta SELECT y devuelve los resultados
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