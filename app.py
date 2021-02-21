'''
Filename: app.py
- Main file for displaying
the project
'''

# MARK: - Libraries
from flask import Flask, request, render_template
import hashlib


app = Flask(__name__)

# MARK: - / Route
@app.route('/')
def index(): 
    return render_template('index.html')


# MARK: - /login Route
@app.route('/login', methods = ['GET', 'POST'])
def login():
    print("Log In User Reuest Recieved") 
    error = None 
    if request.method == 'POST':
        if (request.form['username'] != 'admin' and request.form['password'] != 'admin'): 
            error ='Invalid Credentials'
        else: 
            return render_template('home.html')
    return render_template('login.html', error=error)

@app.route('/mainpage', methods=["POST"])
def uploadFile():
    print("Trying to upload file")
    if request.method == 'POST':
        print("File Upload Attempt")
        uploadedFile = request.files['file']
        #hashName = hashlib.sha224(uploadedFile.filename).hexdigest()
        hashName = "Ab1ZK"
        print("Hash Name: ", hashName)
        if uploadedFile.filename != '': 
            print("Send file to IPFS node") 
            return render_template('home.html', filename=uploadedFile.filename, hash=hashName)
   
@app.route('/mainpage')
def makeHome(): 
    return render_template('home.html')


if __name__ == '__main__': 
    app.run(debug = True)
