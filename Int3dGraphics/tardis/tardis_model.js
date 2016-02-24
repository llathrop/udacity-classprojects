function createTardis(tardis){
	// Tardis blue: color: 0x102372
	//var material = new THREE.MeshBasicMaterial( { color: 0x102372 } );
	
	var tardisTextureMap =  THREE.ImageUtils.loadTexture( 'media/img/tardisTextureMap.png' );
	var material = new THREE.MeshPhongMaterial({map: tardisTextureMap });
	
	
	var TardisSideA = [new THREE.Vector2(0, 0.55), new THREE.Vector2(.25, .55), new THREE.Vector2(.25, .97), new THREE.Vector2(0, .97)];
	var TardisSideB = [new THREE.Vector2(0.25, 0.55), new THREE.Vector2(.50, .55), new THREE.Vector2(.50, .97), new THREE.Vector2(.25, .97)];
	var TardisSideC = [new THREE.Vector2(0.50, 0.55), new THREE.Vector2(.75, .55), new THREE.Vector2(.75, .97), new THREE.Vector2(0.50, .97)];
	var TardisSideD = [new THREE.Vector2(0.75, 0.55), new THREE.Vector2(1, .55), new THREE.Vector2(1, .97), new THREE.Vector2(0.75, .97),];
	var TardisTopBottom = [new THREE.Vector2(0.68, 0.10), new THREE.Vector2(.9, .10), new THREE.Vector2(.9, .35), new THREE.Vector2(0.68, .35)];
	//var TardisBottom = [new THREE.Vector2(0.75, 0.5), new THREE.Vector2(1, .5), new THREE.Vector2(1, 1), new THREE.Vector2(0.75, 1)];

	
	var geometry = new THREE.BoxGeometry( 30, 50, 30 );
	geometry.faceVertexUvs[0] = [];
	
	geometry.faceVertexUvs[0][8] = [ TardisSideA[3], TardisSideA[0], TardisSideA[2] ];
	geometry.faceVertexUvs[0][9] = [ TardisSideA[0], TardisSideA[1], TardisSideA[2] ];
	
	geometry.faceVertexUvs[0][2] = [ TardisSideB[3], TardisSideB[0], TardisSideB[2] ];
	geometry.faceVertexUvs[0][3] = [ TardisSideB[0], TardisSideB[1], TardisSideB[2] ];
	
	geometry.faceVertexUvs[0][0] = [ TardisSideC[3], TardisSideC[0], TardisSideC[2] ];
	geometry.faceVertexUvs[0][1] = [ TardisSideC[0], TardisSideC[1], TardisSideC[2] ];
	
	geometry.faceVertexUvs[0][10] = [ TardisSideD[3], TardisSideD[0], TardisSideD[2] ];
	geometry.faceVertexUvs[0][11] = [ TardisSideD[0], TardisSideD[1], TardisSideD[2] ];
	
	geometry.faceVertexUvs[0][4] = [ TardisTopBottom[3], TardisTopBottom[0], TardisTopBottom[2] ];
	geometry.faceVertexUvs[0][5] = [ TardisTopBottom[0], TardisTopBottom[1], TardisTopBottom[2] ];
	
	geometry.faceVertexUvs[0][6] = [ TardisTopBottom[3], TardisTopBottom[0], TardisTopBottom[2] ];
	geometry.faceVertexUvs[0][7] = [ TardisTopBottom[0], TardisTopBottom[1], TardisTopBottom[2] ];
	
	box = new THREE.Mesh( geometry, material );
	box.position.y= 00;
	tardis.add( box);
	
	
	var material = new THREE.MeshBasicMaterial( { color: 0x102372 } );
	var geometry = new THREE.BoxGeometry( 5, 5, 5 );
    boxTopLight = new THREE.Mesh( geometry, material );
	boxTopLight.position.y= 25;
	tardis.add( boxTopLight);
	
	tardis.position.set(0,25,0);
	//tardis.castShadow = true;
}