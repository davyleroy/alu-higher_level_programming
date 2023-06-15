#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const apiUrl = process.argv[2];

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
      const tasks = JSON.parse(body);
      const completedTasksByUser = {};

      tasks.forEach(task => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    } catch (error) {
      console.error(`An error occurred while parsing the response: ${error}`);
    }
  });
} else {
  console.log('Please provide the API URL as an argument.');
}
