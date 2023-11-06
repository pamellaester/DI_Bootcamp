// Exercise 1 : Scope
// #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// prediction : a = 3 

// #1.1 - run in the console:
// funcOne()
// #1.2 What will happen if the variable is declared 
// with const instead of let ?
// prediction : a = 5
//#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// #2.1 - run in the console:
// funcThree()  prediction : a = 0
// funcTwo() prediction : a = 5
// funcThree() prediction : a =  5
// #2.2 What will happen if the variable is declared 
// with const instead of let ?


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?

// Exercise 2 : Ternary Operator

// function winBattle(){
//     return true;
// }

// const  winBattle = () => true;
// const experiencePoints = winBattle() ? 10 : 1;
// console.log(experiencePoints);

// Exercise 3 : Is It A String ?

// const isString = (value) => typeof value === 'string';
// console.log(isString('Hello'));
// console.log(isString(123));

// Exercise 4 : Find The Sum

// const sum = (x,y) =>  x + y ; 
// console.log(sum(2,9));

// Exercise 5 : Kg And Grams
// function convert (x) {
//     return x * 1000;
//   }
// console.log(convert(2));

// const convert = function (x) {
//     return x * 1000;
//   }
// console.log(convert(2));

// don't need function names

// const convert = (x) =>  x * 1000 ; 
// console.log(convert(2));

// Exercise 6 : Fortune Teller

// (function (numberOfChildren,PartnersName,geographicLocation,jobTitle) {
//     alert(`You will be a ${jobTitle} in ${geographicLocation}, and married to ${PartnersName} with ${numberOfChildren} kids.`);
// })(4,"Jack","Londres","Manager")

// Exercise 7 : Welcome

// (function (userName,profilePicture) {
//    const nav = document.querySelector("nav")
//    const newDiv = document.createElement("div")
//    newDiv.textContent = `User name: ${userName}
//    Profile picture: ${profilePicture}`
//    return nav.append(newDiv)
// })("Maria","flowers")

// Exercise 8 : Juice Bar

function makeJuice (size) {    
    const ingredients = []

    function addIngredients(first,second,third) {           
            ingredients.push(first,second,third)     
    }
   
    function displayJuice() {           
        const sentence = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`
        console.log(sentence); 
    }
    addIngredients("apple","banana","mango");
    addIngredients("grape","lemon","strawberry")
    displayJuice()
}

makeJuice("medium")


