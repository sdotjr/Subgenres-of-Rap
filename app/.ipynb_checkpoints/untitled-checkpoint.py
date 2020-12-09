from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/<name>')
def hello(name=None):
    return render_template('temp.html', name=name)



