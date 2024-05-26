const fs = require('fs');
const readline = require('readline');

// 创建一个指向 'paper.txt' 的可读流
const fileStream = fs.createReadStream('paper.txt');

// 使用 readline 模块和文件流创建一个接口
const rl = readline.createInterface({
  input: fileStream,
  crlfDelay: Infinity // 支持任何换行符
});

// 监听 'line' 事件，每读取一行就打印出来
rl.on('line', (line) => {
  console.log(line);
});

// 监听 'close' 事件，当文件读取完成时触发
rl.on('close', () => {
  console.log('文件读取完成。');
});
