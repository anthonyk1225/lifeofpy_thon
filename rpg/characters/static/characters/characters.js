$(document).ready(function(){
    $.get('/characters/list/', function(data){
        $('.content').empty();
        var template = $('#welcomePage').html();
        var output = Mustache.render(template,data);
        $('.content').append(output);
    });

    $('#character_list').on('click',function(event){
        event.preventDefault();
        $('.content').empty();
        $.get('/characters/list/', function(data){
            $('.content').empty();
            var template = $('#welcomePage').html();
            var output = Mustache.render(template,data);
            $('.content').append(output);
        });
    });

    $('#make_character').on('click',function(event){
        event.preventDefault();
        $('.content').empty();
        $('#classes').css({'display': 'block'})
    });

    $('#classes form').on('submit',function(event){
        event.preventDefault();
        $('.content').empty();
        $('#classes').css({'display': 'none'});
    });
});