#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (number) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
