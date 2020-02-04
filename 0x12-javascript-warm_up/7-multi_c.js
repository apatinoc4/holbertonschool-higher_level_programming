#!/usr/bin/node
const myvar = process.argv[2];
const myvar2 = 'C is cool';
let i = 0;
if (isNaN(parseInt(myvar))) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(myvar)) {
    console.log(myvar2);
    i++;
  }
}
