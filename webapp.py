import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"

@app.route('/say hello')
def hello():
    return 'Hello, how are you doing?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
