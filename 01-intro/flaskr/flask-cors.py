#!/usr/bin/env python
# coding: utf-8

# # Flask-CORS
# In your Flask applications, you'll use the Flask-CORS library to enable CORS.
# Below you'll see samples of how to use Flask-CORS to enable different configurations of CORS. Try reading and analyzing the code before using the tooltips to hear the explanations.

# Import Dependencies
from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    #   CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PATCH,POST,DELETE,OPTIONS"
        )
        return response

    @app.route("/messages")
    @cross_origin()
    def get_messages():
        return "GETTING MESSAGES"
