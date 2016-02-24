
function assignUVs(geometry ){

    geometry.computeBoundingBox();

    var max     = geometry.boundingBox.max;
    var min     = geometry.boundingBox.min;

    var offset  = new THREE.Vector2(0 - min.x, 0 - min.y);
    var range   = new THREE.Vector2(max.x - min.x, max.y - min.y);

    geometry.faceVertexUvs[0] = [];
    var faces = geometry.faces;

    for (i = 0; i < geometry.faces.length ; i++) {

      var v1 = geometry.vertices[faces[i].a];
      var v2 = geometry.vertices[faces[i].b];
      var v3 = geometry.vertices[faces[i].c];

      geometry.faceVertexUvs[0].push([
        new THREE.Vector2( ( v1.x + offset.x ) / range.x , ( v1.y + offset.y ) / range.y ),
        new THREE.Vector2( ( v2.x + offset.x ) / range.x , ( v2.y + offset.y ) / range.y ),
        new THREE.Vector2( ( v3.x + offset.x ) / range.x , ( v3.y + offset.y ) / range.y )
        ]);

    }

    geometry.uvsNeedUpdate = true;

}

function quadGeometry(corner0, corner1, corner2, corner3) {

	var quad = new THREE.Geometry();
	// Your code goes here
	quad.vertices.push( corner0 );
	quad.vertices.push( corner1 );
	quad.vertices.push( corner2 );
	quad.vertices.push( corner3 );
	
	quad.faces.push( new THREE.Face3( 0, 1, 2 ) );	
	quad.faces.push( new THREE.Face3( 1, 2, 3 ) );

	assignUVs(quad );
	// don't forget to return the geometry!	The following line is required!

	return quad;
}



function createPinewood(pinewood){
	// tardis blue: color: 0x102372
	
	var pinewoodTextureMap =  THREE.ImageUtils.loadTexture( 'media/img/crate.gif' );
	var quadMaterial = new THREE.MeshPhongMaterial({map: pinewoodTextureMap, side: THREE.DoubleSide});
		quadMaterial.wireframe = false;
		//quadMaterial.specular.setRGB(1,0.5,0.5);
		quadMaterial.emissive.setHex( 0xAdA79b );
		
	
//carfront
	quad0 = new THREE.Vector3(-10,0,0);
	quad1 = new THREE.Vector3(-10, 5,0);
	quad2 = new THREE.Vector3( 10,0,0);
	quad3 = new THREE.Vector3( 10, 5,0);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	quadMesh.position.y = 0;
	quadMesh.position.z = 0;
	pinewood.add(quadMesh);
	
//carRear
	quad0 = new THREE.Vector3(-12.5, 9, 70);
	quad1 = new THREE.Vector3(-12.5,0, 70);
	quad2 = new THREE.Vector3( 12.5, 9, 70);
	quad3 = new THREE.Vector3( 12.5,0, 70);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	pinewood.add(quadMesh);
	
//hood
	quad0 = new THREE.Vector3(-12.5, 6, 13.5);
	quad1 = new THREE.Vector3(-10, 5, 0);
	quad2 = new THREE.Vector3( 12.5, 6, 13.5);
	quad3 = new THREE.Vector3( 10, 5, 0);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	pinewood.add(quadMesh);
	
//hoodUnderside
	quad0 = new THREE.Vector3(-12.5,0, 13.5);
	quad1 = new THREE.Vector3(-10,0, 0);
	quad2 = new THREE.Vector3( 12.5,0, 13.5);
	quad3 = new THREE.Vector3( 10,0, 0);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	pinewood.add(quadMesh);
	
//CarTop
	quad0 = new THREE.Vector3(-12.5, 9, 70);
	quad1 = new THREE.Vector3(-12.5, 6, 13.5);
	quad2 = new THREE.Vector3( 12.5, 9, 70);
	quad3 = new THREE.Vector3( 12.5, 6, 13.5);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	pinewood.add(quadMesh);
	

//carBottom
	quad0 = new THREE.Vector3(-12.5, 0, 13.5);
	quad1 = new THREE.Vector3(-12.5, 0, 70);
	quad2 = new THREE.Vector3( 12.5, 0, 13.5);
	quad3 = new THREE.Vector3( 12.5, 0, 70);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	pinewood.add(quadMesh);
	
	
//carSideDriver
	quad0 = new THREE.Vector3(-12.5, 0, 13.5);
	quad1 = new THREE.Vector3(-12.5, 0, 70);
	quad2 = new THREE.Vector3(-12.5, 6, 13.5);
	quad3 = new THREE.Vector3(-12.5, 9, 70);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	pinewood.add(quadMesh);
	
//carSidePassenger
	quad0 = new THREE.Vector3(12.5, 0, 13.5);
	quad1 = new THREE.Vector3(12.5, 0, 70);
	quad2 = new THREE.Vector3(12.5, 6, 13.5);
	quad3 = new THREE.Vector3(12.5, 9, 70);
	
	var geometry = quadGeometry(quad0,quad1,quad2,quad3);
	var quadMesh = new THREE.Mesh(geometry, quadMaterial);
	pinewood.add(quadMesh);


//axel
	var axelMaterial = new THREE.MeshBasicMaterial({color: 0x999999});
	var axelGeometry = new THREE.CylinderGeometry( .8, .8, 34, 32 );
	
//axel Front
	var axel = new THREE.Mesh(axelGeometry, axelMaterial);
	axel.rotation.z = 90 * Math.PI/180;
	axel.position.z = 17.8;

	pinewood.add(axel);
//axel Rear
	var axel = new THREE.Mesh(axelGeometry, axelMaterial);
	axel.rotation.z = 90 * Math.PI/180;
	axel.position.z = 61.8;
	pinewood.add(axel);
	

//wheel
	var wheelMaterial = new THREE.MeshBasicMaterial({color: 0x111111});
	var wheelGeometry = new THREE.TorusGeometry( 6, 2.7, 16, 100 );

// wheel, front, driver
	var wheel = new THREE.Mesh(wheelGeometry, wheelMaterial);
	wheel.rotation.y = 90 * Math.PI/180;
	wheel.position.z = 17.8;
	wheel.position.x = -17;
	pinewood.add(wheel);

// wheel, front, passenger
	var wheel = new THREE.Mesh(wheelGeometry, wheelMaterial);
	wheel.rotation.y = 90 * Math.PI/180;
	wheel.position.z = 17.8;
	wheel.position.x = 17;
	pinewood.add(wheel);

// wheel, rear, driver
	var wheel = new THREE.Mesh(wheelGeometry, wheelMaterial);
	wheel.rotation.y = 90 * Math.PI/180;
	wheel.position.z = 61.8;
	wheel.position.x = -17;
	pinewood.add(wheel);

// wheel, rear, passenger
	var wheel = new THREE.Mesh(wheelGeometry, wheelMaterial);
	wheel.rotation.y = 90 * Math.PI/180;
	wheel.position.z = 61.8;
	wheel.position.x = 17;
	pinewood.add(wheel);


	pinewood.position.set(0,8.7,0);
	pinewood.castShadow = true;
}