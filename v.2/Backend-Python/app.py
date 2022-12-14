import json
import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
import requests

import config
from game import Game


load_dotenv()

app = Flask(__name__)
# added cors
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# DB Connection
config.conn = mysql.connector.connect(
    host=os.environ.get('HOST'),
    port=3306,
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASS'),
    autocommit=True
)\




def fly(id, dest, consumption=0, player=None):
    if id == 0:
        game = Game(0, dest, consumption, player)
    else:
        game = Game(id, dest, consumption)
    game.location[0].fetchWeather(game)
    nearby = game.location[0].find_nearby_airports()
    for a in nearby:
        game.location.append(a)
    #     add property to check game finished somehwere here or game.py (fetchgoalinfo) if all goals me
    json_data = json.dumps(game, default=lambda o: o.__dict__, indent=4)
    return json_data


# http://127.0.0.1:5000/flyto?game=fEC7n0loeL95awIxgY7M&dest=EFHK&consumption=123
@app.route('/flyto')
def flyto():
    args = request.args
    id = args.get("game")
    dest = args.get("dest")
    consumption = args.get("consumption")
    json_data = fly(id, dest, consumption)
    print("*** Called flyto endpoint ***")
    return json_data
# endpoint for continent


@app.route('/continent/<continent>')
def airports_by_country(continent):
    sql = f'''SELECT ident, name, latitude_deg, longitude_deg
              FROM airport
              WHERE continent = %s AND type ='large_airport' '''
    cursor = config.conn.cursor(dictionary=True)
    cursor.execute(sql, (continent,))
    result = json.dumps(cursor.fetchall())
    print(result)
    return result

# http://127.0.0.1:5000/newgame?player=Vesa&loc=EFHK
@app.route('/newgame')
def newgame():
    args = request.args
    player = args.get("player")
    dest = args.get("loc")
    json_data = fly(0, dest, 0, player)
    return json_data



apikey = "860bb330bc46d74511f5ed55ff8b4cf0"


@app.route('/getweather/<location>')
def getweather(location):
    request2 = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + apikey 
    try:
        response2 = requests.get(request2)
        if response2.status_code == 200:
            json_response2 = response2.json()
            return json_response2

    except requests.exceptions.RequestException as e:
        print("Request could not be completed.")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
