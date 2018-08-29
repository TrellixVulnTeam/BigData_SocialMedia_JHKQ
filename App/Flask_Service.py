from flask import Flask, request, jsonify
from flask_restful import Resource, Api 
import json
from flask_cors import CORS

app = Flask(__name__) #create the Flask app
CORS(app)

@app.route('/model', methods=['POST']) #GET requests will be blocked
def doResponse():
    response = ""
    data = request.get_json()
    print(data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)