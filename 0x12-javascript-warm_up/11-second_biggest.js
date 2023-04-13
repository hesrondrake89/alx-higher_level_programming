#!/usr/bin/node
const length = process.argv.length;
const result = length <= 3 
  ? 0 
  : process.argv
      .slice(2, length)
      .map(Number)
      .sort((a, b) => a - b)[length - 4];
console.log(`The second largest number is ${result}`);
