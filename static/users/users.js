$(document).ready(function(){
    $('#logInLink').on('click',function(event){
        event.preventDefault();
        $('header div:last-child').remove();
        var template = $('#logIn').html();
        var output = Mustache.render(template);
        $('header').append(output)
    });

    $('#registerLink').on('click',function(event){
        event.preventDefault();
        $('header div:last-child').remove();
        var template = $('#register').html();
        var output = Mustache.render(template);
        $('header').append(output)
    });
});