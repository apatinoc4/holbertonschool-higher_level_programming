#!/usr/bin/node

const n = process.argv;

if (isNaN(n[2])) {
  console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < parseInt(n[2]); i++) {
    console.log('C is cool');
  }
}
