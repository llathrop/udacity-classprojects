function groundGrid( size,units){
	///////////////////////
	// GROUND
	// put grid lines every 10000/100 = 100 units
	var solidGround = new THREE.Mesh(
		new THREE.PlaneGeometry( size, size ),
		new THREE.MeshPhongMaterial({ color: 0xFFFFFF,
			// polygonOffset moves the plane back from the eye a bit, so that the lines on top of
			// the grid do not have z-fighting with the grid:
			// Factor == 1 moves it back relative to the slope (more on-edge means move back farther)
			// Units == 4 is a fixed amount to move back, and 4 is usually a good value
			polygonOffset: true, polygonOffsetFactor: 1.0, polygonOffsetUnits: 4.0
		}));
	solidGround.rotation.x = -Math.PI / 2;
	solidGround.receiveShadow = true;

	scene.add( solidGround );

	var ground = new THREE.Mesh(
		new THREE.PlaneGeometry( size, size, size/units, size/units ),
		new THREE.MeshBasicMaterial( { color: 0x0, wireframe: true } ) );
	ground.rotation.x = - Math.PI / 2;
	scene.add( ground );
	
	
}