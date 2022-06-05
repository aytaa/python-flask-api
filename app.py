from flask import Flask, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="movie"
)


@app.route("/")
def home():
    return {
        "username": "Aytac",
        "email": "aytac@aytacunal.com"
    }


@app.route("/users", methods=['GET'])
def users():
    return {"name": "Jhone"}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return {"method": "POST"}
    else:
        return {"method": "GET"}


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return {"error": "Not Found"}


if __name__ == "__main__":
    app.run(debug=True)
