$(document).ready(function(){
    
    $.get('/characters/list/', function(data){
        var template = $('#welcomePage').html();
        var output = Mustache.render(template,data);
        $('.content').append(output);
    });
});