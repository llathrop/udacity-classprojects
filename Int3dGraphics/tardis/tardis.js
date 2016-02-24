			// Our Javascript will go here.
var camera, scene, renderer, stats, engine;
var cameraControls, effectController;
var clock = new THREE.Clock();
var cylinder, sphere, tardis, box, boxTop,skyBox,smokeringParticleGroup, smokeringEmitter;
var light;
var tardisDirection = 1, angle =0, tardisSpeed = 2;
var camx,camy,camz;


function init() {
	var canvasWidth = window.innerWidth;
	var canvasHeight = window.innerHeight;

	// RENDERER
	renderer = new THREE.WebGLRenderer( { antialias: true } );
	renderer.gammaInput = true;
	renderer.gammaOutput = true;
	renderer.setSize(canvasWidth, canvasHeight);
	renderer.setClearColor( 0x0, 1.0 );
	renderer.shadowMapEnabled = true;

	var container = document.getElementById('container');
	container.appendChild( renderer.domElement );

	// CAMERA
	camera = new THREE.PerspectiveCamera( 50, canvasWidth/ canvasHeight, 1, 4000 );
	camera.position.set( -100, 50, -10 );

	// CONTROLS
	cameraControls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
	cameraControls.target.set(0,50,0);
	
	// STATS
	stats = new Stats();
	stats.setMode( 0 );
	stats.domElement.style.position = 'absolute';
	stats.domElement.style.top = '0px';
	stats.domElement.style.zIndex = 100;
	container.appendChild( stats.domElement );

	stats.domElement.children[ 0 ].children[ 0 ].style.color = "#aaa";
	stats.domElement.children[ 0 ].style.background = "transparent";
	stats.domElement.children[ 0 ].children[ 1 ].style.display = "none";

	
}

function fillScene() {
	scene = new THREE.Scene();
	scene.fog = new THREE.Fog( 0x0, 2000, 4000 );

	// LIGHTS
	scene.add( new THREE.AmbientLight( 0x222222 ) );
	
	light = new THREE.SpotLight( 0xFFFFFF, 1.0 );
	light.position.set( -300, 500, 200 );
	light.angle = 20 * Math.PI / 180;
	light.exponent = 1;
	light.target.position.set( 0, 200, 0 );
	light.castShadow = false;

	scene.add( light );

	var lightSphere = new THREE.Mesh(
		new THREE.SphereGeometry( 10, 12, 6 ),
		new THREE.MeshBasicMaterial() );
	lightSphere.position.copy( light.position );

	scene.add( lightSphere );

	//groundGrid(500,10);
	
	//setup the smokering
	smokering();
	scene.add( smokeringParticleGroup.mesh );
	smokeringParticleGroup.material.side =THREE.DoubleSide;
	smokeringParticleGroup.material.blending =5;
	
	//run a helix smokering
	smokeringHelix();

	
	//var axes = new THREE.AxisHelper(100);
	//scene.add( axes );
	
	//SkyBox
	var imagePrefix = "media/img/dawnmountain-";
	var directions  = ["xpos", "xneg", "ypos", "yneg", "zpos", "zneg"];
	var imageSuffix = ".png";
	var skyGeometry = new THREE.BoxGeometry( 4000, 4000, 4000 );
	
	var materialArray = [];
	for (var i = 0; i < 6; i++)
		materialArray.push( new THREE.MeshBasicMaterial({
			map: THREE.ImageUtils.loadTexture( imagePrefix + directions[i] + imageSuffix ),
			side: THREE.DoubleSide
		}));
	var skyMaterial = new THREE.MeshFaceMaterial( materialArray );
	skyBox = new THREE.Mesh( skyGeometry, skyMaterial );
	skyBox.receiveShadow = false;
	skyBox.position.y = 250;
	scene.add( skyBox );
	

	//add the tardis model in
	tardis = new THREE.Object3D();
	createTardis(tardis);
	scene.add( tardis );
	
	
}

function setupGui() {
	effectController = {
		tardisCam : true,
		tardisFollow : false,
		tardisAnimate: false,
		tardisSpeed: 0,
		//tardisx: 0,
		//tardisy: 25,
		//tardisz: 0
		
	};
	var gui = new dat.GUI();
	gui.add( effectController, "tardisCam");
	gui.add( effectController, "tardisFollow");
	//gui.add( effectController, "tardisAnimate");
	gui.add( effectController, "tardisSpeed", 0.0, 15.0 ).name("tardisSpeed");
	//gui.add( effectController, "tardisx", -500.0, 500.0 ).name("tardisX");
	//gui.add( effectController, "tardisy", -500.0, 500.0 ).name("tardisY");
	//gui.add( effectController, "tardisz", -500.0, 500.0 ).name("tardisZ");
}

function addToDOM() {
	var container = document.getElementById('container');
	var canvas = container.getElementsByTagName('canvas');
	if (canvas.length>0) {
		container.removeChild(canvas[0]);
	}
	container.appendChild( renderer.domElement );
}

function animate() {
	window.requestAnimationFrame(animate);
	render();
}

function render() {
	var delta = clock.getDelta();
	cameraControls.update(delta);
	
	smokeringParticleGroup.tick( delta );
	
	//if (effectController.tardisAnimate==true) { //move the tardis according to the script
		tardisAnimation(effectController.tardisSpeed);
	//}
	if (effectController.tardisCam==true) { //cam follows the tardis
		cameraControls.target.set(tardis.position.x, tardis.position.y, tardis.position.z);
	}
	if (effectController.tardisFollow==true) { //keep the camera at it's current position relative to the tardis
		camera.position.set( tardis.position.x+camx, tardis.position.y+camy, tardis.position.z+camz );
	}
	else { //keep track of where the camera is relative to tardis
		camx = camera.position.x-tardis.position.x;
		camy = camera.position.y-tardis.position.y;
		camz = camera.position.z-tardis.position.z;
	}
	//move the tardis with the controls
	//tardis.position.x = effectController.tardisx;
	//tardis.position.y = effectController.tardisy;
	//tardis.position.z = effectController.tardisz;
	
	//move the skybox and light target with the tardis, as it is the focus
	skyBox.position.copy(tardis.position);
	light.target.position.copy(tardis.position);
	smokeringEmitter.position.copy(tardis.position);
	if (tardisDirection == 1){ smokeringEmitter.position.x  += 300;}
		else {smokeringEmitter.position.x  -= 300;}
	

	var radius = 200;
	if (angle>=360){
		angle = 1;
		}
	else{
		angle+=3;
		}

	//smokeringEmitter.position.y = radius * Math.cos(angle*Math.PI/180.0) + smokeringEmitter.position.y ;
	//smokeringEmitter.position.z = radius * Math.sin(angle*Math.PI/180.0) + smokeringEmitter.position.z ;
	//smokeringEmitter.position.x = radius * Math.sin(angle*Math.PI/180.0) + smokeringEmitter.position.x ;

	//console.log( "tardispos: ",tardis.position);

	
	renderer.render(scene, camera);
	
}

try {
	init();
	fillScene();
	setupGui();
	addToDOM();
} catch(e) {
	console.log(">>Your program encountered an unrecoverable error in setup, can not draw on canvas. Error was:<br/><br/> ",e);
}

try {
	animate();
} catch(e) {
	console.log(">>Your program encountered an unrecoverable error in render, can not draw on canvas. Error was:<br/><br/> ",e);
}


