from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    #return jsonify({"data" : "Hello World"})
    return ({"Available Routes" : ["GET /api/ping", "GET /api/posts"]})

if __name__ == '__main__':
   app.run()