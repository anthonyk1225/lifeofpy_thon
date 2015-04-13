$(document).ready(function(){
    
    // $.get('/characters/list/', function(data){
    //     $('.content').empty();
    //     var template = $('#welcomePage').html();
    //     var output = Mustache.render(template,data);
    //     $('.content').html(output);
    // });

    $('#character_list').on('click',function(event){
        event.preventDefault();
        $('.content').empty();
        $.get('/characters/list/', function(data){
            var template = $('#welcomePage').html();
            var output = Mustache.render(template,data);
            $('.content').html(output);
        });
    });
});