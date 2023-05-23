#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = `http://swapi.co/api/films/${filmId}`;

request(url, (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});
