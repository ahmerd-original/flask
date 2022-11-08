from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/ahmerd')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app ahmerd suleman"})


if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))
