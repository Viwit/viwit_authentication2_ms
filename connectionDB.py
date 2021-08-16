import mysql.connector
import sys

database = "ikHV5b7fXF"
host = "remotemysql.com"
user = "ikHV5b7fXF"
password = "sub54mrAjY"


def open_connection():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            auth_plugin='mysql_native_password',
            database=database
        )
        print("Se ha realizado la connexion a " + database)
        return connection

    except:
        print("No se ha logrado la connexion a la base de datos: ")
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
