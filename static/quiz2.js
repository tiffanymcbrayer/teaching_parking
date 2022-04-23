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

var steps = [
    "Phyllis",
    "Angela",
    "Dwight",
    "Oscar",
    "Creed",
    "Pam",
    "Jim",
    "Stanley",
    "Michael",
    "Kevin",
    "Kelly"
]

var orders = []

function hoverColor(button) {
    $(button).mouseover(function () {
        button.css('background-color', '#77b5fe'); //how to change back after?
    });
    button.mouseout(function () {
        button.css('background-color', '#007bff'); //how to change back after?
    });
}

$(document).ready(function () {

    function generateNames() {
        $(".names").empty()
        let list = stepnames
        if (ordernames.length > stepnames.length) {
            list = ordernames
        }


        $.each(list, function (idx, val) {
            let lname = ''
            let rname = ''
            if (idx < stepnames.length) {
                lname = '<div class="namebox col-2" data-from="stepname" id="' + idx + '">' + stepnames[idx] + '</div>'
            }
            if (idx < ordernames.length) {
                rname = '<div class="namebox col-2" data-from="ordername" id="' + idx + '">' + ordernames[idx] + '</div>'
            }
            let row = '<div class="row"> ' + lname + rname + '</div >'
            $(".names").append(row)
            $('.namebox').hover(function () {
                $(this).css('background-color', 'lightyellow')
                $(this).css('cursor', 'move')
            }, function () {
                $(this).css('background-color', 'white')
                $(this).css('cursor', 'default')
            })
            $('.namebox').draggable({
                revert: 'invalid',
                stack: '.namebox',
                start: function (event, ui) {
                    console.log($(this).data('from'))
                    if ($(this).data('from') == 'stepname') {
                        $('.droporder').css('background-color', '#37839c')
                    } else {
                        $('.dropstep').css('background-color', '#37839c')
                    }
                },
                stop: function (event, ui) {
                    if ($(this).data('from') == 'stepname') {
                        $('.droporder').css('background-color', 'lightblue')
                        $('.dropstep').css('background-color', 'lightblue')
                    } else {
                        $('.droporder').css('background-color', 'lightblue')
                        $('.dropstep').css('background-color', 'lightblue')
                    }
                }
            });
        })
    }
    generateNames()


    $('.droporder').droppable({
        tolerance: 'pointer',
        accept: function (d) {
            if (d.data('from') == "stepname") {
                return true
            }
        },
        drop: function (event, ui) {
            // console.log($(ui.draggable).attr('id'));
            let nid = $(ui.draggable).attr('id')
            let from = $(ui.draggable).data('from')
            let fromname = stepnames
            // if (from == "ordername") {
            //     fromname = ordernames
            // }
            let name = fromname.splice(nid, 1)
            ordernames.push(name)
            generateNames()
        },
        over: function (event, ui) {
            $(this).css('background-color', '#114a5e')
        },
        out: function (event, ui) {
            $(this).css('background-color', '#37839c')
        }
    });
    $('.dropstep').droppable({
        tolerance: 'pointer',
        accept: function (d) {
            if (d.data('from') == "ordername") {
                return true
            }
        },
        drop: function (event, ui) {
            // console.log($(ui.draggable).attr('id'));
            let nid = $(ui.draggable).attr('id')
            let from = $(ui.draggable).data('from')
            let fromname = ordernames
            // if (from == "stepname") {
            //     fromname = stepnames
            // }
            let name = fromname.splice(nid, 1)
            stepnames.push(name)
            generateNames()
        },
        over: function (event, ui) {
            $(this).css('background-color', '#114a5e')
        },
        out: function (event, ui) {
            $(this).css('background-color', '#37839c')
        }
    });


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
                if ((parseInt(q_num) + 1).toString() == 6) {
                    $('#next-button').append("<button class = 'quizButtons' id='next'>See Results</button>")
                }
                else {
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
})