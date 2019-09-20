from flask import Flask, render_template
import json
import requests
import os

app = Flask(__name__, static_url_path='/static')

API_ADDR = os.environ['API_URL'] if 'API_URL' in os.environ else "https://api.naesheim.com/v1/getlatest"

def get_latest():
    r = requests.get(API_ADDR)
    try:
        response = { 'latlon' :[r[1],r[2]], 'time' : r[3]}
    except TypeError:
        return {'locations' : 'empty'}

    return json.dumps(response)

@app.route("/")
def base():
    return render_template('index.html', data=get_latest())

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
