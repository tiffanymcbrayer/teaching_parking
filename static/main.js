// Dropdown on hover
document.addEventListener("DOMContentLoaded", function () {
    // make it as accordion for smaller screens
    if (window.innerWidth > 992) {

        document.querySelectorAll('.navbar .nav-item').forEach(function (item) {

            item.addEventListener('mouseover', function (e) {

                let el_link = this.querySelector('a[data-bs-toggle]');

                if (el_link != null) {
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.add('show');
                    nextEl.classList.add('show');
                }

            });
            item.addEventListener('mouseleave', function (e) {
                let el_link = this.querySelector('a[data-bs-toggle]');

                if (el_link != null) {
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.remove('show');
                    nextEl.classList.remove('show');
                }

            })
        });

    }
});

function hoverColor(button){
    $(button).mouseover(function(){
        button.css('background-color', '#ffd500'); //how to change back after?
        button.css('border-style', 'dashed');
    });
    button.mouseout(function(){
        button.css('background-color', '#ffeb8a'); //how to change back after?
        button.css('border-style', 'solid');
    });
}

$(document).ready(function () {
    hoverColor($("#nextl"))
    hoverColor($("#nextq"))
})
