#!/usr/bin/node

const a = parseInt(process.argv[2]);
if (Number.isNaN(a)) {
  console.log('Not a number');
} else {
  console.log(a);
}
