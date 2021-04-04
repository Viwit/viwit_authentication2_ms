import mysql.connector

database = "viwit"
host = "localhost"
user = "root"
password = "Password123#@!"


def connect():
    while True:
        try:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                auth_plugin='mysql_native_password',
                database=database
            )
            print("Se ha realizado la conexión a " + database)
            return mydb
        except:
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
                print("ERROR")
