
$(document).ready(function(){

$('.menu-pick').click(function(e) {
    if ($('#navigation-side-bar').hasClass('nav-closed')) {
        $('nav').removeClass('nav-closed');
        $('nav').addClass('nav-open');
        $('.nav-button').removeClass('nav-button-closed')
        $('.nav-button').addClass('nav-button-open');        
    } else {
        $('nav').removeClass("nav-open");
        $('nav').addClass("nav-closed");
        $('.nav-button').removeClass('nav-button-open')
        $('.nav-button').addClass('nav-button-closed');
    }
    e.preventDefault()
});

});