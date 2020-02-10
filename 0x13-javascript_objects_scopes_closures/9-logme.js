#!/usr/bin/node
const console = require('console');
let counting = 0;
exports.logMe = function (item) {
  console.log(`${counting++}: ${item}`);
};
