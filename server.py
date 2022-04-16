from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__)

learning = {
    
    "forward": {
        "name": "Forwards Parking",
        "steps": [[1,"Drive forward until the mirror lines up with the parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p1.gif?raw=true"],
                [2,"Turn the wheel to your right and move forward into space", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p2.gif?raw=true"], 
                [3,"Once you are centered in the spot, straighten the wheel and move up to the line ", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p3.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards.gif?raw=true"       
    },
    "reverse": {
        "name": "Reverse Parking",
        "steps": [[1, "Drive forward until the mirror lines up with the parking line (keep close to the space)", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p1.gif?raw=true"],
                [2, "Turn the wheel to your left and go forward until you see edge of parking line in left mirror", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p2.gif?raw=true"],
                [3, "Straighten the wheel until you align your right mirror with the edge of the car to your right ", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p3.gif?raw=true"], 
                [4, "Turn the wheel to the right and reverse until you are centered in the spot", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p4.gif?raw=true"],
                [5, "Once you are centered in the spot, straighten the wheel and move up to the line ", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p5.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse.gif?raw=true"
    },
    "angled": {
        "name": "Angled Parking",
        "steps": [[1, "Drive forward until the mirror lines up with the parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p1.gif?raw=true"],
                 [2, "Turn the wheel to your left and go forward into space", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p2.gif?raw=true"],
                 [3, "Once you are centered in the spot, straighten the wheel and move up to the line ", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p3.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled.gif?raw=true"
    },
    "parallel": {
        "name": "Parallel Parking",
        "steps": [[1,"Drive forward until your car is in line with the car next to you (keep a reasonably close distance to the car)", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p1.gif?raw=true"],
                [2, "Turn the wheel all the way to your right and reverse until you can see the back corner through the mirror ", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p2.gif?raw=true"],
                [3, "Straighten out the wheel and back in until you align your right mirror with the left bumper of the car in front", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p3.gif?raw=true"],
                [4, "Turn the wheel left and back up until you have no more space", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p4.gif?raw=true"],
                [5, "Once you are centered in the spot, straighten the wheel and move up until you are in the middle of the spot", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p5.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel.gif?raw=true"
    }
}

quiz = {1: {"goal": "park forwards",
            "question": "When should I start turning right?",
            "quizQs": [["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_a.png?raw=true"],
                        ["B", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_b.png?raw=true"],
                        ["C", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_c.png?raw=true"]],
            "correctAns": ["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_asw.gif?raw=true"]
        },
        2: {"goal": "park backwards",
            "question": "How should I position the car if the next step is to turn the wheel left and move forward?",
            "quizQs": [["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_a.png?raw=true"],
                        ["B", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_b.png?raw=true"],
                        ["C", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_c.png?raw=true"],
                        ["D", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_d.png?raw=true"]],
            "correctAns": ["B", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_asw.gif?raw=true"]
        },
        3: {"goal": "park angled forwards",
            "question": "Am I in a good position to turn left and move forwards?",
            "quizQs": [["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q3_a.png?raw=true"],
                        ["B", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q3_b.png?raw=true"]],
            "correctAns": ["B", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q3_asw.gif?raw=true"]
        },
        4: {"goal": "parallel park",
            "question": "How do I position the car before I turn my wheel right to reverse into the spot?",
            "quizQs": [["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_a.png?raw=true"],
                        ["B", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_b.png?raw=true"],
                        ["C", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_c.png?raw=true"]],
            "correctAns": ["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_asw.gif?raw=true"]
        },
        5: {"goal": "parallel park",
            "question": "How do I position the car before I reverse straight into the spot?",
            "quizQs": [["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q5_a.png?raw=true"],
                        ["B", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q5_b.png?raw=true"],
                        ["C", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q5_c.png?raw=true"],],
            "correctAns": ["A", "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q5_asw.gif?raw=true"]
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
