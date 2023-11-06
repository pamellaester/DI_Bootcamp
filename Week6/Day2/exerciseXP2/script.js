// Exercise 1: Timer
// function sayHello(phrase) {
//     alert(`${phrase}!`);
// }
  
// setTimeout(sayHello, 2000, "Hello World");

// const clearButton = document.getElementById("clear");
// let paragraphCount = 0;
// const intervalId = setInterval(function () {
//     const divElement = document.querySelector("#container")
//     const newP = document.createElement("p");
//     newP.textContent = ("Hello World");
//     divElement.appendChild(newP);
//     paragraphCount++;

//     if (paragraphCount === 5) {
//         clearInterval(intervalId);
//     }
// }, 2000);

// clearButton.addEventListener("click", function () {
//     clearInterval(intervalId);
// });

// Exercise 2 : Move The Box

function myMove() {
    const container = document.getElementById("container");
    const animate = document.getElementById("animate");
    
    let position = 0;
    
    const moveInterval = setInterval(function () {
        position++;
        animate.style.left = position + "px";
        
        // Check if the animation has reached the right end of the container
        if (position + animate.clientWidth >= container.clientWidth) {
            clearInterval(moveInterval);
        }
    }, 1);
}