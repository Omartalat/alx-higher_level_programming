#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const apiURL = url + movieID;

request(apiURL, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
