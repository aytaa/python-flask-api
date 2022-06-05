from flask import Flask, session, request

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "username": "Aytac",
        "email": "aytac@aytacunal.com"
    }


@app.route("/users", methods=['GET', 'POST'])
def users():
    return {
        "username": "Aytac",
        "email": "aytac@aytacunal.com",
        "age": "34"
    }


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
