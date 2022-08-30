from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

incomes = [
  { 'name': 'Mert Lale ile Python', 'amount': 5000 , "description" : "Hey gidi python" }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def books():
    return jsonify(incomes)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5005))
    app.run(debug=True, host='0.0.0.0', port=port)