from flask import Flask, render_template, jsonify
from yolov5.detect import printcount_vacancies
from numberExample import *
import time
import re
import json
import sqlite3
import requests

app = Flask(__name__)

#global router
@app.route('/')
def home():
        return render_template('index.html')

#requiet api route. get prayer time from solat.my , and no vacancy of prayer hall 
@app.route('/api')
def result_json():
        
        islamicMonth = ["Mhrm.","Safr.","Rab. I","Rab. II","jmd. I","Jmd. II","Rajb.","Shbn.","Rmdn.","Shwl.","Dhu'l-Q.","Dhu'l-H."]

        response = requests.get('https://solat.my/api/daily/sgr01')
        

        #count = printcount_vacancies() #to get number from YOLO
        vacancy = return_json() #to get number from numberExample
        # count = vacancy['value']
        print(vacancy)
        #count = 27
        if response.status_code == 200:
        # success
        
                conn = sqlite3.connect('numbers.db')
                c = conn.cursor()

                c.execute('SELECT * FROM vacancy ORDER BY rowid DESC LIMIT 1')
                row = c.fetchone()
                timestamp = row[0]
                count = row[1]
                conn.close()
    
    
                data1 = response.json()
                
                day = (data1['prayerTime'][0]['day'])[:3]
                date = (data1['prayerTime'][0]['date'])[:-5]
                date = date.replace('-',' ')
                date = day + ', ' + date    
                
                hijri = (data1['prayerTime'][0]['hijri'])
                # Split the hijri string into its year, month, and day components
                year, month, day = hijri.split('-')

                # Convert the month number to its corresponding month name
                month_name = islamicMonth[int(month)-1]

                # Format the date string as 'day month_name year AH'
                hijri = f"{day} {month_name} {year} AH"
                
                
                fajr = (data1['prayerTime'][0]['fajr'])[:-3]
                zuhr = (data1['prayerTime'][0]['dhuhr'])[:-3]
                asr = (data1['prayerTime'][0]['asr'])[:-3]
                maghrib = (data1['prayerTime'][0]['maghrib'])[:-3]
                isya = (data1['prayerTime'][0]['isha'])[:-3]
        else:
        # error
                print(f'Error: {response.status_code}')
        
        data = {'num': count,'date':date, 'hijri': hijri, 'fajr':fajr, 'zuhr':zuhr, 'asr':asr, 'maghrib':maghrib, 'isya':isya}
        return jsonify(data)        


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(port=5000)
