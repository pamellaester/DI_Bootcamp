let people = ["Greg", "Mary", "Devon", "James"];
// people.shift()
// console.log(people)

// people[3] = "Jason"
// console.log(people)

// people.push("Pamella")
// console.log(people)

// let result = people.indexOf("Mary")
// console.log(result)

// let names = people.slice(0,5)
// names.splice(1,1)
// console.log(names)

// let result = people.indexOf("Foo")
// console.log(result)

// const last = people[people.length - 1];
// console.log(last)

// for (let i=0; i<people.length; i++) {
//     console.log(people[i]);
// }

// for (let i = 0; i < people.length; i++) {
//     if(i=== 3){
//         break
//     }
//     console.log(people[i]);
// }

// Exercise 2 : Your Favorite Colors

// let colors = ["red", "yellow", "blue", "black", "white"]
// let suffixes = ["st", "nd", "rd"];

// for (let i = 0 ; i < colors.length; i++) {
//     for (let i = 0; i < colors.length; i++) {
//         let suffix = "th";
      
//         if (i < 3) {
//           suffix = suffixes[i];
//         }
      
//         console.log(`My ${i + 1}${suffix} choice is ${colors[i]}`);
//       }
//     }

// Exercise 3 : Repeat The Question
// let number; {

// do {
//   const user = prompt("Enter a number:");
//   number = parseFloat(user);

//   if (isNaN(number)) {
//     alert("That's not a valid number. Please try again.");
//   }
// } while (isNaN(number) || number >= 10);

// alert("You entered a number less than 10.");
// }

// Exercise 4 : Building Management

// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// console.log(building.numberOfFloors)
// console.log(building.numberOfAptByFloor.firstFloor)
// console.log(building.numberOfAptByFloor.thirdFloor)
// console.log(building.nameOfTenants[1],building.numberOfRoomsAndRent.dan[0])
// const sarahRent = building.numberOfRoomsAndRent.sarah[1];
// const davidRent = building.numberOfRoomsAndRent.david[1];
// const danRent = building.numberOfRoomsAndRent.dan[1];
// if (sarahRent + davidRent > danRent) {
//     console.log("Sum of Sarah's and David's rent is bigger than Dan's rent.");
//     danRent = 1200;
//     console.log("Dan's rent increased to 1200.");
// }


// Exercise 5 : Family

// const family = {
//     name: "Yehudit",
//     city: "Brazil",
//     members: 3,
//     pets: "Dog",
//   };

// for (const key in family) {
//     console.log(key);
// }

// for (const key in family) {
//     console.log(family[key]);
// }

// Exercise 6 : Rudolf

// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
// }

// let sentence = " "
// for (const key in details) {
//     sentence = sentence + " " + key + " " + details[key] 
//     console.log(sentence);
// }

// // Exercise 7 : Secret Group

// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// let acronym = ""

// for (const name of names.sort()) {
//     console.log(name)
//     acronym = acronym + name[0]
// }

//  console.log(acronym)