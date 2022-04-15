from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__)

learning = {
    
    "forward": {
        "name": "Forwards Parking",
        "steps": {1:"Drive forward until the mirror lines up with the parking line", 2:"Turn the wheel to your right and move forward into space", 
                3:"Once you are centered in the spot, straighten the wheel and move up to the line " },
        "media": []        
    },
    "reverse": {
        "name": "Reverse Parking",
        "steps": {1:"Drive forward until the mirror lines up with the parking line (keep close to the space)", 2:"Turn the wheel to your left and go forward until you see edge of parking line in left mirror", 
                3:"Once you are centered in the spot, straighten the wheel and back up to the line" }
    },
    "angled": {
        "name": "Angled Parking",
        "steps": {}
    },
    "parallel": {
        "name": "Parallel Parking",
        "steps": {}
    }
}

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/learn/<type>')
def learn(type = None):
    global learning
    parkingType = learning[type]
    return render_template('learn.html', parkingType = parkingType)

@app.route('/quiz/<q>')
def quiz():
    pass

if __name__ == '__main__':
    app.run(debug = True)
