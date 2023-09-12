#!/usr/bin/node
const args = process.argv.slice(2);
if (parseInt(args[0], 10)) {
  console.log(parseInt(args[0], 10));
} else {
  console.log('Not a number');
}
