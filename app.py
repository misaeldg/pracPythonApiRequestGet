from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

 
@app.route('/employee', methods=['GET'])
def home():
    r = requests.get('http://dummy.restapiexample.com/api/v1/employees')

    r3 = r.json()

    print(""+str(r3["data"][1]))

    #return r.json()
    return r3["data"][4]
 
if __name__ == '__main__':
   app.run(debug = True)

