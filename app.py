from flask import Flask, render_template
import json
import requests
import os

app = Flask(__name__, static_url_path='/static')

API_ADDR = os.environ['API_URL']

def create_json(data):
    try:
        response = { 'latlon' : [data[1],data[2]], 'time' : data[3]}
        return response
    except TypeError:
        return { 'locations' : 'empty'}

def get_latest():
    r = requests.get(API_ADDR)
    return r.json()

@app.route("/")
def base():
    pos = get_latest()
    jsonified_data = create_json(pos)
    print(jsonified_data)
    return render_template('index.html', data=pos)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
