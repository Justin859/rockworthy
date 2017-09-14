
$(document).ready(function(){

    $('.menu-pick').click(function(e) {
        if ($('#navigation-side-bar').hasClass('nav-closed')) {
            $('nav').removeClass('nav-closed');
            $('nav').addClass('nav-open');
            $('.nav-button').removeClass('nav-button-closed')
            $('.nav-button').addClass('nav-button-open');
            $('body').addClass('stop-mobile-scroll')     
        } else {
            $('nav').removeClass("nav-open");
            $('nav').addClass("nav-closed");
            $('.nav-button').removeClass('nav-button-open')
            $('.nav-button').addClass('nav-button-closed');
            $('body').removeClass('stop-mobile-scroll')
        }
        e.preventDefault()
    });

    var lastScrollTop = 0;

    $(window).scroll(function(event){
       var st = $(this).scrollTop();
       if (st > lastScrollTop){
           $('.nav-button').addClass('hide-button');
       } else {
           $('.nav-button').removeClass('hide-button');
       }
       lastScrollTop = st;
    });

});