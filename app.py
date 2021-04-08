from flask import Flask, jsonify
import json 

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi"

@app.route('/properties/<record>', methods=['GET'])
def get_records(record):
    with open('Data/data.json') as f:
        data = json.load(f)

    if record in data:
        return {record : data[record]}, 200

@app.route('/properties')
def properties():
    with open('Data/data.json') as f:
        data = json.load(f)

    # s1 = json.dumps(data, indent=4, sort_keys=True)
    return {'Properties': Flask.jsonify(data)}, 200  

if __name__ == '__main__':
    app.run()