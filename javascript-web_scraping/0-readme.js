#!/usr/bin/node
const fs = require('fs');

function readFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(`An error occurred while reading the file: ${err}`);
    } else {
      console.log(data);
    }
  });
}

// Check if the file path is provided as an argument
if (process.argv.length > 2) {
  const filePath = process.argv[2];
  readFile(filePath);
} else {
  console.log('Please provide the file path as an argument.');
}
