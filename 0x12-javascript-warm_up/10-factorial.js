#!/usr/bin/node

const n1 = parseInt(process.argv[2]);

function factorial (a) {
    if (a === 0 || a === 1) {
      return 1;
    }
    return factorial(a - 1) * a;
  }
  if (isNaN(n1)) {
    console.log(1);
  } else {
    console.log(factorial(n1));
  }
