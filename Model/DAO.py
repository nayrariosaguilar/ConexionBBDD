import psycopg2
from psycopg2 import Error


#Obrim una excepció per un intent de connexió a la base de dades
try:
    # Passem el servidor, el nom de la base de dades, l'usuari i el seu password
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  dbname="training")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query

    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
        print("PostgreSQL connection is closed")