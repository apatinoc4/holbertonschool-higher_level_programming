#!/usr/bin/node
const request = require('request');

request.get('http://swapi.co/api/films/' + process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});