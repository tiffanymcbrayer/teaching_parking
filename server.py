import json
import math
import random
from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import Response, request, jsonify
from sympy import re
app = Flask(__name__)

QUIZ_NUM = 5

learning = {

    "0": {
        'ord': 0,
        "name": "Forwards Parking",
        "steps": [["1", "Drive forward until the mirror lines up with the parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p1.gif?raw=true"],
                  ["2", "Turn the wheel to your right and move forward into space",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p2.gif?raw=true"],
                  ["3", "Once you are centered in the spot, straighten the wheel and move up to the line ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p3.gif?raw=true"],
                  ["4", "", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards.gif?raw=true",
        "tips": [["Mirror inline with parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_tip1.png?raw=true"]],
        "numsteps": "4"
    },
    "1": {
        'ord': 1,
        "name": "Reverse Parking",
        "steps": [["1", "Drive forward until the mirror lines up with the parking line (keep close to the space)", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p1.gif?raw=true"],
                  ["2", "Turn the wheel to your left and go forward until you see edge of parking line in left mirror",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p2.gif?raw=true"],
                  ["3", "Straighten the wheel until you align your right mirror with the edge of the car to your right ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p3.gif?raw=true"],
                  ["4", "Turn the wheel to the right and reverse until you are centered in the spot",
                   "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p4.gif?raw=true"],
                  ["5", "Once you are centered in the spot, straighten the wheel and move up to the line ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p5.gif?raw=true"],
                  ["6", "", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse.gif?raw=true",
        "tips": [["Mirror inline with second parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_tip1.png?raw=true"], ["Mirror inline with back bumper", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_tip2.png?raw=true"]],
        "numsteps": "6"
    },
    "2": {
        'ord': 2,
        "name": "Angled Parking",
        "steps": [["1", "Drive forward until the mirror lines up with the parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p1.gif?raw=true"],
                  ["2", "Turn the wheel to your right and go forward into space",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p2.gif?raw=true"],
                  ["3", "Once you are centered in the spot, straighten the wheel and move up to the line ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p3.gif?raw=true"],
                  ["4", "", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled.gif?raw=true",
        "tips": [["Mirror inline with parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_tip1.png?raw=true"]],
        "numsteps": "4"
    },
    "3": {
        'ord': 3,
        "name": "Parallel Parking",
        "steps": [["1", "Drive forward until your car is in line with the car next to you (keep a reasonably close distance to the car)", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p1.gif?raw=true"],
                  ["2", "Turn the wheel all the way to your right and reverse until you can see the back corner through the mirror ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p2.gif?raw=true"],
                  ["3", "Straighten out the wheel and back in until you align your right mirror with the left bumper of the car in front",
                   "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p3.gif?raw=true"],
                  ["4", "Turn the wheel left and back up until you have no more space",
                   "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p4.gif?raw=true"],
                  ["5", "Once you are centered in the spot, straighten the wheel and move up until you are in the middle of the spot",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p5.gif?raw=true"],
                  ["6", "", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel.gif?raw=true",
        "tips": [["Mirror inline with back corner", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_tip1.png?raw=true"], ["Mirror inline with back bumper", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_tip2.png?raw=true"]],
        "numsteps": "6"
    }
}

questions = {
    "1": {
        "type": "mc",
        "goal": "Park forwards",
        "question": "In the first step, how should driver align the car?",
        "question-img": "",
        "choice-num": 3,
        "choice-text": ["", "", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_a.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_b.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q1_c.png?raw=true"],
        "answer": 0,
        "answer-img": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/quizPics/q1_asw.gif?raw=true"
    },
    "2": {
        "type": "mc",
        "goal": "Park backwards",
        "question": "In the second step before turn the wheel left and move forward, how should the driver align the car?",
        "question-img": "",
        "choice-num": 4,
        "choice-text": ["", "", "", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_a.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_b.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_c.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q2_d.png?raw=true"],
        "answer": 2,
        "answer-img": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/quizPics/q2_anw.gif?raw=true"
    },
    "3": {
        "type": "mc",
        "goal": "Park angled forwards",
        "question": "In the first step of angled parking, which alignment is correct?",
        "question-img": "",
        "choice-num": 2,
        "choice-text": ["", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q3_a.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q3_b.png?raw=true"],
        "answer": 0,
        "answer-img": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/quizPics/q3_asw.gif?raw=true"
    },
    "4": {
        "type": "mc",
        "goal": "Parallel park",
        "question": "In the first step of parallel parking, how do I position the car before I turn my wheel right to reverse into the spot?",
        "question-img": "",
        "choice-num": 3,
        "choice-text": ["", "", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q4_a.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q4_b.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q4_c.png?raw=true"],
        "answer": 0,
        "answer-img": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/quizPics/q4_asw.gif?raw=true"
    },
    "5": {
        "type": "mc",
        "goal": "Parallel park",
        "question": "In the second step, which position should I align before backing straight?",
        "question-img": "",
        "choice-num": 3,
        "choice-text": ["", "", ""],
        "choice-img": ["https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q5_a.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q5_b.png?raw=true",
                       "https://github.com/tiffanymcbrayer/teaching_parking/blob/Tiffany/img/quizPics/q5_c.png?raw=true"],
        "answer": 0,
        "answer-img": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/quizPics/q5_asw.gif?raw=true"
    },
    "6": {
        'ord': 6,
        "type": "order",
        "name": "Forwards Parking",
        "steps": [["1", "Drive forward until the mirror lines up with the parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p1.gif?raw=true"],
                  ["2", "Turn the wheel to your right and move forward into space",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p2.gif?raw=true"],
                  ["3", "Once you are centered in the spot, straighten the wheel and move up to the line ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_p3.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards.gif?raw=true",
        "tips": [["Mirror inline with parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/forwards_tip1.png?raw=true"]],
        "numsteps": "4"
    },
    "7": {
        'ord': 7,
        "type": "order",
        "name": "Reverse Parking",
        "steps": [["1", "Drive forward until the mirror lines up with the parking line (keep close to the space)", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p1.gif?raw=true"],
                  ["2", "Turn the wheel to your left and go forward until you see edge of parking line in left mirror",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p2.gif?raw=true"],
                  ["3", "Straighten the wheel until you align your right mirror with the edge of the car to your right ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p3.gif?raw=true"],
                  ["4", "Turn the wheel to the right and reverse until you are centered in the spot",
                   "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p4.gif?raw=true"],
                  ["5", "Once you are centered in the spot, straighten the wheel and move up to the line ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_p5.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse.gif?raw=true",
        "tips": [["Mirror inline with second parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_tip1.png?raw=true"], ["Mirror inline with back bumper", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/reverse_tip2.png?raw=true"]],
        "numsteps": "6"
    },
    "8": {
        'ord': 8,
        "type": "order",
        "name": "Angled Parking",
        "steps": [["1", "Drive forward until the mirror lines up with the parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p1.gif?raw=true"],
                  ["2", "Turn the wheel to your right and go forward into space",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p2.gif?raw=true"],
                  ["3", "Once you are centered in the spot, straighten the wheel and move up to the line ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_p3.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled.gif?raw=true",
        "tips": [["Mirror inline with parking line", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/angled_tip1.png?raw=true"]],
        "numsteps": "4"
    },
    "9": {
        'ord': 9,
        "type": "order",
        "name": "Parallel Parking",
        "steps": [["1", "Drive forward until your car is in line with the car next to you (keep a reasonably close distance to the car)", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p1.gif?raw=true"],
                  ["2", "Turn the wheel all the way to your right and reverse until you can see the back corner through the mirror ",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p2.gif?raw=true"],
                  ["3", "Straighten out the wheel and back in until you align your right mirror with the left bumper of the car in front",
                   "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p3.gif?raw=true"],
                  ["4", "Turn the wheel left and back up until you have no more space",
                   "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p4.gif?raw=true"],
                  ["5", "Once you are centered in the spot, straighten the wheel and move up until you are in the middle of the spot",
                      "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_p5.gif?raw=true"]],
        "fullGif": "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel.gif?raw=true",
        "tips": [["Mirror inline with back corner", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_tip1.png?raw=true"], ["Mirror inline with back bumper", "https://github.com/tiffanymcbrayer/teaching_parking/blob/main/img/learnGifs/parallel_tip2.png?raw=true"]],
        "numsteps": "6"
    }
}

response = {
    "num": 0,
    "q_num": [],
    "ans": [],
    "score": 0
}

response2 = {
    "num": 0,
    "q_num": [],
    "ans": [],
    "score": 0
}


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/learn/<type>/<stepnum>')
def learn(type=None, stepnum=None):
    global learning
    parkingType = learning[type]
    if int(type)-1 >= 0:
        prevType = learning[str(int(type)-1)]
    else:
        prevType = None

    indexStep = int(stepnum)-1
    step = parkingType['steps'][indexStep]
    lastStep = len(parkingType['steps'])
    lastStep = str(lastStep)

    return render_template('learn.html', parkingType=parkingType, step=step, lastStep=lastStep, prevType=prevType)


@app.route('/quiz/<q_num>')
def quiz(q_num=None):
    global learning
    global questions
    global response
    global QUIZ_NUM

    if(response["num"] == 0 and q_num.lower() != "start".lower()):
        response = {
            "num": 0,
            "q_num": [],
            "ans": [],
            "score": 0
        }
        return render_template('quiz.html', end=0, total_num=QUIZ_NUM, response=response, q_num=None, question=None)
    elif(q_num.lower() == "start".lower()):
        if(response["num"] == 0):
            response["num"] = 1
            response["q_num"] = random.sample(
                range(1, len(questions.keys())+1), QUIZ_NUM)
            return redirect('/quiz/'+str(response["num"]))
        else:
            return redirect('/quiz/'+str(response["num"]))
    elif(str(response["num"]) != q_num):
        return redirect('/quiz/'+str(response["num"]))
    elif(response["num"] > QUIZ_NUM):
        tmp = response
        response = {
            "num": 0,
            "q_num": [],
            "ans": [],
            "score": 0
        }
        return render_template("quiz.html", end=1, total_num=QUIZ_NUM, q_num=None, response=tmp, question=None)
    else:
        q = str(response["q_num"][int(q_num)-1])
        if questions[q]["type"] == "mc":
            question = {
                "num": str(q_num),
                "type": questions[q]["type"],
                "goal": questions[q]["goal"],
                "question": questions[q]["question"],
                "choice-num": questions[q]["choice-num"],
                "choice-text": questions[q]["choice-text"],
                "choice-img": questions[q]["choice-img"]
            }
            return render_template('quiz.html', end=0, total_num=QUIZ_NUM, q_num=q_num, response=response, question=question)
        elif questions[q]["type"] == "order":
            parkingType = questions[str(questions[q]["ord"])]
            return render_template('quiz2.html', parkingType=parkingType, total_num=QUIZ_NUM, q_num=q_num)


'''@app.route('/quiz2/<q_num>')
def quiz2(q_num=None):
    # global questions2
    global learning
    # if q_num == '4':
    #     parkingType = learning['3']
    #     return render_template('quiz2.html', parkingType=parkingType)
    # else:
    parkingType = learning[q_num]
    return render_template('quiz2.html', parkingType=parkingType)
'''
### AJAX CALLS ###


@app.route('/submit_response', methods=['GET', 'POST'])
def submit_response():
    global questions
    global response
    json_data = request.get_json()
    correct_ans = questions[str(
        response["q_num"][int(json_data['q_num'])-1])]["answer"]
    correct_img = questions[str(
        response["q_num"][int(json_data['q_num'])-1])]["answer-img"]
    response["num"] += 1
    response["ans"].append(int(json_data['choice']))
    correct = correct_ans == int(json_data['choice'])
    if(correct):
        response["score"] += 1
    return jsonify(response=response, correct=correct, correct_ans=correct_ans, correct_img=correct_img)


@app.route('/submit_response2', methods=['GET', 'POST'])
def submit_response2():
    global response
    json_data = request.get_json()
    print(json_data)
    score = int(json_data['ans'])
    response["num"] += 1
    response["score"] += score
    # TODO: Add response2 updating
    return jsonify(response=response2)


if __name__ == '__main__':
    app.run(debug=True)
