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
    // let ordnumi = int(ordnum)
    if (ordnum == 0) {
        $('.prev').append("<button class = 'learnButtons' id='home'>Home</button>")
        $(document).on('click', '#home', function (e) {
            window.location.href = '/'
        }); 
        hoverColor($("#home"))

    } else {
        $('.prev').append("<button class = 'learnButtons' id='prevtutorial'>Previous</button>")
        $(document).on('click', '#prevtutorial', function (e) {
            var nextnum = parseInt(ordnum) - 1
            window.location.href = '/learn/' + nextnum
        });
        hoverColor($("#prevtutorial"))
    }


    if (ordnum == 3) {
        $('.next').append("<button class = 'learnButtons' id='quiz'>Start Quiz</button>")
        $(document).on('click', '#quiz', function (e) {
            window.location.href = '/quiz/0'
        });
        hoverColor($("#quiz"))
    } else {
        $('.next').append("<button class = 'learnButtons' id='nexttutorial'>Next</button>")
        $(document).on('click', '#nexttutorial', function (e) {
            var nextnum = parseInt(ordnum) + 1
            window.location.href = '/learn/' + nextnum
        });
        hoverColor($("#nexttutorial"))
    }
})