$(document).ready(function() {

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
    });

    $(window).bind("pageshow", function(event) {
        $("#overlay").hide();
    });

    $('#myModal').modal('show')
});