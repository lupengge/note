const fs = require('fs')
var request = require('request');
const fetch = require('node-fetch')
const { Stream } = require('stream')
const http = require('http')
const content='内容'

/**
 * flag可选项
 * r+ 打开文件用于读写。
 * w+ 打开文件用于读写，将流定位到文件的开头。如果文件不存在则创建文件.
 * a 打开文件用于写入，将流定位到文件的末尾。如果文件不存在则创建文件。
 * a+ 打开文件用于读写，将流定位到文件的末尾。如果文件不存在则创建文件。
 */
/**
fs.writeFile(__dirname+'/bin/1.txt',content,(err)=>{
  if(err){
    console.error(err)
    return
  }
})
 */

//创建文件夹
if(!fs.existsSync(__dirname+'/bin')){
  fs.mkdirSync(__dirname+'/bin')
}


let imgSrc='http://127.0.0.1/static/test.png';
/*
//使用fetch下载png图片
fetch('http://127.0.0.1/static/test.png').then(response=>response.blob()).then((blob)=>blob.stream()).then(stream=>{
  const writableStream=fs.createWriteStream(__dirname+'test.png')
  
  stream.pipe(writableStream);
}).catch(a=>console.error(a))

//使用request下载png图片
const writableStream=fs.createWriteStream(__dirname+'/test.png')
request('http://127.0.0.1/static/test.png').pipe(writableStream)


//使用http下载图片
http.get(imgSrc,res=>{
  let imgData="";
  res.setEncoding("binary")
  res.on("data",chunk=>{
    imgData+=chunk;
  })
  res.on('end',()=>{
    if(!fs.existsSync(__dirname+"/httpDownload")){
      fs.mkdirSync(__dirname+"/httpDownload")
    }

    fs.writeFile(__dirname+"/httpDownload/test.png",imgData,"binary",(err)=>{
      if(err){
        console.error(err);
      }else{
        console.log("图片下载成功");
      }
    })
  })
})
*/
console.log("\x1b[33m当前环境参数为：\x1b[0m");
console.log(process.argv.join(" "));

/**打印出颜色 */
console.log('\x1b[33m%s\x1b[0m', '你好')


//创建进度条
const ProgressBar = require('progress')

// const bar = new ProgressBar(':bar', { total: 10 })
// const timer = setInterval(() => {
//   bar.tick()
//   if (bar.complete) {
//     clearInterval(timer)
//   }
// }, 100)

// const inquirer = require('inquirer')

// var questions = [
//   {
//     type: 'input',
//     name: 'name',
//     message: "你叫什么名字?"
//   }
// ]

// inquirer.prompt(questions).then(answers => {
//   console.log(`你好 ${answers['name']}!`)
// })

//打印耗时
const doSomething = () => console.log('正在执行一段程序...')
const measureDoingSomething = () => {
  console.time('程序耗时')
  //做点事，并测量所需的时间。
  doSomething()
  console.timeEnd('程序耗时')
}
measureDoingSomething()