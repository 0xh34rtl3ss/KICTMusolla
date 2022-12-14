from flask import Flask, render_template, jsonify,json, request
from algo import generateRand
import time

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/api')
def result_json():
        data = {'num': generateRand()}
        return jsonify(data)        


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run()
