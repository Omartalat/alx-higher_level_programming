#!/usr/bin/node

const { argv } = require('node:process');
let str = '';

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(argv[2]); i++) {
    for (let j = 0; j < Number(argv[2]); j++) {
      str += 'X';
    }
    str += '\n';
  }
  console.log(str.slice(0, -1));
}
