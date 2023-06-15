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

      charactersUrls.forEach(characterUrl => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.error(`An error occurred while making the request: ${error}`);
            return;
          }

          if (response.statusCode !== 200) {
            console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
            return;
          }

          const character = JSON.parse(body);
          console.log(character.name);
        });
      });
    } catch (error) {
      console.error(`An error occurred while parsing the response: ${error}`);
    }
  });
} else {
  console.log('Please provide the Movie ID as an argument.');
}
