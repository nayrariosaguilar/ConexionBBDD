import psycopg2
from psycopg2 import Error

def connect():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="127.0.0.1",
                                      port="5432",
                                      dbname="training")
        return connection.cursor()

    except (Exception,Error) as error:
        print("Error while connecting to PostgreSQL", error)

if __name__ == '__main__':
    connect()