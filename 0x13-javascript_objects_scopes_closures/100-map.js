#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map(function (num, index) {
  return num * index;
});


consoe.log(list);
console.log(newList);
