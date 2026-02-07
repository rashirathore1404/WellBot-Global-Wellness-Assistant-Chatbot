from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask API"

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    result = data["a"] + data["b"]
    return jsonify({"sum": result})

if __name__ == "__main__":
    app.run(debug=True)
