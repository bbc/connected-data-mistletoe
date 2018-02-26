import base64
import json
import logging
import os

from flask import current_app, Flask, render_template, request, jsonify

from domain import root, profilesInsights

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    res = root.obj
    return jsonify(res)

@app.route('/profiles/?user=NkiahWTp0gXmbZXUGSv4kwO2jJUO593f2KjCwvBqrV0/?origin=insights', methods=['GET'])
def profilesInsights():
    res = profilesInsights.obj
    return jsonify(res)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """Uh oh!""".format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
