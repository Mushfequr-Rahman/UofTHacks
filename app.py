'''
Filename: app.py
- Main file for displaying
the project
'''

# MARK: - Libraries
from flask import Flask, request, redirect, render_template
import hashlib
import ipfshttpclient
import requests
import json

# Database
from backend.db import database
from backend.user_model import User, Hashes


app = Flask(__name__)

p2boxDB = database()

# MARK: - / Route
@app.route('/')
def index(): 
    return render_template('index.html')


# MARK: - /login Route
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None 
    if request.method == 'POST':

        req = request.form

        getDemoAdmin = p2boxDB.find(1)
        print(getDemoAdmin["user"])
        print(req["user"])
        if (req['user'] != getDemoAdmin["user"] or req["password"] != getDemoAdmin["pwd"]): 
            feedback = "Wrong user and pass."
            return render_template("login.html", feedback=feedback)
        else: 
            return render_template('home.html')
    return render_template('login.html', error=error)



# MARK: - /mainpage
@app.route('/mainpage', methods=["POST"])
def uploadFile():
    if request.method == 'POST':
        api =  ipfshttpclient.connect('/ip4/138.197.130.102/tcp/8080')
        print("File Upload Attempt")
        uploadedFile = request.files['file']
        if uploadedFile.filename != '': 
            r = requests.post("https://uoft.et0.me/api/v0/version?stream-channels=true%22", uploadedFile)
            print(r.json())
            return render_template('home.html', filename=uploadedFile.filename)
"""
@app.route('/mainpage', methods=["GET"])
def getFile(): 
    return "Function to get FIle"
""" 
@app.route('/mainpage')
def makeHome(): 
    return render_template('home.html')


def getVersion():
    req = requests.post("https://uoft.et0.me/api/v0/version")
    return req.json()

if __name__ == '__main__':     
    app.run(debug = True)
