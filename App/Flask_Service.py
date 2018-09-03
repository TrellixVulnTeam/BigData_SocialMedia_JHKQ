from flask import Flask,render_template,request,jsonify
from flask_restful import Resource,Api
from flask_cors import CORS
import json
import sys

app = Flask(__name__)  #create flask app
CORS(app)
@app.route('/home')
def forms():
    return 0
@app.route('/model', methods=['POST'])
def demo():
    info = request.get_json()
    aplha = info[0]['alpha']
    beta = info[0]['beta']
    print(aplha + " " + beta)
    concat = aplha + " " + beta     
    return  jsonify({'text' : concat})

if __name__ == '__main__':
    app.run(debug=True)