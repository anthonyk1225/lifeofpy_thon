// function Battle(player1, player2){
//     this.fighter = [player1, player2]
// }

// function Fighter(){

// }

function battleLog(winner, loser){
    $("input[name='winner']").val(winner);
    $("input[name='loser']").val(loser);
    // triggerHandler did not work
    $("#battle_log").trigger("submit");
}

$(document).ready(function(){

    $('.btn-primary').on('click', function(event){
    	event.preventDefault();

	    var villianHealth = $('#villianhealth')[0].innerHTML,
		heroHealth = $('#herohealth')[0].innerHTML,
		heroHitFor = $('#heropower')[0].innerHTML,
		villianHitFor = $('#villianpower')[0].innerHTML,
		damage = parseInt(villianHealth) - heroHitFor;

    	$('#villianhealth').html((damage > 0 ? damage : 0));
    	$('#update').html('Your ' + $('.btn-primary')[0].innerHTML +' hit for ' + heroHitFor + ' dmg.')
    	

    	if (parseInt($('#villianhealth')[0].innerHTML) < 1){
            $('#update').html('You win!');
            setTimeout(function() {
                battleLog($("input[name='winner']").val(), $("input[name='loser']").val());
            },1500);

		}
		else{
	    	setTimeout(function(){
	    		$('#herohealth').html(parseInt(heroHealth)-villianHitFor);
	    		$('#update').html('Villians attack hit for ' + villianHitFor + ' dmg.');
	  		},1500);
			if (parseInt($('#herohealth')[0].innerHTML) < 1){  
                $('#update').html('You Lose!');
                setTimeout(function() {
                    battleLog($("input[name='loser']").val(), $("input[name='winner']").val());
                },1500);
			}
		}
	});
});
