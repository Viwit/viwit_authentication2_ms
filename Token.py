from datetime import datetime
from datetime import timedelta
import secrets
import connectionDB
import sys


def generate_token():
    token = secrets.token_hex(20)
    initial = datetime.now()
    finish = initial + timedelta(minutes=1)

    initial = initial.strftime('%Y-%m-%d %H:%M:%S')
    finish = finish.strftime('%Y-%m-%d %H:%M:%S')

    state = {
        "token": token,
        "initial": initial,
        "finish": finish
    }
    return state


def put_token(id):
    try:

        state = generate_token()
        sql = "UPDATE tokens SET `token`='" + state["token"] + \
              "', `expiration_date`='" + state["finish"].__str__() + \
              "', `creation_date`='" + state["initial"].__str__() + \
              "' WHERE user_id ='" + id + "';"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)
        connection.commit()
        connection_cursor.close()
        connection.close()

        return {"id": id}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500


def get_token(id):
    try:
        sql = "SELECT * FROM tokens WHERE user_id ='" + id + "'"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)

        result = connection_cursor.fetchall()
        state = {
            "id": result[0][0],
            "token": result[0][1],
            "initial": result[0][4],
            "finish": result[0][3]
        }

        connection_cursor.close()
        connection.close()

        return state, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500


def post_token(id):
    try:
        state = generate_token()

        sql = "INSERT INTO tokens (token, user_id, expiration_date, creation_date) VALUES (%s, %s, %s, %s)"
        val = (state["token"], id, state["finish"], state["initial"])

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql, val)
        connection.commit()

        new_id = connection_cursor.lastrowid

        connection_cursor.close()
        connection.close()
        return {"id": new_id}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500


def delete_token(id):
    try:
        sql = "DELETE FROM tokens WHERE user_id ='" + id + "'"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)
        connection.commit()
        connection_cursor.close()
        connection.close()

        return {"message": "OK"}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500
