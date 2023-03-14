#!/usr/bin/node

class Square extends require('./5-square.js') {
  charprint (c) {
    if (!c) {
      c = 'x';
    }
    
    const charArray = [];
    
    for (let i = 0; i < this.width; i++) {
      charArray.push(c.repeat(this.width));
    }
    
    console.log(charArray.join('\n'));
  }
}
