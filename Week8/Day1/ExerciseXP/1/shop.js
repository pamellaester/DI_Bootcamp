// Exercise 1: Multiple Exports And Import Using CommonJS Syntax

const products = require('../products.js');

function Search(name) {
    return products.find(product => product.name.toLowerCase() === name.toLowerCase());
}
    
console.log(Search("laptop"))
console.log(Search("headphones"))