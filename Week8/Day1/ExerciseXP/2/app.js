// Exercise 2: Advanced Module Usage Using ES6 Module Syntax

import { peopleData } from './data.js';

function calculateAverageAge(peopleData) {
    const totalAges = peopleData.reduce((acc,person) => acc + person.age, 0);
    const averageAge = totalAges / peopleData.length;
    console.log(`The average age of all persons is: ${averageAge.toFixed(2)}`);
}

calculateAverageAge(peopleData);