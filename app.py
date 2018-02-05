import base64
import json
import logging
import os

from flask import current_app, Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return "I think you'd like Star Wars"
    return 'OK', 200

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """Uh oh!""".format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
