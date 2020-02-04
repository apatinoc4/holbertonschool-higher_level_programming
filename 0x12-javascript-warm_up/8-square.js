#!/usr/bin/node
const myvar = process.argv[2];
let i, j;
if (isNaN(parseInt(myvar))) {
  console.log('Missing size');
} else {
  for (i = 0; i < parseInt(myvar); i++) {
    for (j = 0; j < parseInt(myvar); j++) {
      console.log('X');
    }
    console.log('');
  }
}
