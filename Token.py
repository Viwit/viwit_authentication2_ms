from datetime import datetime
from datetime import timedelta
import secrets
import connectionDB

connection = connectionDB.connect()
connection_cursor = connection.cursor()


def generate_token():
    token = secrets.token_hex(20)
    initial = datetime.now()
    finish = initial + timedelta(minutes=1)

    initial = initial.strftime('%Y-%m-%d %H:%M:%S')
    finish = finish.strftime('%Y-%m-%d %H:%M:%S')
    state = {
        "id": connection_cursor.lastrowid,
        "token": token,
        "initial": initial,
        "finish": finish
    }
    return state


def update_token(id):
    try:

        state = generate_token()

        sql = "UPDATE tokens SET `token`='" + state["token"] + \
              "', `expiration_date`='" + state["finish"].__str__() + \
              "', `creation_date`='" + state["initial"].__str__() + \
              "' WHERE token_id ='" + id + "';"
        connection_cursor.execute(sql)
        connection.commit()
        return {"id": id}, 200
    except:
        return {"message": "Database connection failed"}, 500


def read_token(id):
    try:
        sql = "SELECT * FROM tokens WHERE user_id ='" + id + "'"
        connection_cursor.execute(sql)

        result = connection_cursor.fetchall()
        state = {
            "id": result[0][0],
            "token": result[0][2],
            "initial": result[0][4],
            "finish": result[0][3]
        }
        return state, 200
    except:
        return {"message": "Database connection failed"}, 500


def create_token(id):
    try:
        state = generate_token()

        sql = "INSERT INTO tokens (token, user_id, expiration_date, creation_date) VALUES (%s, %s, %s, %s)"
        val = (state["token"], id, state["finish"], state["initial"])
        connection_cursor.execute(sql, val)
        connection.commit()

        return {"id": connection_cursor.lastrowid}, 200
    except:
        return {"message": "Database connection failed"}, 500
