# hello-api-python-flask/app.py
from flask import Flask, jsonify, request


# Initialize the app
app = Flask(__name__)

# Define what the app does


@app.get("/greet")
def index():

    return jsonify("Hello, World")
