
$(document).ready(function(){

$('.menu-pick').click(function() {
    if ($('#navigation-side-bar').hasClass('nav-closed')) {
        $('nav').removeClass('nav-closed');
        $('nav').addClass('nav-open');
    } else {
        $('nav').removeClass("nav-open");
        $('nav').addClass("nav-closed");
    }
    
});

});