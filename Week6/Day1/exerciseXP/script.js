// Exercise 1 : Find The Numbers Divisible By 23
// function displayNumbersDivisible(divisor = 23)  {
//     let sum = 0

//     for (let i = 0; i <= 500; i++) {
//         if (i % divisor === 2) {
//             console.log(i)
//             sum += i
//         }
//     }
//     console.log(`Sum: ${sum}`)
// }

// displayNumbersDivisible();
// displayNumbersDivisible(3);
// displayNumbersDivisible(45);

// Exercise 2 : Shopping List

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// const shoppingList = ['banana', 'orange', 'apple']

// function myBill() {
//     let totalBill = 0;
    
//     for (const item of shoppingList) {
//         if (stock.hasOwnProperty(item) && stock[item] > 0) {
//             totalBill += prices[item];
//             stock[item] --;
//         }
//     }
//     return totalBill     
// }

// const totalCost = myBill();
// console.log(`Total cost: ${totalCost}`)

// Exercise 3 : What’s In My Wallet ?
// function changeEnough(itemPrice, amountOfChange){

// }

// Exercise 4 : Vacations Costs
// function hotelCost() {
//     let userNumberOfNights;
//     do {
//         userNumberOfNights = prompt("How many night would you like to stay in the hotel?");
//         userNumberOfNights = parseInt(userNumberOfNights);
//         if (isNaN(userNumberOfNights)) {
//             alert("Please enter a valid number for the number of nights.");
//         }
//     } while (isNaN(userNumberOfNights)); 

//     const costPerNight = 140;
//     const sum = userNumberOfNights * costPerNight; 
//     return sum
// }


// const totalHotelCost = hotelCost();
// console.log("Total hotel cost: $" + totalHotelCost.toFixed(2));

// function planeRideCost() {  
//  let userDestination;
//     while (true) {
//         userDestination = prompt("What's your next detination?");

//     if (userDestination === null || userDestination.trim() === "") {
//         alert("Please enter a valid destination for the plane ride cost.")
//     } else {
//         const normalizedDestination = userDestination.toLowerCase();
        
//         let cost;
//         if (normalizedDestination === "london") {
//             cost = 183;
//         } else if 
//             (normalizedDestination === "paris") {
//                 cost = 220;
//             } else {
//             cost = 300
//         }

//         return cost
//         }
//     }
// }

// const travelCost = planeRideCost();
// console.log("Your plane ride cost: $" + travelCost);

// function rentalCarCost() {

// }

// Exercise 5 : Users

// const retriveDIV = document.getElementById("container");
// console.log(retriveDIV);

// const myList = document.querySelector(".list");
// myList.lastElementChild.innerText = "Richard" 
// console.log(myList.textContent);

// const myList = document.querySelectorAll(".list")
// delete myList 



// Exercise 6 : Change The Navbar

// Exercise 7 : My Book List



class Rabbit {
    constructor(type) {
        this.type = type;
    }
    speak(line) {
        console.log(`The ${this.type} rabbit says '${line}'`);
    }
}
let killerRabbit = new Rabbit("killer");
console.log(killerRabbit.speak("I'm gonna kill u"))
let blackRabbit = new Rabbit("black");
console.log(blackRabbit.speak("Hey, bro!!"))

