$(document).ready(function(){
    $('.btn-primary').on('click', function(event){
    	event.preventDefault();
	    var villianHealth = $('#villianhealth')[0].innerHTML
		var heroHealth = $('#herohealth')[0].innerHTML
		var heroHitFor = $('#heropower')[0].innerHTML
		var villianHitFor = $('#villianpower')[0].innerHTML
    	$('#villianhealth').html(parseInt(villianHealth) - heroHitFor)
    	$('#update').html('Your ' + $('.btn-primary')[0].innerHTML +' hit for ' + heroHitFor + ' dmg.')
    	if (parseInt($('#villianhealth')[0].innerHTML) < 1){
			$('#update').html('You win!');
				setTimeout(function() {
	    		window.location.replace('/characters/')
	  	},1500);
		}
		else{
	    	setTimeout(function() {
	    		$('#herohealth').html(parseInt(heroHealth)-villianHitFor);
	    		$('#update').html('Villians attack hit for ' + villianHitFor + ' dmg.');
	  	},1500);
		if (parseInt($('#herohealth')[0].innerHTML) < 1){
			$('#update').html('You Lose!');
				setTimeout(function() {
	    		window.location.replace('/characters/')
	  	},1500);
	}
	}
	})
})
