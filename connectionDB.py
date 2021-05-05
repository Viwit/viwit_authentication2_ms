import mysql.connector
import sys


database = "authentication"
host = "authentication.cjareiirr0dz.us-east-1.rds.amazonaws.com"
user = "root"
password = "jbj4cNRqd7NWnMd"

def open_connection():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            auth_plugin='mysql_native_password',
            database=database
        )
        print("Se ha realizado la conexion a " + database)
        return connection

    except:
        print("No se ha logrado la conexion a la base de datos: ")
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])


