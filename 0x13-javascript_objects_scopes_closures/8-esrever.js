#!/usr/bin/node
exports.esrever = function (list) {
  const lReverse = [];
  let i = list.length - 1;
  while (i >= 0) {
    lReverse.push(list[i]);
    i--;
  }
  return lReverse;
};
