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
        "media": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p1.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p2.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p3.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards.gif?raw=true"]        
    },
    "reverse": {
        "name": "Reverse Parking",
        "steps": {1:"Drive forward until the mirror lines up with the parking line (keep close to the space)", 2:"Turn the wheel to your left and go forward until you see edge of parking line in left mirror", 
                3:"Once you are centered in the spot, straighten the wheel and back up to the line" },
        "media": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p1.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p2.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p3.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p4.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p5.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse.gif?raw=true"]
    },
    "angled": {
        "name": "Angled Parking",
        "steps": {},
        "media": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p1.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p2.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p3.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled.gif?raw=true"] 
    },
    "parallel": {
        "name": "Parallel Parking",
        "steps": {},
        "media": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p1.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p2.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p3.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p4.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p5.gif?raw=true",
        "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel.gif?raw=true"]
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
