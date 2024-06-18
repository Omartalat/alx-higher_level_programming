#!/usr/bin/node

const { argv } = require('node:process');

function factorialize (num) {
  if (num < 0) return -1;
  else if (num === 0) return 1;
  else {
    return num * factorialize(num - 1);
  }
}

if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(`${factorialize(Number(argv[2]))}`);
}
