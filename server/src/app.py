import os
from flask import Flask, jsonify

JSON_FILEPATH = 'json_files'

app = Flask(__name__)

def get_full_path(filename):
    json_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), JSON_FILEPATH)
    return os.path.join(json_dir, filename)


def get_json_file(filename):
    full_path = get_full_path(filename)

    if os.path.isfile(full_path):
        with open(full_path) as f:
            return f.read()
    else:
        app.logger.error("filename [%s] doesn't exist ", filename)

    return {}

@app.route('/reports')
def reports():
    reports_file = get_json_file('reports.json')    

    return jsonify(reports_file)

