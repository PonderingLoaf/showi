from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)


@app.route("/test")
def test():
    return jsonify({"message": "test successful"})


if __name__ == "__main__":
    app.run(debug=True)
