from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "data" : data,
        "message" : "Success!"
    }), 200

@app.route("/planet")
def planet():
    name = request.args.get("name")
    # The next function is used to find a dictionary that satisfies the if condition.
    planet_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data" : planet_data,
        "message" : "Success!"
    }), 200
# To check the output for specific exo planet:
# http://127.0.0.1:5000/planet?name=14%20Andromedae%20b
if __name__ == "__main__":
    app.run(debug = True)


