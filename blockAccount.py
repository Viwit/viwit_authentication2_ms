import connectionDB
import sys

connection = connectionDB.connect()
connection_cursor = connection.cursor()


def hello():
    return "HELLO", 200


def block_account(id_user):
    try:
        sql = "UPDATE users SET `block_account`='1', `credit_card`='1' WHERE user_id ='" + id_user + "';"
        connection_cursor.execute(sql)
        connection.commit()
        return {"message": "OK"}, 200
    except:
	print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        return {"message": "Database connection failed"}, 500


def unlock_account(id_user):
    try:
        sql = "UPDATE users SET `block_account`='0' WHERE user_id ='" + id_user + "';"
        connection_cursor.execute(sql)
        connection.commit()
        return {"message": "OK"}, 200
    except:
	print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        return {"message": "Database connection failed"}, 500
