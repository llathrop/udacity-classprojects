function smokering(){
// Create particle group
    smokeringParticleGroup = new SPE.Group({
    texture: THREE.ImageUtils.loadTexture("media/img/cloud.png"),
    maxAge: 15,
    hasPerspective: 0,
    colorize: 1,
    transparent: 1,
    alphaTest: 0.5,
    depthWrite: false,
    depthTest: true,
    blending: THREE.AdditiveBlending
});

// Create particle emitter 0
    smokeringEmitter = new SPE.Emitter( {
    type: 'sphere',
    particleCount: 4000,
	particlesPerSecond: 120,
    position: new THREE.Vector3( 0, 0, 0 ),
    positionSpread: new THREE.Vector3( 0, 0, 0 ),
    radius: 200,
    radiusSpread: 1.5,
    radiusSpreadClamp: 0,
    radiusScale: new THREE.Vector3( 1,1, 1 ),
    speed: 1,
    speedSpread: 1.2,
    sizeStart: 120,
    sizeStartSpread: 1,
      angleStart: -1.6,
    angleStartSpread: 0,
    angleAlignVelocity: false,
    colorStart: new THREE.Color( 0x888888 ),
    opacityStart: .5,
    opacityStartSpread: 0,
    duration: null,
    alive: 0.95,
    isStatic: 0
} );


smokeringParticleGroup.addEmitter( smokeringEmitter );
}



function smokeringHelix(){
	
	var smokeTextureMap =  THREE.ImageUtils.loadTexture( 'media/img/smokeparticle.png' );
	smokeTextureMap.repeat=new THREE.Vector2( 2,2);
	smokeTextureMap.wrapS = smokeTextureMap.wrapT = THREE.MirroredRepeatWrapping;
	
	var smokeMaterial = new THREE.MeshLambertMaterial( { map: smokeTextureMap,  } );
	
	var radius = 150;
	var tube = 35;
	var radialSegments = 15;
	var height = 1200;
	var segmentsWidth = 50;
	var arc = 6;

	var helix;
	helix = createHelix( smokeMaterial, radius, tube, radialSegments, segmentsWidth, height, arc, true );
	helix.position.x = height/2;
	helix.rotation.z = 90 * Math.PI / 180;
	scene.add( helix );
}


function createHelix( material, radius, tube, radialSegments, tubularSegments, height, arc, clockwise )
{
	// defaults
	tubularSegments = (tubularSegments === undefined) ? 32 : tubularSegments;
	arc = (arc === undefined) ? 1 : arc;
	clockwise = (clockwise === undefined) ? true : clockwise;

	var helix = new THREE.Object3D();

	var top = new THREE.Vector3();

	var sine_sign = clockwise ? 1 : -1;

	///////////////
	// YOUR CODE HERE: remove spheres, use capsules instead, going from point to point.
	//
	var capBottom= new THREE.Vector3();
	
	capBottom.set( radius, -height/2, 0 );
	
	var openBottom =false;
	
	for ( var i = 0; i <= arc*radialSegments ; i++ )
	{
		// going from X to Z axis
		top.set( radius * Math.cos( i * 2*Math.PI / radialSegments ),
			height * (i/(arc*radialSegments)) - height/2,
			sine_sign * radius * Math.sin( i * 2*Math.PI / radialSegments ) );
		
		var cap =  createCapsule( material, tube, top, capBottom, tubularSegments, false, openBottom );
		helix.add( cap );
		
		openBottom = true;
		
		capBottom.copy(top);
	}
	///////////////

	return helix;
}

/**
* Returns a THREE.Object3D cylinder and spheres going from top to bottom positions
* @param material - THREE.Material
* @param radius - the radius of the capsule's cylinder
* @param top, bottom - THREE.Vector3, top and bottom positions of cone
* @param segmentsWidth - tessellation around equator, like radiusSegments in CylinderGeometry
* @param openTop, openBottom - whether the end is given a sphere; true means they are not
*/
function createCapsule( material, radius, top, bottom, segmentsWidth, openTop, openBottom )
{
	// defaults
	segmentsWidth = (segmentsWidth === undefined) ? 32 : segmentsWidth;
	openTop = (openTop === undefined) ? false : openTop;
	openBottom = (openBottom === undefined) ? false : openBottom;

	// get cylinder height
	var cylAxis = new THREE.Vector3();
	cylAxis.subVectors( top, bottom );
	var length = cylAxis.length();

	// get cylinder center for translation
	var center = new THREE.Vector3();
	center.addVectors( top, bottom );
	center.divideScalar( 2.0 );

	// always open-ended
	var cylGeom = new THREE.CylinderGeometry( radius, radius, length, segmentsWidth, 1, 1 );
	var cyl = new THREE.Mesh( cylGeom, material );

	// pass in the cylinder itself, its desired axis, and the place to move the center.
	makeLengthAngleAxisTransform( cyl, cylAxis, center );

	var capsule = new THREE.Object3D();
	capsule.add( cyl );
	if ( !openTop || !openBottom ) {
		// instance geometry
		var sphGeom = new THREE.SphereGeometry( radius, segmentsWidth, segmentsWidth/2 );
		if ( !openTop ) {
			var sphTop = new THREE.Mesh( sphGeom, material );
			sphTop.position.set( top.x, top.y, top.z );
			capsule.add( sphTop );
		}
		if ( !openBottom ) {
			var sphBottom = new THREE.Mesh( sphGeom, material );
			sphBottom.position.set( bottom.x, bottom.y, bottom.z );
			capsule.add( sphBottom );
		}
	}

	return capsule;

}

// Transform cylinder to align with given axis and then move to center
function makeLengthAngleAxisTransform( cyl, cylAxis, center )
{
	cyl.matrixAutoUpdate = false;

	// From left to right using frames: translate, then rotate; TR.
	// So translate is first.
	cyl.matrix.makeTranslation( center.x, center.y, center.z );

	// take cross product of cylAxis and up vector to get axis of rotation
	var yAxis = new THREE.Vector3(0,1,0);
	// Needed later for dot product, just do it now;
	// a little lazy, should really copy it to a local Vector3.
	cylAxis.normalize();
	var rotationAxis = new THREE.Vector3();
	rotationAxis.crossVectors( cylAxis, yAxis );
	if ( rotationAxis.length() < 0.000001 )
	{
		// Special case: if rotationAxis is just about zero, set to X axis,
		// so that the angle can be given as 0 or PI. This works ONLY
		// because we know one of the two axes is +Y.
		rotationAxis.set( 1, 0, 0 );
	}
	rotationAxis.normalize();

	// take dot product of cylAxis and up vector to get cosine of angle of rotation
	var theta = -Math.acos( cylAxis.dot( yAxis ) );
	//cyl.matrix.makeRotationAxis( rotationAxis, theta );
	var rotMatrix = new THREE.Matrix4();
	rotMatrix.makeRotationAxis( rotationAxis, theta );
	cyl.matrix.multiply( rotMatrix );
}