#!/usr/bin/node

const n = process.argv;
let num = parseInt(n[2]);
if (isNaN(num)) {
  console.log('Missing size');
}
while (num > 0) {
  console.log('X'.repeat(n[2]));
  --num;
}
