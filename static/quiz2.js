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
var score = 0;

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

    (function ($) {

        $.fn.randomize = function (childElem) {
            return this.each(function () {
                var $this = $(this);
                var elems = $this.children(childElem);

                elems.sort(function () { return (Math.round(Math.random()) - 0.5); });

                $this.detach(childElem);

                for (var i = 0; i < elems.length; i++)
                    $this.append(elems[i]);

            });
        }
    })(jQuery);

    // $('.stepsdiv').randomize('.namebox');
    $('.detailsdiv').randomize('.dropbox');

    $('.dragbox').hover(function () {
        $(this).css('background-color', 'orange')
        $(this).css('cursor', 'move')
    }, function () {
        $(this).css('background-color', '#007bff')
        $(this).css('cursor', 'default')
    })
    $('.dragbox').draggable({
        revert: 'invalid',
        stack: '.dragbox',
        start: function (event, ui) {
            console.log($(this).data('from'))
            $('.dropbox').css('background-color', 'lightblue')
        },
        stop: function (event, ui) {
            $('.dropbox').css('background-color', 'lightgray')
            $(this).css('background-color', '#007bff')
            $(this).css('cursor', 'default')
        },
    });

    $('.dropbox').droppable({
        tolerance: 'pointer',

        drop: function (event, ui) {
            $(ui.draggable).detach().css({ top: -0, left: -50 }).prependTo(this);
            $(this).data("step", $(ui.draggable).data("step"));
            console.log(this)
            console.log("Data step " + $(this).data("step"));
            console.log("Data order " + $(ui.draggable).data("step"));
        },
        over: function (event, ui) {
            $(this).css('background-color', '#37839c')
        },
        out: function (event, ui) {
            $(this).css('background-color', 'lightblue')
        }
    });

    var submit_answer = function (c) {
        // TODO Finish submit answer
        $.ajax({
            type: 'POST',
            url: '/submit_response2',
            dataType: 'json',
            contentType: 'application/json, charset=utf-8',
            data: JSON.stringify(c),
            success: function (result) {
                console.log(result)
                score = parseInt(result['response']['score'])
            },
            error: function (request, status, error) {
                console.log('Error')
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }

    $(document).on('click', '#showresult', function (e) {
        var allcorrect = true
        var pass = true
        console.log("###############################")
        $('.dropbox').each(function (e) {
            console.log($(this).data("step"))
            if (!$(this).data('step')) {
                pass = false;
            }
        })
        console.log("Page " + ordnum)
        if (pass) {
            if ($('#next').length == 0) {
                $('.buttons').append("<button class='quizButtons' id='next'>Next Question</button>")
                hoverColor($("#next"))
            }
            $('.dropbox').each(function (e) {
                console.log($(this).data('step'))
                console.log($(this).data('order'))
                if ($(this).data("step") == $(this).data("order")) {
                    $(this).css("background-color", "green")
                } else {
                    $(this).css("background-color", "red")
                    allcorrect = false
                }
            })
        } else {
            alert("Please drop ALL the steps to ALL the all orders!")
        }
    });

    $(document).on('click', '#next', function (e) {
        var allcorrect = true
        $('.dropbox').each(function (e) {
            if ($(this).data("step") != $(this).data("order")) {
                allcorrect = false
            }
        })
        if (allcorrect) {
            submit_answer({ 'ans': 1 })
        } else {
            submit_answer({ 'ans': 0 })
        }
        window.location.href = '/quiz/' + (parseInt(ordnum) + 1).toString()
    });

})