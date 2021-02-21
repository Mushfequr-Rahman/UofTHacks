'''
Filename: app.py
- Main file for displaying
the project
'''

# MARK: - Libraries
from flask import Flask, request, redirect, render_template, url_for, session
import hashlib
import ipfshttpclient
import requests
import json

# Database
from backend.db import database
from backend.user_model import User, Hashes


app = Flask(__name__)
app.secret_key = "UofTHACKSESSSION"
p2boxDB = database()
# api =  ipfshttpclient.connect('/dns/uoft.et0.me/tcp/80/http')
# res = api.add('README.md')

# MARK: - / Route
@app.route('/')
def index(): 
    return render_template('index.html')


# MARK: - /login Route
@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'POST':

        req = request.form
        session.clear()
        getDemoAdmin = p2boxDB.find(1)
        print(getDemoAdmin["user"])
        print(req["user"])
        if (req['user'] != getDemoAdmin["user"] or req["password"] != getDemoAdmin["pwd"]): 
            feedback = "Wrong user and pass."
            return render_template("login.html", feedback=feedback)
        else: 
            session['loginOK'] = True
            session['userID'] = getDemoAdmin["_id"]
            return redirect('mainpage')
    return render_template('login.html')



# MARK: - /mainpage
@app.route('/mainpage', methods=["GET" ,"POST"])
def uploadFile():
    
    if session['loginOK']:
        print(session['loginOK'])
        return render_template('home.html')

    elif request.method == 'POST':
        api =  ipfshttpclient.connect('/ip4/138.197.130.102/tcp/8080')
        print("File Upload Attempt")
        uploadedFile = request.files['file']
        #hashName = hashlib.sha224(uploadedFile.filename).hexdigest()
        hashName = "Ab1ZK"
        print("Hash Name: ", hashName)
        if uploadedFile.filename != '': 
            new_file = api.add(uploadedFile) 
            print(new_file)
            return render_template('home.html', filename=uploadedFile.filename, hash=hashName)
    
    else:
        return redirect('login')

@app.route('/mainpage', methods=["GET"])
def getFile(): 
    return "Function to get FIle"

@app.route('/mainpage')
def makeHome(): 
    return render_template('home.html')


def getVersion():
    req = requests.post("https://uoft.et0.me/api/v0/version")
    return req.json()

if __name__ == '__main__':     
    app.run(debug = True)
