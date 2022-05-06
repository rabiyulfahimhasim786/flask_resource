from flask import Flask, render_template, request, json
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/signin", methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        return json.dumps({'validation' : validateUser(username, password)})
    return json.dumps({'validation' : False})

def validateUser(username, password):
    return True
    

app.run(host='0.0.0.0', port=8080)