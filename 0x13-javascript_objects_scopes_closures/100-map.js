<<<<<<< HEAD
#!/usr/bin/node
const initList = require('./100-data.js').list;
const newList = initList.map((number, index) => number * index);

console.log(initList);
console.log(newList);
=======
#!/usr/bin/node
const List = require('./100-data.js').list;
const newList = List.map((number, index) => number * index);

console.log(List);
console.log(newList);
>>>>>>> 033f9dd759c67b1a6835f9a8f0346250603c1538
