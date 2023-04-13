#!/usr/bin/node

module.exports = class Rectangle {
  constructor (weight, height) {
    if (weight > 0 && height > 0) { [w, h] = [this.width, this.height]; }
  }
};
