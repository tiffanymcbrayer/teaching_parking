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
        button.css('background-color', '#ffd500'); //how to change back after?
    });
    button.mouseout(function(){
        button.css('background-color', '#ffeb8a'); //how to change back after?
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
                $('#'+dict[result["correct_ans"]]+"-img").empty()
                $('#answer').append("<span class='stepNameQuiz'>Correct answer is " + dict[result["correct_ans"]] + "</span>")
                $('#'+dict[result["correct_ans"]]+"-img").append("<img class='correctChoice img-fluid' src='" + result["correct_img"] + "'>")
                $('#'+dict[result["correct_ans"]]).css("border", "5px dashed green")
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
        $('#goal').append("<div class='col-md-6'></div><div class='col-md-4'> <span class='stepNameQuiz'>Score: " + response["score"] + "/" + QUIZ_NUM + "</span> </div>")
        $('#question').append("<div class='col-md-5'></div><button class = 'quizButtons' id='restart'>Try Again</button>")
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
            $('#goal').append("<div class='col-md-5'></div><div class='col-md-5'> <span class='stepNameQuiz'>Test your knowledge!</span> </div>")
            $('#question').append("<div class='col-md-6'></div> <button class = 'mcButtons centeralign' id='start'>Start</button>")
            hoverColor($("#start"))

            $('#start').click(function () {
                window.location.href = '/quiz/start'
            })
        } else {
            $('#selectionTitle').text("Select an Answer Choice:")
            $('#goal').append("<span class='stepNameQuiz'>" + question['goal'] + "</span>")
            $('#question').append("<span class='stepNameQuiz'>" + question['question'] + "</span>")
            $.each(question['choice-img'], function (index, value) {
                let choice = CHOICES[index]
                $('#' + choice + "-img").append("<img class='img-fluid' src='" + this + "'></img>")
                $('#' + choice + "-text").text(question['choice-text'][index])
                $('#' + choice + "-button").append("<button class='mcButtons' id='" + choice + "'>" + choice + "</button>")
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

            hoverColor($('#A'))
            hoverColor($('#B'))
            hoverColor($('#C'))
            hoverColor($('#D'))
        }
    }
})