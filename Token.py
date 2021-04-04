# export FLASK_APP=Token.py
# flask run -h localhost -p 8080

from datetime import datetime
from datetime import timedelta
import secrets
import connectionDB
from flask import Flask

app = Flask(__name__)

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


@app.route('/update-token/<id>')
def update_token(id):
    try:

        state = generate_token()

        sql = "UPDATE token SET `token`='" + state["token"] + \
              "', `expiration_date`='" + state["finish"].__str__() + \
              "', `creation_date`='" + state["initial"].__str__() + \
              "' WHERE token_id ='" + id + "';"
        connection_cursor.execute(sql)
        connection.commit()
        return {"id": id}, 200
    except:
        return 'Database connection failed', 500


@app.route('/read-token/<id>')
def read_token(id):
    try:
        sql = "SELECT * FROM token WHERE token_id ='" + id + "'"
        connection_cursor.execute(sql)

        result = connection_cursor.fetchall()
        state = {
            "id": result[0][0],
            "token": result[0][1],
            "initial": result[0][3],
            "finish": result[0][2]
        }
        return state, 200
    except:
        return 'Database connection failed', 500


@app.route('/create-token/')
def create_token():
    try:
        state = generate_token()

        sql = "INSERT INTO token (token, expiration_date, creation_date) VALUES (%s, %s, %s)"
        val = (state["token"], state["finish"], state["initial"])
        connection_cursor.execute(sql, val)
        connection.commit()

        return {"id": connection_cursor.lastrowid}, 200
    except:
        return 'Database connection failed', 500