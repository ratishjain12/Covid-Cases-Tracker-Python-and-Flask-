from flask import Flask,render_template,redirect
import requests
import json
app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
	api = requests.get('https://api.covid19india.org/data.json')
	data_json = api.json()
	for d in data_json['cases_time_series']:
		data = {"confirmed_cases":d['dailyconfirmed'],'recovered':d['dailyrecovered'],"date":d["date"]}
		
	
	return render_template("index.html",data_json=data)
	


