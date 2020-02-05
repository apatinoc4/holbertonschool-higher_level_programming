#!/usr/bin/node

const unique = (value, index, self) => {
    return self.indexOf(value) === index
  }

const n = process.argv;
const n2 = n.slice(2);
const n3 = n2.map(Number);
const n4 = n3.filter(unique);
const n5 = n4.sort();
const n6 = n5[n5.length -2];


if (n.length < 3) {
    console.log(0);
  } else if (n.length === 3){
    console.log(0);
  }
  else {
  console.log(n6);
  }