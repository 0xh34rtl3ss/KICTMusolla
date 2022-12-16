from flask import Flask, render_template, jsonify
from algo import generateRand
from flask_cors import CORS
import time
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/api')
def result_json():

        response = requests.get('https://solat.my/api/daily/sgr01')

        if response.status_code == 200:
        # success
                data1 = response.json()
                hijri = data1['prayerTime'][0]['hijri']
                fajr = data1['prayerTime'][0]['fajr']
                zuhr = data1['prayerTime'][0]['dhuhr']
                asr = data1['prayerTime'][0]['asr']
                maghrib = data1['prayerTime'][0]['maghrib']
                isya = data1['prayerTime'][0]['isha']
        # do something with the data here
        else:
        # error
                print(f'Error: {response.status_code}')
        
        data = {'num': generateRand(),'hijri': hijri, 'fajr':fajr, 'zuhr':zuhr, 'asr':asr, 'maghrib':maghrib, 'isya':isya}
        print(data)
        return jsonify(data)        


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run()
