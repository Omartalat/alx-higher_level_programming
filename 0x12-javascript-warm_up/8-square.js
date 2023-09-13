#!/usr/bin/node
const args = process.argv.slice(2);
let str = '';
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    for (let j = 0; j < args[0]; j++) {
      str += 'X';
    }
    str += '\n';
  }
  console.log(str.slice(0, -1));
}
