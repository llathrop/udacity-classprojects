
function pinewoodAnimation(speed){

	if (pinewood.position.z >= 400){
		pinewoodDirection=0;
		//console.log("greater than 60", pinewoodDirection);
	}
	if (pinewood.position.z <= -400){
		pinewoodDirection=1;
		//console.log("less than 0", pinewoodDirection);
	}
	if (pinewoodDirection == 1){
		//pinewood.position.y = 
		pinewood.position.z +=speed;
		//pinewood.position.x = Math.cos(pinewood.position.y);
	}
	else {
	//pinewood.position.y = 
	pinewood.position.z -=speed;
//	pinewood.position.x -=Math.sin(pinewood.position.y);
	}
	
	effectController.pinewoody = pinewood.position.y;
	effectController.pinewoodx = pinewood.position.x;

	
	//pinewood.rotation.x = pinewood.rotation.y += 0.015*speed;
	//pinewood.rotation.y += 0.03;
	//pinewood.rotation.y += 0.03;

	
}