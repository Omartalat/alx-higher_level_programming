#!/usr/bin/node

const SquareParent = require('./5-square');

module.exports = class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += c;
      }
      console.log(str);
    }
  }
};
