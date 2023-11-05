
const name = "Mike Taylor";

const greeting = function (name) {
  console.log(`Hello ${name}, welcome to NodeJS`);מםגק
};

const hello = (name) => {
  console.log(`hello ${name}`)
}

// module.exports = greeting;


module.exports = {
  greeting,
  hello
}

// const getData = async () => {
//   try {
//     const res = await fetch("")
//     const data = res/JSON();
//     console.log(data)
//   } catch (error) {
//     console.log(error)
//   }
// }

// getData().then(d => console.log(d))