$(document).ready(function(){
    $.getJson('/characters/list/', function(data){

        var template = $('#welcomePage').html();
        console.log(template)
        var output = Mustache.render(template,data);
        console.log(output)
        $('.content').append(output);
    });
});