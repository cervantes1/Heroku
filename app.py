from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Properties"

@app.route('/properties')
def properties():

    with open('Data/data.json') as f:
        data = json.load(f)

    return jsonify({'Properties': data}), 200  


@app.route('/properties/<record>', methods=['GET'])
def get_records(record):

    print(record)

    with open('Data/data.json') as f:
        data = json.load(f)

    if record in data:
        return jsonify({record : data[record]}), 200


if __name__ == '__main__':
    app.run()