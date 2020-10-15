from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    @app.route("/")
    def index():
        return jsonify({"hello": "world"})

    @app.route("/emoji")
    @cross_origin()
    def emoji():
        return jsonify({"emoji": "😂"})

    return app
