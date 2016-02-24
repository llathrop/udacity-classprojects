			// Our Javascript will go here.
var camera, scene, renderer, stats, engine;
var cameraControls, effectController;
var clock = new THREE.Clock();
var cylinder, sphere, pinewood, box, boxTop,skyBox,smokeringParticleGroup, smokeringEmitter;
var light;
var pinewoodDirection = 1, angle =0, pinewoodSpeed = 2;
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
	light.position.set( -100, 200, 50 );
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

	groundGrid(1000,10);

	
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
	

	//add the pinewood model in
	pinewood = new THREE.Object3D();
	createPinewood(pinewood);
	scene.add( pinewood );
	
}

function setupGui() {
	effectController = {
		pinewoodCam : true,
		pinewoodFollow : false,
		pinewoodAnimate: false,
		pinewoodSpeed: 0,
		//pinewoodx: 0,
		//pinewoody: 25,
		//pinewoodz: 0
		
	};
	var gui = new dat.GUI();
	gui.add( effectController, "pinewoodCam");
	gui.add( effectController, "pinewoodFollow");
	//gui.add( effectController, "pinewoodAnimate");
	gui.add( effectController, "pinewoodSpeed", 0.0, 15.0 ).name("pinewoodSpeed");
	//gui.add( effectController, "pinewoodx", -500.0, 500.0 ).name("pinewoodX");
	//gui.add( effectController, "pinewoody", -500.0, 500.0 ).name("pinewoodY");
	//gui.add( effectController, "pinewoodz", -500.0, 500.0 ).name("pinewoodZ");
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
	

	//if (effectController.pinewoodAnimate==true) { //move the pinewood according to the script
		pinewoodAnimation(effectController.pinewoodSpeed);
	//}
	if (effectController.pinewoodCam==true) { //cam follows the pinewood
		cameraControls.target.set(pinewood.position.x, pinewood.position.y, pinewood.position.z);
	}
	if (effectController.pinewoodFollow==true) { //keep the camera at it's current position relative to the pinewood
		camera.position.set( pinewood.position.x+camx, pinewood.position.y+camy, pinewood.position.z+camz );
	}
	else { //keep track of where the camera is relative to pinewood
		camx = camera.position.x-pinewood.position.x;
		camy = camera.position.y-pinewood.position.y;
		camz = camera.position.z-pinewood.position.z;
	}
	//move the pinewood with the controls
	//pinewood.position.x = effectController.pinewoodx;
	//pinewood.position.y = effectController.pinewoody;
	//pinewood.position.z = effectController.pinewoodz;
	
	//move the skybox and light target with the pinewood, as it is the focus
	skyBox.position.copy(pinewood.position);
	light.target.position.copy(pinewood.position);

	

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

	//console.log( "pinewoodpos: ",pinewood.position);

	
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


