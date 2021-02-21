'''
Filename: app.py
- Main file for displaying
the project
'''
import pathlib
# MARK: - Libraries
from flask import Flask, request, redirect, render_template, url_for, session
import requests as r
from werkzeug.utils import secure_filename
import datetime

# Database
from backend.db import database
from backend.user_model import User, Hashes


app = Flask(__name__)
app.secret_key = "UofTHACKSESSSION"
p2boxDB = database()
# api =  ipfshttpclient.connect('/dns/uoft.et0.me/tcp/80/http')
# res = api.add('README.md')

# MARK: - / Route

# MARK: - /login Route
@app.route('/', methods = ['GET', 'POST'])
def login():
    session.clear()
    if request.method == 'POST':

        req = request.form
        session.clear()
        getDemoAdmin = p2boxDB.find(1)

        if (req['user'] != getDemoAdmin["user"] or req["password"] != getDemoAdmin["pwd"]): 
            feedback = "Wrong user and pass."
            return render_template("login.html", feedback=feedback)
        else: 
            session['loginOK'] = True
            session['userID'] = getDemoAdmin["_id"]
            return redirect('home')
    return render_template('login.html')



# MARK: - /home
@app.route('/home', methods=["GET"])
def home():
    if session.get('loginOK') is not None:
        if session["loginOK"]:
            
            if request.args.get('failed'):
                return render_template('home.html', failed=True)
            elif request.args.get("success"):
                return render_template('home.html', success=True, fileCID=request.args.get("fileCID"))
            else:
                return render_template("home.html")
    else:
        return redirect('/')

# MARK: - Upload to IPFS Node
@app.route('/home', methods=["POST"])
def addIPFS():
    
    if request.method == "GET":
        return redirect('home')
    
    print(request.files['userFile'])
    if 'userFile' not in request.files:
        return redirect(url_for("home", failed=True))
    
    usersFiles = request.files['userFile']

    if usersFiles:
        # Temp saving file
        secFilename = secure_filename(usersFiles.filename)
        usersFiles.save(secFilename)
        tempFile= open(secFilename, "rb")
        
        ipfsClient = r.post("https://uoft.et0.me/api/v0/add", files={"file": tempFile})
        res = ipfsClient.json()
        newHash = Hashes(res["Hash"], datetime.datetime.now().utcnow()).new()
        pathlib.Path(secFilename).unlink()

        currentUser = p2boxDB.find(session["userID"])
        if "hashes" in currentUser:
            for item in currentUser["hashes"]:
                if item["hash"] != res["Hash"]:
                    p2boxDB.update_hash(session["userID"], newHash)
        else:
            p2boxDB.update_hash(session["userID"], newHash)

        if ipfsClient.reason != "OK":
            return redirect(url_for("home", failed=True ))

        return redirect(url_for("home", fileCID=res["Hash"], success=True ))
    

@app.route('/files', methods=["GET"])
def getFile(): 

    return render_template('upload.html')



def getVersion():
    req = requests.post("https://uoft.et0.me/api/v0/version")
    return req.json()

if __name__ == '__main__':     
    app.run(debug = True)
