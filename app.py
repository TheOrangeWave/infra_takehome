from flask import Flask
import requests
import json
import sqlite3


app = Flask(__name__)


def get_bird(state: str):
    conn = sqlite3.connect("./birds.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    print(f"select * from birds where abbreviation = '{state}';")
    row = cursor.execute(f"select * from birds where abbreviation = '{state}';")
    res = row.fetchall()
    list_accumulator = []
    for item in res:
        print(item)
        list_accumulator.append({k: item[k] for k in item.keys()})
    return json.dumps(list_accumulator)


def get_weather(state: str):
    r = requests.get(f'https://api.weather.gov/alerts/active?area={state}')
    return r.json()


@app.get('/')
def hello():
    return "Add a 2 letter state param to learn about birds and the weather challenges they face.", \
           200, \
           {'Content-Type': 'text/html; charset=utf-8'}


@app.get('/<state>')
def bird(state):

    bird = get_bird(state)
    print(bird)
    weather = get_weather(state)
    print(weather)
    out = json.dumps([bird, json.dumps(weather)])
    return out, 200, {'Content-Type': 'application/json'}

