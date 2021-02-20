'''
Filename: app.py
- Main file for displaying
the project
'''

# MARK: - Libraries
from flask import Flask, request, render_template


app = Flask(__name__)

# MARK: - / Route
@app.route('/')
def index(): 
    return render_template('index.html')

# MARK: - /renderLogin Route
@app.route('/renderLogin')
def renderLogin(): 
    return render_template('login.html') 

# MARK: - /login Route
@app.route('/login', methods = ['GET', 'POST'])
def validateUser(): 
    pass 



if __name__ == '__main__': 
    app.run(debug = True)
