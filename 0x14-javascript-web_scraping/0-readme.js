#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

fs.readFile(`./${argv[2]}`, 'utf-8', (err, data) => {
	if (err) throw err;
	console.log(data);
})
