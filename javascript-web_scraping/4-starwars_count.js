#!/usr/bin/node

const request = require('request-promise');

// Function to check if Wedge Antilles is present in a movie
function isWedgeAntillesPresent(movie) {
  const wedgeAntillesId = '18';
  return movie.characters.some(characterUrl => characterUrl.includes(wedgeAntillesId));
}

(async () => {
  try {
    // Check if the API URL is provided as an argument
    if (process.argv.length > 2) {
      const apiUrl = process.argv[2];
  
      const response = await request.get(apiUrl);
      const movies = JSON.parse(response).results;
      const moviesWithWedgeAntilles = movies.filter(isWedgeAntillesPresent);
      console.log(moviesWithWedgeAntilles.length);
    } else {
      console.log('Please provide the API URL as an argument.');
    }
  } catch (error) {
    console.error('An error occurred while making the request:', error);
  }
})();
