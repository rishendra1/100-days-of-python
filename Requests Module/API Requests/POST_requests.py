import json
from flask import Flask, request, jsonify

app = Flask(__name__)


# Example usage:
# http://127.0.0.1:5000/get-user/123?extra={"age":25,"city":"Delhi"}
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "username": "Rishendra",
        "email": "rishendra009@gmail.com",
    }

    # GET Request: An HTTP method primarily used to retrieve data from a server.
    # When you visit a website or request information from an API,
    # a GET request is typically made.

    extra = request.args.get("extra")
    if extra:
        try:
            user_data["extra"] = json.loads(extra)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON in 'extra' parameter"}), 400

    return jsonify(user_data), 200
@app.route("/create-user/", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201
if __name__ == "__main__":
    app.run(debug=True)
