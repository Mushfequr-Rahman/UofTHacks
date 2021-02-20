from flask import Flask, request, render_template,url_for, redirect 
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')


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
    app.debug = True
    app.run()
    app.run(debug = True)
