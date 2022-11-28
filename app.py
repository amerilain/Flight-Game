import json
import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS

import config
from main_functions import greetings

load_dotenv()

app = Flask(__name__)
# lisätty cors
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Tietokantayhteys
config.conn = mysql.connector.connect(
         host=os.environ.get('HOST'),
         port= 3306,
         database=os.environ.get('DB_NAME'),
         user=os.environ.get('DB_USER'),
         password=os.environ.get('DB_PASS'),
         autocommit=True