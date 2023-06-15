#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const json = JSON.parse(body);
    const results = json.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const chars = (results[i].characters);
      for (let j = 0; j < chars.length; j++) {
        const check = chars[j].endsWith('18/');
        if (check) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
