import math
import random
from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__)

QUIZ_NUM = 5

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

questions = {
    "1": {
        "goal": "Park Forwards",
        "question": "When should I start turning right?",
        "question-img" : "", 
        "choice-num": 3, 
        "choice-text": ["","", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/a9fed650dad8270a810f5d54597581729caa761a/img/quizPics/q1_a.png?raw=true",
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_b.png?raw=true", 
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_c.png?raw=true"],
        "answer": 2
    },
    "2": {
        "goal": "Park Forwards",
        "question": "When should I start turning right?",
        "question-img" : "", 
        "choice-num": 3, 
        "choice-text": ["","", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/a9fed650dad8270a810f5d54597581729caa761a/img/quizPics/q1_a.png?raw=true",
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_b.png?raw=true", 
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_c.png?raw=true"],
        "answer": 2
    },
    "3": {
        "goal": "Park Forwards",
        "question": "When should I start turning right?",
        "question-img" : "", 
        "choice-num": 3, 
        "choice-text": ["","",""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/a9fed650dad8270a810f5d54597581729caa761a/img/quizPics/q1_a.png?raw=true",
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_b.png?raw=true", 
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_c.png?raw=true"],
        "answer": 2
    },
    "4": {
        "goal": "Park Forwards",
        "question": "When should I start turning right?",
        "question-img" : "", 
        "choice-num": 3, 
        "choice-text": ["","", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/a9fed650dad8270a810f5d54597581729caa761a/img/quizPics/q1_a.png?raw=true",
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_b.png?raw=true", 
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_c.png?raw=true"],
        "answer": 2
    },
    "5": {
        "goal": "Park Forwards",
        "question": "When should I start turning right?",
        "question-img" : "", 
        "choice-num": 3, 
        "choice-text": ["","", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/a9fed650dad8270a810f5d54597581729caa761a/img/quizPics/q1_a.png?raw=true",
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_b.png?raw=true", 
                       "https://raw.githubusercontent.com/tiffanymcbrayer/teaching_parking/f2eeacb767fdf9ddcc114bfaf388ecbdf09be9bc/img/quizPics/q1_c.png?raw=true"],
        "answer": 2
    }
}

response = {
    "num": 0,
    "q_num": [],
    "ans": []
}

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/learn/<type>')
def learn(type = None):
    global learning
    parkingType = learning[type]
    return render_template('learn.html', parkingType = parkingType)

@app.route('/quiz/<q_num>')
def quiz(q_num = None):
    global questions
    global response

    if(response["num"] == 0 and q_num.lower() != "start".lower()):
        response = {
            "num": 0,
            "q_num": [],
            "ans": []
        }
        return render_template('quiz.html', response = response, q_num=None, question=None)
    elif(q_num.lower() == "start".lower()):
        response["num"] = 1
        response["q_num"] = random.sample(range(1, len(questions.keys())+1), QUIZ_NUM)
        return redirect('/quiz/'+str(response["num"]))
    elif(str(response["num"]) != q_num):
        return redirect('/quiz/'+str(response["num"]))
    else:
        q = response["q_num"][int(q_num)-1]
        question = {
            "num": str(q_num),
            "goal": questions[str(q)]["goal"],
            "question": questions[str(q)]["question"],
            "choice-num": questions[str(q)]["choice-num"],
            "choice-text": questions[str(q)]["choice-text"],
            "choice-img": questions[str(q)]["choice-img"]
        }
        return render_template('quiz.html', q_num = q_num, response = response, question=question)

### AJAX CALLS ###
@app.route('/submit_response', methods=['GET', 'POST'])
def submit_response():
    global questions
    global response
    json_data = request.get_json()
    # TODO: Add response updating
    pass

if __name__ == '__main__':
    app.run(debug = True)
