const fs = require("fs");

const input = fs
  .readFileSync("input.txt", "utf-8")
  .split("\n\n")
  .map((x) => x.replace(/\n/g, " ").split(" ").map(y => parseInt(y)))

const reducedInput = input.map(array => array.reduce((a, b) => a + b, 0))

let newArray = []

for (let i = 0; i<3 ; i++) {
  newArray.push(Math.max(...reducedInput))
  reducedInput.splice(reducedInput.indexOf(Math.max(...reducedInput)), 1)
}

console.log("solution 1: " + Math.max(...newArray))
console.log("solution 2: " + newArray.reduce((a,b) => a+b,0));
