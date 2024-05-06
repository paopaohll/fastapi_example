'use strict';

var arr = ['小明', '小红', '大军', '阿黄'];

var str = arr.sort().join(', ');

var str2 = `欢迎 ${str} 同学`;
console.log(str2);