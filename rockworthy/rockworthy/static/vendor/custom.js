var $grid = $('.grid').masonry({
    // options...
    itemSelector: '.grid-item',
    transitionDuration: 0,
  });

$grid.imagesLoaded().progress(function() {
    // init Masonry
    $grid.masonry('layout');
    $('.card').removeClass('hide');
  });

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

    $(".container, .container-fluid").click(function() {
        if($('#navigation-side-bar').hasClass('nav-open')) {
            $('nav').removeClass("nav-open");
            $('nav').addClass("nav-closed");
            $('.nav-button').removeClass('nav-button-open')
            $('.nav-button').addClass('nav-button-closed');
            $('body').removeClass('stop-mobile-scroll')
        }
    })

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

    var scrollToTop = 0;
    
    $(window).scroll(function(){
        var scr = $(window).scrollTop();
        if (scr > scrollToTop || scr < 500) {
            $('#myBtn').removeClass('btn-top-show');
            $('#myBtn').addClass('btn-top-hide');
        } else {
            $('#myBtn').addClass('btn-top-show');
            $('#myBtn').removeClass('btn-top-hide');
        }
        scrollToTop = scr;
    });

    $("input[name=name]").on('focusin', function(e){
        $(e.target).addClass('focused');
    });

    $("input[name=name]").on('focusout', function(e){
        $(e.target).removeClass('focused');
    });

    $("input[name=email]").on('focusin', function(e){
        $(e.target).next('.form-text').removeClass('hide');
        $(e.target).addClass('focused');
    });

    $("input[name=email]").on('focusout', function(e){
        $(e.target).next('.form-text').addClass('hide');
        $(e.target).removeClass('focused');
    });

    $(document).on('focusin', 'textarea', function(e){
        $(e.target).next('.form-text').removeClass('hide');
        $(e.target).addClass('focused');
    });

    $(document).on('focusout', 'textarea', function(e){
        $(e.target).next('.form-text').addClass('hide');
        $(e.target).removeClass('focused');
    });

    $("input[name=email]").on('change focusout', function(e){
        if($(e.target).is(':invalid'))  {
            $('#emailHelp').removeClass('hide');
        } else {
            $('#emailHelp').addClass('hide');
        }
    });

    $("input[name=name]").on('change focusout', function(e){
        if($(e.target).is(':invalid'))  {
            $('#nameHelp').removeClass('hide');
        } else {
            $('#nameHelp').addClass('hide');
        }
    });

    $(document).on('change focusout', 'textarea', function(e){
        if($(e.target).is(':invalid'))  {
            $('#queryHelp').removeClass('hide');
        } else {
            $('#queryHelp').addClass('hide');
        }
    });

    $("form").submit(function() {
        document.getElementById("overlay").style.display = "block";
        document.getElementById("overlay_text").style.display = "block";
    });

    $(window).bind("pageshow", function(event) {
        $("#overlay").hide();
    });
    
    $(window).bind("pageshow", function(event) {
        $("#overlay_text").hide();
    });

    $('#myModal').modal('show')    

});
