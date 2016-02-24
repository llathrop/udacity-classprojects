
function tardisAnimation(speed){

	if (tardis.position.x >= 800){
		tardisDirection=0;
		//console.log("greater than 60", tardisDirection);
	}
	if (tardis.position.x <= -00){
		tardisDirection=1;
		//console.log("less than 0", tardisDirection);
	}
	if (tardisDirection == 1){
		//tardis.position.y = 
		tardis.position.x +=speed;
		//tardis.position.x = Math.cos(tardis.position.y);
	}
	else {
	//tardis.position.y = 
	tardis.position.x -=speed;
//	tardis.position.x -=Math.sin(tardis.position.y);
	}
	
	effectController.tardisy = tardis.position.y;
	effectController.tardisx = tardis.position.x;

	
	tardis.rotation.x = tardis.rotation.y += 0.015*speed;
	//tardis.rotation.y += 0.03;
	//tardis.rotation.y += 0.03;

	
}