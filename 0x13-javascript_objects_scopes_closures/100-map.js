#!/usr/bin/node
const List = require('./100-data.js').list;
const newList = List.map((number, index) => number * index);

console.log(List);
console.log(newList);
