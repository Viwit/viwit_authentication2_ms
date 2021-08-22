from datetime import datetime
from datetime import timedelta
import secrets
import connectionDB
import sys

token_types = {'Login': "Login", 'QR': "QR"}


def generate_token(type):
    token = secrets.token_hex(32)
    initial = datetime.now()

    if type == token_types['Login']:
        finish = initial + timedelta(minutes=15)
    elif type == token_types['QR']:
        finish = initial + timedelta(minutes=3)
    else:
        return

    initial = initial.strftime('%Y-%m-%d %H:%M:%S')
    finish = finish.strftime('%Y-%m-%d %H:%M:%S')

    state = {
        "token": token,
        "initial": initial,
        "finish": finish
    }
    return state


def put_token(id, token):
    try:
        state_initial = get_token(id, token)
        state = generate_token(state_initial["type"].__str__())

        if state_initial["finish"].__str__() > state["initial"].__str__():
            sql = "UPDATE tokens SET `expiration_date`='" + state["finish"].__str__() + \
                  "', `creation_date`='" + state["initial"].__str__() + \
                  "' WHERE user_id ='" + id + "' AND token ='" + state_initial["token"] + "'"

            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute(sql)
            connection.commit()
            connection_cursor.close()
            connection.close()

            return {"token": get_token(id, token), "isValid": 1}, 200
        else:
            return {"token": get_token(id, token), "isValid": 0}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500


def get_token(id, token):
    try:
        sql = "SELECT * FROM tokens WHERE user_id ='" + id + "' AND token ='" + token.__str__() + "'"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)

        result = connection_cursor.fetchall()
        state = {
            "id": result[0][0],
            "token": result[0][1],
            "initial": result[0][4],
            "finish": result[0][3],
            "type": result[0][5]
        }

        connection_cursor.close()
        connection.close()

        return state
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}


def post_token(id, type):
    if type in token_types:
        try:
            state = generate_token(type)

            sql = "INSERT INTO tokens (token, user_id, expiration_date, creation_date, type) VALUES (%s, %s, %s, %s, %s)"
            val = (state["token"], id, state["finish"], state["initial"], type)

            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute(sql, val)
            connection.commit()

            new_id = connection_cursor.lastrowid

            connection_cursor.close()
            connection.close()
            return {"id": new_id, "token": state["token"]}, 200
        except:
            return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500
    else:
        return {"error 1": "bad request, type not found"}, 400


def delete_token(id, token):
    try:
        sql = "DELETE FROM tokens WHERE user_id ='" + id + "' AND token ='" + token.__str__() + "'"

        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)
        connection.commit()
        connection_cursor.close()
        connection.close()

        return {"message": "OK"}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500


def put_token_firebase(id, token, firebase):
    try:
        state_initial = get_token(id, token)
        state = generate_token(state_initial["type"].__str__())

        if state_initial["finish"].__str__() > state["initial"].__str__():
            sql = "UPDATE tokens SET `expiration_date`='" + state["finish"].__str__() + \
                  "', `creation_date`='" + state["initial"].__str__() + \
                  "', `token_firebase`='" + firebase.__str__() + \
                  "' WHERE user_id ='" + id + "' AND token ='" + state_initial["token"] + "'"

            connection = connectionDB.open_connection()
            connection_cursor = connection.cursor()
            connection_cursor.execute(sql)
            connection.commit()
            connection_cursor.close()
            connection.close()

            return {"token": get_token(id, token), "isValid": 1}, 200
        else:
            return {"token": get_token(id, token), "isValid": 0}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500


def get_token_firebase(id):
    try:
        sql = "SELECT * FROM `tokens` WHERE user_id = '" + id + "' AND NOT token_firebase = 'NULL'"
        connection = connectionDB.open_connection()
        connection_cursor = connection.cursor()
        connection_cursor.execute(sql)

        result = connection_cursor.fetchall()
        return_result = []
        initial = datetime.now()
        initial = initial.strftime('%Y-%m-%d %H:%M:%S')
        for i in range(0, len(result)):
            state = {
                "token_id": result[i][0],
                "token": result[i][1],
                "user_id": result[i][2],
                "expiration_date": result[i][3],
                "creation_date": result[i][4],
                "type": result[i][5],
                "token_firebase": result[i][6],
            }
            if state["expiration_date"].__str__() > initial.__str__():
                return_result.append(state)
        connection_cursor.close()
        connection.close()

        return {"result": return_result}, 200
    except:
        return {"error 1": str(sys.exc_info()[0]), "error 2": str(sys.exc_info()[1])}, 500
