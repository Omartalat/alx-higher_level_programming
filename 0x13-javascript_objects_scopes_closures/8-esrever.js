#!/usr/bin/node

exports.esrever = function (list) {
  const nlist = [];
  for (let i = 0; i < list.length; i++) {
    nlist[i] = list[list.length - (i + 1)];
  }
  return nlist;
};
