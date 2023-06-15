#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`An error occurred while making the request: ${error}`);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
      return;
    }

    try {
      const movie = JSON.parse(body);
      const charactersUrls = movie.characters;

      const printCharacters = (urls, index = 0) => {
        if (index >= urls.length) {
          return;
        }

        request.get(urls[index], (error, response, body) => {
          if (error) {
            console.error(`An error occurred while making the request: ${error}`);
          } else if (response.statusCode !== 200) {
            console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }

          printCharacters(urls, index + 1);
        });
      };

      printCharacters(charactersUrls);
    } catch (error) {
      console.error(`An error occurred while parsing the response: ${error}`);
    }
  });
} else {
  console.log('Please provide the Movie ID as an argument.');
}
