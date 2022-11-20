/*script.js
Github repository for this BSP: https://github.com/CookNChips/BSP1---DoodleRec-Deep-Learning-Image-Recognition
For easier use, please execute the DoodleRec.bat file provided with this, or read the README file*/

const canvas = document.getElementById("canvas"); //Create a canvas element
const ctx = canvas.getContext("2d"); //As well as a context zone for intercation

let painting = false; //Initialize painting state

//Initialize starting position to avoid errors with the user's mouse position
function startPos(e) {
    painting = true;
    draw(e);
}

function finPos() {
  painting = false;
  ctx.beginPath();
}

//Initialize canvas' size and context zone to be 28x28 pixels rendered into 420x420px
canvas.width = 28;
canvas.height = 28;
canvas.style.width = "420px";
canvas.style.height = "420px";
ctx.scale((28/420), (28/420));

//draw function with event listeners
function draw(e) {
    if (!painting) return;
    ctx.imageSmoothingEnabled = false;
    ctx.lineWidth = 35;
    ctx.lineCap = "circle";
    ctx.lineTo(e.clientX - 100, e.clientY - 100);
    ctx.stroke();
    ctx.strokeStyle = "#FFFFFF";
    ctx.beginPath()
    ctx.moveTo(e.clientX - 100, e.clientY - 100);
}

canvas.addEventListener('mousedown', startPos);
canvas.addEventListener('mouseup', finPos);
canvas.addEventListener('mousemove', draw);

//Every 1s, this function takes the image data of the input image and returns an array of it
//It then parses it to a JSON request, that will be fetched by the Flask application
setInterval(function(){ 
    imgData = ctx.getImageData(0,0,28,28);
    imgDataBW = [];
    imgDataBW.push(imgData.data[3]);
    for (var i = 7; i < imgData.data.length + 1; i = i + 4) {
        imgDataBW.push(imgData.data[i]);
    }

    var sendData = {
        "userinput" : imgDataBW
        }
          fetch(`${window.origin}/`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(sendData),
            cache: "no-cache",
            headers: new Headers({
              "content-type": "application/json"
            })
          })

}, 1000);