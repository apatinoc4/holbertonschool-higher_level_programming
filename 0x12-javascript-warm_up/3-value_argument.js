#!/usr/bin/node
const myvar = process.argv[2];
if (myvar == undefined) {
  console.log('No argument');
} else {
  console.log(myvar);
}
