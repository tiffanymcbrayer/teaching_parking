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

function hoverColor(button){
    $(button).mouseover(function(){
        button.css('background-color', '#2FBEFD'); //how to change back after?
        button.css('border-color', '#ffeb8a');
        button.css('color', '#ffeb8a');
    });
    button.mouseout(function(){
        button.css('background-color', '#ffeb8a'); //how to change back after?
        button.css('border-color', '#2FBEFD');
        button.css('color', '#2FBEFD');
    });
}

function hoverColor2(button){
    $(button).mouseover(function(){
        button.css('background-color', '#C0C0C0'); //how to change back after?
        button.css('border-color', 'black');
        button.css('color', 'black');
        button.css('cursor', 'not-allowed');
    });
    button.mouseout(function(){
        button.css('background-color', '#C0C0C0');//how to change back after?
        button.css('border-color', 'black');
        button.css('color', 'black');
        button.css('cursor', 'default');
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
    hoverColor($("#showresult"))
    // $('.stepsdiv').randomize('.namebox');
    $('.detailsdiv').randomize('.dropbox');

    $('.dragbox').hover(function () {
        $(this).css('background-color', '#ffd500')
        $(this).css('color', '#2FBEFD')
        $(this).css('cursor', 'move')
    }, function () {
        $(this).css('background-color', '#ffeb8a')
        $(this).css('color', '#2FBEFD')
        $(this).css('cursor', 'default')
    })
    $('.dragbox').draggable({
        revert: 'invalid',
        stack: '.dragbox',
        start: function (event, ui) {
            console.log($(this).data('from'))
            $('.dropbox').css('background-color', '#FFEB8A')
            $(this).css('color', '#2FBEFD')
            $(this).css('background-color', '#ffeb8a')
        },
        stop: function (event, ui) {
            $('.dropbox').css('background-color', 'darkgray')
            $(this).css('background-color', '#ffeb8a')
            $(this).css('color', '#2FBEFD')
            $(this).css('cursor', 'default')
        },
    });

    $('.dropbox').droppable({
        tolerance: 'pointer',

        drop: function (event, ui) {
            $(ui.draggable).detach().css({ top: -0, left: -0 }).prependTo(this);
            // if ($(this).children('.dragbox').length == 1) {
            //     $(this).data("step", $(ui.draggable).data("step"));
            // }
            // console.log(this)
            // console.log("Data step " + $(this).data("step"));
            // console.log("Data order " + $(ui.draggable).data("step"));
            // $(this).css('background-color', '#FFEB8A')
        },
        over: function (event, ui) {
            $(this).css('background-color', '#ffd500')
        },
        out: function (event, ui) {
            $(this).css('background-color', '#FFEB8A')
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
                //console.log(result)
                //score = parseInt(result['response']['score'])
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
            if ($(this).children('.dragbox').length == 0) {
                pass = false;
            }
        })
        console.log("Page " + ordnum)
        if (pass) {
            hoverColor2($("#showresult"))
            if ($('#next').length == 0) {
                $('.buttons').append("<button class='quizButtons' id='next'>Next Question</button>")
                hoverColor($("#next"))
            }
            $('.dropbox').each(function (e) {
                // console.log($(this).data('step'))
                console.log($(this).data('order'))
                console.log($(this).children('.dragbox').data('step'))
                if ($(this).children('.dragbox').data('step') == $(this).data("order")) {
                    $(this).css("background-color", "green")
                } else {
                    $(this).css("background-color", "red")
                    allcorrect = false
                }
            })
            if (allcorrect) {
                console.log("All correct")
            } else {
                console.log("Incorrect")
            }
        } else {
            alert("Please drop ALL the steps to ALL the all orders!")
        }
    });

    $(document).on('click', '#next', function (e) {
        var allcorrect = true
        $('.dropbox').each(function (e) {
            if ($(this).children('.dragbox').data('step') != $(this).data("order")) {
                allcorrect = false
            }
        })
        if (allcorrect) {
            submit_answer({ 'ans': 1 })
        } else {
            submit_answer({ 'ans': 0 })
        }
        window.location.href = '/quiz/' + (parseInt(q_num) + 1).toString()
    });

    $(".fullGif").css("height", $(".hintgif").height() + ' !important');
    console.log($(".hintgif").height());
})