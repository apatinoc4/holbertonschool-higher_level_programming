#!/usr/bin/node
const myvar = process.argv[2];
if (myvar == null) {
  console.log('No argument');
} else {
  console.log(myvar);
}
