#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let num = 0;

request(url, (err, _, body) => {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    if (body.results) {
      const results = body.results;
      for (let i = 0; i < results.length; i++) {
        for (let j = 0; j < results[i].characters.length; j++) {
          if (results[i].characters[j].endsWith('/18/')) num++;
        }
      }
    }
    console.log(num);
  }
});
