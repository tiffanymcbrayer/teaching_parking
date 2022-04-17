var NUM_QUESTIONS = 5
var CHOICES = ["A", "B", "C", "D"]
var dict = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3
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
                
            },
            error: function(request, status, error){
                console.log('Error')
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }

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
    }
})