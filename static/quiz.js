var CHOICES = ["A", "B", "C", "D"]
var dict = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    0: "A",
    1: "B",
    2: "C",
    3: "D"
};

$(document).ready(function () {
    var submit_answer = function(c){
        // TODO Finish submit answer
        $.ajax({
            type: 'POST',
            url: '/submit_response',
            dataType: 'json',
            contentType: 'application/json, charset=utf-8',
            data : JSON.stringify(c),
            success: function(result){
                $('#A,#B,#C,#D').prop("disabled",true);
                if (result["correct"]) {
                    $('#'+dict[c["choice"]]).css("background-color", "green")
                } else{
                    $('#'+dict[c["choice"]]).css("background-color", "red")
                }

                $('#answer').text("Correct answer is "+dict[result["correct_ans"]])
                $('#answer-img').append("<img src='"+result["correct_img"]+"' class='img-fluid'>")
                $('#next-button').append("<button id='next'>Next Question</button>")
            },
            error: function(request, status, error){
                console.log('Error')
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }
    if(end_quiz == 1){
        $('#goal').text("Score: "+response["score"]+"/"+QUIZ_NUM)
        $('#question').append("<button id='restart'>Try Again</button>")
        $(document).on('click', '#restart', function(e){
            window.location.href = '/quiz/0'
        });
    } else{
        if(!question){
            $('#goal').empty()
            $('#goal').text("Test your knowledge!")
            $('#question').append('<button id="start">Start</button>')

            $('#start').click(function(){
                window.location.href = '/quiz/start'
            })
        } else{
            $('#goal').append("<span class='ml-5'>"+question['goal']+"</span>")
            $('#question').append("<span>"+question['question']+"</span>")
            $.each(question['choice-img'], function(index, value){
                let choice = CHOICES[index]
                $('#'+choice+"-img").append("<img class='img-fluid' src='"+this+"'></img>")
                $('#'+choice+"-text").text(question['choice-text'][index])
                $('#'+choice+"-button").append("<button id='"+choice+"'>"+choice+"</button>")
            })

            $(document).on('click', '#A,#B,#C,#D', function(e){
                let choice = dict[e.target.id];
                let json_choice = {
                    'q_num': q_num,
                    'choice': choice
                }
                submit_answer(json_choice)
            });

            $(document).on('click', '#next', function(e){
                window.location.href = '/quiz/'+(parseInt(q_num)+1).toString()
            });
        }
    }
})