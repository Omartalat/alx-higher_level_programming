#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const results = {};

request(url, (err, _, body) => {
  if (err) console.error(err);
  else {
    body = JSON.parse(body);
    for (let i = 0; i < body.length; i++) {
      if (body[i].completed === true) {
        if (results[body[i].userId] === undefined) results[body[i].userId] = 1;
        else results[body[i].userId]++;
      }
    }
    console.log(results);
  }
});
