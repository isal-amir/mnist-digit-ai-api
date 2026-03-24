const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d")

ctx.fillStyle = "black"
ctx.fillRect(0,0,canvas.width,canvas.height)

let drawing = false

canvas.addEventListener("mousedown", () => drawing = true)
canvas.addEventListener("mouseup", () => drawing = false)

canvas.addEventListener("mousemove", draw)

function draw(e){

if(!drawing) return

ctx.fillStyle = "white"

ctx.beginPath()
ctx.arc(e.offsetX, e.offsetY, 10, 0, Math.PI*2)
ctx.fill()

}

function clearCanvas(){

ctx.fillStyle = "black"
ctx.fillRect(0,0,canvas.width,canvas.height)

}

async function predict(){

const dataURL = canvas.toDataURL()

const response = await fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body: JSON.stringify({
image:dataURL
})

})

const result = await response.json()

document.getElementById("result").innerText =
"Prediction: " + result.prediction

document.getElementById("latency").innerText = 
"Latency: " + (result.latency * 1000).toFixed(2) + " ms"

}