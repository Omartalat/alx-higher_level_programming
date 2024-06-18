#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2]) {
  if (argv[3]) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
