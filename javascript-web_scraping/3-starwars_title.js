#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`An error occurred while making the request: ${error}`);
    } else if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    } else {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  });
} else {
  console.log('Please provide the movie ID as an argument.');
}
