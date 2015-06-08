$(document).ready(function(){
    
    $('#character_list').on('click',function(event){
        event.preventDefault();
        $('.content').empty();
        $.get('/characters/list/', function(data){
            var template = $('#welcomePage').html();
            var output = Mustache.render(template,data);
            $('.content').append(output);
        });
    });

    $('#character_list').trigger('click');

    $('#battle').on('click',function(event){
        event.preventDefault();
        $('.content').empty();
        $.get('/characters/list/', function(data){
            var template = $('#character_selection').html();
            var output = Mustache.render(template,data);
            $('.content').append(output);
        });
    });

    $('#make_character').on('click',function(event){
        event.preventDefault();
        $('.content').empty();
        var template = $('#classes').html();
        var output = Mustache.render(template);
        $('.content').append(output);
    });

    $('.content').on('submit', '.create',function(event){
        event.preventDefault();
        $.post(this.action ,$(this).serialize(), function(data){
            $('#character_list').trigger('click');
        });
    });

});