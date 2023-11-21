// 1rst Daily Challenge

// function makeAllCaps(words) {
//    return  new Promise((resolve, reject) => {
//         if (words.every(isString) ) {
//             resolve(words.map((word) => word.toUpperCase()));
//         } else {
//             reject("All values must be strings");
//         }    
//     })
// };

// function isString(params) {
//     return typeof (params) === "string";
// };

// function sortWords(words) {
//     return  new Promise((resolve, reject) => {
//         if ((words.lengh >= 4)) {
//             resolve(words.sort());
//         } else {
//             reject("Array too short!");
//         }    
//     })
// }; 


// const array = ["maria","silva","carla","monica","livia"]

// makeAllCaps(array)
//     .then((res) => {
//         return sortWords(res);
//     })
//     .then((res) => console.log(res))
//     .catch((err) => console.error(err));

// 2nd Daily Challenge

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`

function toJs() {
    const json = JSON.parse(morse)
    return new Promise((resolve, reject) => {
        if (morse.length === 0) {
            reject("It's empty")
        } else {
            const morseObject = JSON.parse(morse);
            resolve(morseObject)
        }
    });
}

function isWordOkay(word, letters) {
    const userLetters = word.split("");
    return userLetters.every((letter) => !letters.includes(letter))
}

function toMorse(morseJS) {
    const userWord = prompt("Insert a word")
    return new Promise((resolve, reject) => {
        const letters = Object.keys(morseJS);
        if (isWordOkay(word, letters)) {
            reject("pleae type lowercase characters");
        } else {
            resolve(co)
        }
    })
}

toJs()
    .then((morseObject) => toMorse(morseObject))
    .then((res) => console.log(res))
    .catch((err) => console.error(err));
