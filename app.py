from flask import Flask, render_template, jsonify
from algo import generateRand
import time
import json
import requests

app = Flask(__name__)

#global router
@app.route('/')
def home():
        return render_template('index.html')

#requiet api route. get prayer time from solat.my , and no vacancy of prayer hall 
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
        else:
        # error
                print(f'Error: {response.status_code}')
        
        data = {'num': generateRand(),'hijri': hijri, 'fajr':fajr, 'zuhr':zuhr, 'asr':asr, 'maghrib':maghrib, 'isya':isya}
        print(data)
        return jsonify(data)        


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run()
