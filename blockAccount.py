import connectionDB
import sys


def hello():
    return "HELLO", 200


def block_account(id_user):
    try:
        sql = "UPDATE users SET `block_account`='1' WHERE user_id ='" + id_user + "';"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)
        connection.commit()
        connection_cursor.close()
        connection.close()

        return {"message": "OK"}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500


def unlock_account(id_user):
    try:
        sql = "UPDATE users SET `block_account`='0' WHERE user_id ='" + id_user + "';"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)
        connection.commit()
        connection_cursor.close()
        connection.close()

        return {"message": "OK"}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500
