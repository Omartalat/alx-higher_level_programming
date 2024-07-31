#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, (err, _, body) => {
  if (err) console.error(err);
  else {
    fs.writeFile(fileName, body, err => {
      if (err) console.error(err);
    });
  }
});
