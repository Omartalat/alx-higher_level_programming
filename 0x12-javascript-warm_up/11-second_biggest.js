#!/usr/bin/node

const argv = process.argv.slice(2).map(Number);

if (argv.length < 2) {
  console.log('0');
} else {
  const num = argv.sort(function (a, b) { return b - a; })[1];
  console.log(num);
}
