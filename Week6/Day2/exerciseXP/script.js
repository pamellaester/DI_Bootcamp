// Exercise 1 : Change The Article

// const h1 = document.querySelector("H1")
// console.log(h1)

// const deleteLastChild = document.querySelector("article")
// const lastParagraph = deleteLastChild.lastElementChild;
// deleteLastChild.removeChild(lastParagraph);

// const h2Element = document.querySelector("h2");
// h2Element.addEventListener("click", function () {
//     h2Element.style.backgroundColor = "red";
// });

// const h3Element = document.querySelector("h3");
// h3Element.addEventListener("click", function () {
//     h3Element.style.display = "none";
// });

// const boldButton = document.getElementById("boldButton");
// const paragraphs = document.querySelectorAll("p");
// boldButton.addEventListener("click", function () {
//     paragraphs.forEach((paragraph) => {
//         paragraph.style.fontWeight = "bold";
//     });
// });

// Exercise 2 : Work With Forms

// const formElement = document.getElementById("myform");
// console.log(formElement);

// const inputfname = document.getElementById("fname");
// const inputlname = document.getElementById("lname");
// console.log(inputfname, inputlname);

// const inputfname = document.getElementsByName("firstname");
// const inputlname = document.getElementsByName("lastname");
// console.log(inputfname, inputlname);

// const submit = formElement.addEventListener("submit", function (event) {
// event.preventDefault();

// const firstNameValue = inputfname.value;
// const lastNameValue = inputlname.value;

// if (firstNameValue && lastNameValue) {
//     const ulElement = document.querySelector(".usersAnswer");
//     const liFirstName = document.createElement("li");
//     ulElement.appendChild(liFirstName);
//     const liLastName = document.createElement("li");
//     ulElement.appendChild(liLastName);

//     liFirstName.textContent = (`First Name: ${firstNameValue}`);
//     liLastName.textContent = (`Last Name: ${lastNameValue}`);
//     inputfname.value = "";
//     inputlname.value = "";
// }
// });

// Exercise 3 : Transform The Sentence

// let allBoldItems;

// function getBoldItems() {
//     const paragraph = document.querySelector("p");
//     allBoldItems = paragraph.querySelectorAll("strong");
//     console.log(allBoldItems)
// }

// getBoldItems()

// function highlight() {
//     allBoldItems.forEach(item => {
//         item.style.color = "blue";
//     });
// }

// highlight()

// function returnItemsToDefault() {
//     allBoldItems.forEach(item => {
// item.style.color = "black"
//     });
// }

// returnItemsToDefault()

// const paragraph = document.querySelector("p");
// paragraph.addEventListener("mouseover", highlight);
// paragraph.addEventListener("mouseout", returnItemsToDefault);

// Exercice 4 : Volume Of A Sphere

// const form = document.getElementById("MyForm");
// const radiusInput = document.getElementById("radius");
// const volumeInput = document.getElementById("volume");

// form.addEventListener("submit", function (e) {
//     e.preventDefault();
//     const radius = parseFloat(radiusInput.value);

//     if (!isNaN(radius) && radius >= 0) {
//         const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
//         volumeInput.value = volume.toFixed(2); // Round to 2 decimal places
//     } else {
//         alert("Please enter a valid positive number for the radius.");
//     }
// });
