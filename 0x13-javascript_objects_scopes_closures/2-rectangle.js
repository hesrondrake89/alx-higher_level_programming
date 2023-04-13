#!/usr/bin/node
class Rectangle {
  constructor(width, height) {
    if (width > 0 && height > 0) {
      [this.width, this.height] = [width, height];
    }
  }
}

module.exports = Rectangle;
