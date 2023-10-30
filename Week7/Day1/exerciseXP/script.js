// Exercise 1 : Location
// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }

// const {name, location: {country, city, coordinates: [lat, lng]}} = person;

// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

// the output will be everything with the proper value
// I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

// Exercise 2: Display Student Info
// function displayStudentInfo({first, last}){
//     return console.log(`Your full name is ${first} ${last}`)
// }

// displayStudentInfo({first: 'Elie', last:'Schoppik'});

// Exercise 3: User & Id
// const users = { user1: 18273, user2: 92833, user3: 90315 }
// const entry = Object.entries(users)
// console.log(entry)
// output: [["user1", 18273], ["user2", 92833], ["user3", 90315]]

// const result = []
// for (const users of entry) {
//  const [name, id] = users;
//  result.push([name,id * 2]);
// }

// console.log(result)

// Exercise 4 : Person Class
// class Person {
//     constructor(name) {
//       this.name = name;
//     }
//   }
  
//   const member = new Person('John');
//   console.log(typeof member);

//will show up what type "member" is = object

// Exercise 5 : Dog Class
// class Dog {
//     constructor(name) {
//       this.name = name;
//     }
//   };

//   // 2 will successfully extend the Dog class
//   class Labrador extends Dog {
//     constructor(name, size) {
//       super(name);
//       this.size = size;
//     }
//   };

// Exercise 6 : Challenges
// [2] === [2] 
// output:false
// {} === {}
// output:false


// const object1 = { number: 5 }; 
// const object2 = object1; 
// const object3 = object2; 
// const object4 = { number: 5};

// object1.number = 4;
// console.log(object2.number)
// output: 4
// console.log(object3.number)
// output: 4
// console.log(object4.number)
// output: 5

// class animal {
//     constructor(name, type, color) {
//         this.name = name;
//         this.type = type;
//         this.color = color;

//       }
// }

// class mamal extends animal {
//     constructor(name,type, color, noise) {
//         super(name, type, color); 
//         this.noise = noise;}
    
//         sound(noise) {
//             return `${this.noise} I'm ${this.type}, named ${this.name} and I'm ${this.color}.`;
//           }
// }

// const farmerCow = new mamal("Lily", "cow", "brown and white", "moo");
// console.log(farmerCow.sound());
  


