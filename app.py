<<<<<<< HEAD
from flask import Flask, request, render_template,url_for, redirect 
=======
'''
Filename: app.py
- Main file for displaying
the project
'''

# MARK: - Libraries
from flask import Flask, request, render_template


>>>>>>> 6d2546314a010d350241c91b830894367173670b
app = Flask(__name__)

# MARK: - / Route
@app.route('/')
def index(): 
    return render_template('index.html')

<<<<<<< HEAD
=======
# MARK: - /renderLogin Route
@app.route('/renderLogin')
def renderLogin(): 
    return render_template('login.html') 
>>>>>>> 6d2546314a010d350241c91b830894367173670b

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

@app.route('/mainpage')
def renderHomePage(): 
    return render_template('home.html')



if __name__ == '__main__': 
    app.run(debug = True)
