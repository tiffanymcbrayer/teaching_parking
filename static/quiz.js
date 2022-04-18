var CHOICES = ["A", "B", "C", "D"]
var dict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    0: "A",
    1: "B",
    2: "C",
    3: "D"
};


function hoverColor(button){
    $(button).mouseover(function(){
        button.css('background-color', '#77b5fe'); //how to change back after?
    });
    button.mouseout(function(){
        button.css('background-color', '#007bff'); //how to change back after?
    });
}

$(document).ready(function () {
    var submit_answer = function (c) {
        // TODO Finish submit answer
        $.ajax({
            type: 'POST',
            url: '/submit_response',
            dataType: 'json',
            contentType: 'application/json, charset=utf-8',
            data: JSON.stringify(c),
            success: function (result) {
                $('#A,#B,#C,#D').prop("disabled", true);
                if (result["correct"]) {
                    $('#' + dict[c["choice"]]).css("background-color", "green")
                } else {
                    $('#' + dict[c["choice"]]).css("background-color", "red")
                }

                $('#answer').append("<span class='stepName'>Correct answer is " + dict[result["correct_ans"]] + "</span>")
                $('#answer-img').append("<img src='" + result["correct_img"] + "' class='img-fluid'>")
                if((parseInt(q_num) + 1).toString()==6){
                   $('#next-button').append("<button class = 'quizButtons' id='next'>See Results</button>") 
                }
                else{
                    $('#next-button').append("<button class = 'quizButtons' id='next'>Next Question</button>")
                }
                hoverColor($("#next"))
            },
            error: function (request, status, error) {
                console.log('Error')
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }
    if (end_quiz == 1) {
        $('#goal').empty()
        $('#goal').append("<span class='stepName'>Score: " + response["score"] + "/" + QUIZ_NUM + "</span>")
        $('#question').append("<button class = 'quizButtons' id='restart'>Try Again</button>")
        hoverColor($("#restart"))
        $(document).on('click', '#restart', function (e) {
            window.location.href = '/quiz/0'
        });

        $('#question').append("<button class ='quizButtons' id='gohome'>Home</button>")
        $(document).on('click', '#gohome', function (e) {
            window.location.href = '/'
        });
        hoverColor($("#gohome"))

    } else {
        if (!question) {
            $('#goal').empty()
            $('#goal').append("<span class='stepName'>Test your knowledge!</span>")
            $('#question').append('<button class = "quizButtons" id="start">Start</button>')
            hoverColor($("#start"))

            $('#start').click(function () {
                window.location.href = '/quiz/start'
            })
        } else {
            $('#goal').append("<span class='ml-5 stepName'>" + question['goal'] + "</span>")
            $('#question').append("<span class='stepName'>" + question['question'] + "</span>")
            $.each(question['choice-img'], function (index, value) {
                let choice = CHOICES[index]
                $('#' + choice + "-img").append("<img class='img-fluid' src='" + this + "'></img>")
                $('#' + choice + "-text").text(question['choice-text'][index])
                $('#' + choice + "-button").append("<button id='" + choice + "'>" + choice + "</button>")
            })

            $(document).on('click', '#A,#B,#C,#D', function (e) {
                let choice = dict[e.target.id];
                let json_choice = {
                    'q_num': q_num,
                    'choice': choice
                }
                submit_answer(json_choice)
            });

            $(document).on('click', '#next', function (e) {
                window.location.href = '/quiz/' + (parseInt(q_num) + 1).toString()
            });
        }
    }
})