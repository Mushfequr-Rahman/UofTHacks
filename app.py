from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/renderLogin')
def renderLogin(): 
    return render_template('login.html') 

@app.route('/login', methods = ['GET', 'POST'])
def validateUser(): 
    pass 



if __name__ == '__main__': 
    app.debug = True
    app.run()
    app.run(debug = True)
