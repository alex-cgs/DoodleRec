const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let painting = false;

function startPos(e) {
    painting = true;
    draw(e);
}

canvas.width = 28;
canvas.height = 28;
canvas.style.width = "420px";
canvas.style.height = "420px";

function finPos() {
    painting = false;
    ctx.beginPath();
}

ctx.scale((28/420), (28/420));

function draw(e) {
    if (!painting) return;
    ctx.lineWidth = 15;
    ctx.lineCap = "square";

    ctx.lineTo(e.clientX, e.clientY);
    ctx.stroke();
    ctx.beginPath()
    ctx.moveTo(e.clientX, e.clientY);
}

canvas.addEventListener('mousedown', startPos);
canvas.addEventListener('mouseup', finPos);
canvas.addEventListener('mousemove', draw);


setInterval(function(){ 
    imgData = ctx.getImageData(0,0,28,28);
    imgDataBW = [];
    imgDataBW.push(imgData.data[3]);
    for (var i = 7; i < imgData.data.length + 1; i = i + 4) {
        imgDataBW.push(imgData.data[i]);
        document.getElementById("dataCont").innerHTML=imgDataBW;
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

}, 500);


