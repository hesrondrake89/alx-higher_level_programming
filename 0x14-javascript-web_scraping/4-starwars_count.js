#!/usr/bin/node
const request = require('request');
<<<<<<< HEAD
request(process.argv[2], (error, response, body) => {
 
=======
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
>>>>>>> 62921d7b5aa9fa40277e7929a9657a61cd184c8b
