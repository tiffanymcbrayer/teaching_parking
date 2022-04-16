NUM_QUESTIONS = 5
CHOICES = ["A", "B", "C"]

$(document).ready(function () {
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
    }
})