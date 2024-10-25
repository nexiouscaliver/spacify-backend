import os
import random
from datetime import date as dt
from datetime import datetime
from datetime import timedelta
import threading
from flask import *
from flask import jsonify, request, send_from_directory
# from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from logging.config import dictConfig
from subprocess import run
import dbserver as db         #FOR SQL SERVER DATABASE
import loginscript as login   #FOR SQL SERVER DATABASE
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key =  "spacIFY_792739"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'down_files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
TEMP_FOLDER = os.path.join(APP_ROOT, 'temp_files')
app.config['TEMP_FOLDER'] = TEMP_FOLDER
app.config['SECRET_KEY'] = "spacIFY_792739"

@app.route('/')
def home():
    #return redirect(url_for('intro'))
    return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/warelogin',methods=['POST'])
def warelogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login.load_ware(username,password):
            return jsonify("Login Successfull"), 200
        else:
            return jsonify("Login Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/warecreate',methods=['POST'])
def warecreate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        if login.create_ware(username,password,name):
            return jsonify("Account Created"), 200
        else:
            return jsonify("Account Creation Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/clientlogin',methods=['POST'])
def clientlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login.load_client(username,password):
            return jsonify("Login Successfull"), 200
        else:
            return jsonify("Login Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

@app.route('/api/v1/clientcreate',methods=['POST'])
def clientcreate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        if login.create_client(username,password,name):
            return jsonify("Account Created"), 200
        else:
            return jsonify("Account Creation Failed"), 404
    else:
        return jsonify("ERROR : contact the correct endpoint for the API"), 404

