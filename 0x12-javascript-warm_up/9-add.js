#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log('NaN');
} else {
  console.log(`${add(Number(argv[2]), Number(argv[3]))}`);
}
