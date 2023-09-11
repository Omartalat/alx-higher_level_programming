#!/usr/bin/node

const args = process.argv.slice(2);
const len = args.length;
if (len === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
