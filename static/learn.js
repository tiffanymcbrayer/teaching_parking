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

$(document).ready(function () {
    // let ordnumi = int(ordnum)
    if (ordnum == 0) {
        $('.prev').append("<button id='home'>Home</button>")
        $(document).on('click', '#home', function (e) {
            window.location.href = '/'
        });
    } else {
        $('.prev').append("<button id='prevtutorial'>Previous</button>")
        $(document).on('click', '#prevtutorial', function (e) {
            var nextnum = parseInt(ordnum) - 1
            window.location.href = '/learn/' + nextnum
        });
    }


    if (ordnum == 3) {
        $('.next').append("<button id='quiz'>Start Quiz</button>")
        $(document).on('click', '#quiz', function (e) {
            window.location.href = '/quiz/0'
        });
    } else {
        $('.next').append("<button id='nexttutorial'>Next</button>")
        $(document).on('click', '#nexttutorial', function (e) {
            var nextnum = parseInt(ordnum) + 1
            window.location.href = '/learn/' + nextnum
        });
    }
})