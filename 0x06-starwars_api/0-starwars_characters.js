#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(filmUrl, (error, response, body) => {
    if (error || response.StatusCode !== 200) {
      console.error('Error: ', error, '| StatusCode: ', response.statusCode);
    } else {
      const filmData = JSON.parse(body);
      people = filmData.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const p of people) {
      await new Promise(resolve => request(p, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          console.error('Error: ', '| StatusCode: ', response.statusCode);
        } else {
          const filmData = JSON.parse(body);
          names.push(filmData.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of names) {
    if (n === names[names.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

getCharNames();
