#!/usr/bin/node

const n = process.argv;
let i = 0;

if (isNaN(n[2])) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(n[2])) {
    console.log('C is cool');
    i++;
  }
}
