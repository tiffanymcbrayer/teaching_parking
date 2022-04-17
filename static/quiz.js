NUM_QUESTIONS = 5
CHOICES = ["A", "B", "C"]

$(document).ready(function () {
    var submit_answer = function(choice){
        // TODO Finish submit answer
        $.ajax({
            type: 'POST',
            url: 'submit_response',
            dataType: 'json',
            contentType: 'application/json, charset=utf-8',
            data : JSON.stringify(restaurant),
            success: function(result){
                $('#submit_success').empty() 
                let valid_text = '<div class="col-md-6">New item successfully created</div>'
                let link_text = '<div class="col-md-6">See it <a class="black" href="/view/'+result['id']+'">here</a></div>'
                $('#submit_success').append(valid_text)
                $('#submit_success').append(link_text)
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
            $('#'+choice+"-button").append("<button class='' id='"+choice+"'>"+choice+"</button>")
        })

        $('#A', '#B', '#C').click(function(){
            //TODO: Run the ajax function and go to next question/answer
        })
    }
})