#!/usr/bin/node
const myvar = process.argv[2];
if (isNaN(parseInt(myvar))) {
  console.log('Not a number');
} else {
  console.log(parseInt(myvar));
}
