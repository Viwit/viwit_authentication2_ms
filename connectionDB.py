import mysql.connector
import sys

database = "viwit"
host = "127.0.0.1"
user = "root"
password = "Password123#@!"


def connect():
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            auth_plugin='mysql_native_password',
            database=database
        )
        print("Se ha realizado la conexion a " + database)
        return mydb
    except:
	print("No se ha logrado la conexion a la base de datos: ")
	print(sys.exc_info()[0])
	print(sys.exc_info()[1])
        try:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                auth_plugin='mysql_native_password',
            )
            my_cursor = mydb.cursor()
            my_cursor.execute("CREATE DATABASE " + database)
            print("Se ha creado la base de datos " + database)
        except:
	    print("No se ha logrado crear la base de datos: ")
	    print(sys.exc_info()[0])
	    print(sys.exc_info()[1])
	    sys.exit(0)
