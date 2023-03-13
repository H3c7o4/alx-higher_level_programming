#!/usr/bin/node

const word = 'C is fun';
let x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (x) {
    console.log(word);
    x--;
  }
}
