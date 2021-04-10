import connectionDB

connection = connectionDB.connect()
connection_cursor = connection.cursor()


def hello():
    return "HELLO", 200


def block_account(id_user):
    sql = "UPDATE user_viwit SET `block_account`='1', `credit_card`='1' WHERE user_id ='" + id_user + "';"
    connection_cursor.execute(sql)
    connection.commit()
    return "OK", 200
    try:
        pass
    except:
        return 'Database connection failed', 500


def unlock_account(id_user):
    try:
        sql = "UPDATE user_viwit SET `block_account`='0' WHERE user_id ='" + id_user + "';"
        connection_cursor.execute(sql)
        connection.commit()
        return "OK", 200
    except:
        return 'Database connection failed', 500
