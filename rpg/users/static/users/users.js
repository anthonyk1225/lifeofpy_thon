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

    $(document).on('submit','#logInForm',function(event){
        event.preventDefault();
        var template = $('#userGreeting').html();
        var output = Mustache.render(template,{username:  $('input[name=username]').val()})
        $('header div:last-child').remove();
        $('header').append(output)
    });

    $(document).on('submit','#registerForm',function(event){
        event.preventDefault();
        var template = $('#userGreeting').html();
        var username = $('input[name=username]').val();
        var output = Mustache.render(template,{username:  $('input[name=username]').val()})
        $('header div:last-child').remove();
        $('header').append(output)
    });

});