// Exercise 1 : Comparison

// function compareToTen(num) {

//     return new Promise((resolve, reject) => {
//         if (num <= 10) {
//             resolve(`Number ${num} is smaller then 10.` );
//         } else {
//             reject(`Number ${num} is greater than 10.`);
//         }
//     });
// }

// compareToTen(15)
//   .then(result => console.log(result))
//   .catch(error => console.log(error))

// compareToTen(8)
// .then(result => console.log(result))
// .catch(error => console.log(error))

// Exercise 2 : Promises

// let string = true;

// let resolvesItself = new Promise(function (resolve, reject) {
//     setTimeout(resolve("sucess"), 4000);
// });

// resolvesItself.then(console.log).catch(console.error);

// Exercise 3 : Resolve & Reject

// Promise.resolve("3").then(console.log)

// Promise.reject("Booo").catch(console.log)
