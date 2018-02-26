import base64
import json
import logging
import os

from flask import current_app, Flask, render_template, request, jsonify

from domain import root
from domain.profiles import insights

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    res = root.obj
    return jsonify(res)

@app.route('/profiles', methods=['GET'])
def insights():
    user = request.args.get('user')
    origin = request.args.get('origin')

    res = insights.obj
    return jsonify(res)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """Uh oh!""".format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
