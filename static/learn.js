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
        button.css('border-style', 'dashed');
    });
    button.mouseout(function(){
        button.css('background-color', '#007bff'); //how to change back after?
        button.css('border-style', 'solid');
    });
}


$(document).ready(function () {

    new Freezeframe('.freezeframe', {
    trigger: 'click',   
    overlay: true
    });

    // let ordnumi = int(ordnum)
    //if it is the first step in first lesson
    if (ordnum == 0 && currstep ==1) {
        $('.prev').append("<button class = 'prevButtons' id='home'>Home</button>")
        $(document).on('click', '#home', function (e) {
            window.location.href = '/'
        }); 
        hoverColor($("#home"))

    } 

    else if(currstep ==1){
        //if it is the first step but not the first lesson
        let nextnum = parseInt(ordnum) - 1
        $('.prev').append("<button class = 'prevButtons' id='prevtutorial'>Summary: "+prevName+"</button>")
        $(document).on('click', '#prevtutorial', function (e) {
            var nextnum = parseInt(ordnum) - 1
            window.location.href = '/learn/' + nextnum+'/'+prevLessonSteps
        });
        hoverColor($("#prevtutorial"))        
    }   

    else {
        $('.prev').append("<button class = 'prevButtons' id='prevtutorial'>Previous Step</button>")
        $(document).on('click', '#prevtutorial', function (e) {
            var nextnum = parseInt(currstep) - 1
            window.location.href = '/learn/' + ordnum+'/'+nextnum
        });
        hoverColor($("#prevtutorial"))
    }



    if (ordnum == 3 && currstep ==laststep) {
        //if it is the last step in the last lesson
        $('.next').append("<button class = 'nextButtons' id='quiz'>Start Quiz</button>")
        $(document).on('click', '#quiz', function (e) {
            window.location.href = '/quiz/0'
        });
        hoverColor($("#quiz"))
    } 

    else if (currstep ==laststep) {
        //if it is the last step but there is a next lesson
        $('.next').append("<button class = 'nextButtons' id='nexttutorial'>Next Lesson</button>")
        $(document).on('click', '#nexttutorial', function (e) {
            var nextnum = parseInt(ordnum) + 1
            window.location.href = '/learn/' + nextnum+'/1'
        });
        hoverColor($("#nexttutorial"))
    } 

    else if ((parseInt(currstep)+1) ==laststep){
        //if there is another step in the same lesson
        $('.next').append("<button class = 'nextButtons' id='nexttutorial'>Summary: "+lessonName+ "</button>")
        $(document).on('click', '#nexttutorial', function (e) {
            let nextStep = parseInt(currstep)+1 
            window.location.href = '/learn/'+ordnum+'/'+nextStep
        });
        hoverColor($("#nexttutorial"))
    }    

    else {
        //if there is another step in the same lesson
        $('.next').append("<button class = 'nextButtons' id='nexttutorial'>Next Step</button>")
        $(document).on('click', '#nexttutorial', function (e) {
            let nextStep = parseInt(currstep)+1 
            window.location.href = '/learn/'+ordnum+'/'+nextStep
        });
        hoverColor($("#nexttutorial"))
    }

    if(currstep==laststep){
        let MyDiv1 = $("#tipDivId").html();
        document.getElementById('tipDivId').innerHTML = ""
        $("#tipDivId").append("<button class='tipButtons' id='tipButton'>Show Tips</button>")
        hoverColor($("#tipButton"))
        $('#tipButton').one('click', function(){
            document.getElementById('tipDivId').innerHTML = document.getElementById('tipDivId').innerHTML + MyDiv1
            $('#tipButton').css('background-color', 'grey')
            $('#tipButton').css('cursor', 'default')
        });
    }
})