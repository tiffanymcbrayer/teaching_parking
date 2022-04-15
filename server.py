from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/learn/<l>')
def learn():
    pass

@app.route('/quiz/<q>')
def quiz():
    pass

if __name__ == '__main__':
    app.run(debug = True)
