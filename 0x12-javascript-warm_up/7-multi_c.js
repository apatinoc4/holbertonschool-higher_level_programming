#!/usr/bin/node

const n = parseInt(process.argv[2]);
let i = 0;

if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  while (i < n) {
    console.log('C is cool');
    i++;
  }
}
