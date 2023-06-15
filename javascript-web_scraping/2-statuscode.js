#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request.get(url, (error, response) => {
    if (error) {
      console.error(`An error occurred while making the request: ${error}`);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
} else {
  console.log('provide the URL as an argument.');
}
