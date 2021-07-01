const fs = require('fs')
const os = require('os')
const path = require('path')


function getAllMd(parentDir){
  let result=[]
  if(fs.readdirSync(parentDir).length==0){
    return result;
  }else{
    childDirs = fs.readdirSync(parentDir)
    for(let dir of childDirs){
      if(dir=="node_modules")continue

      let state=fs.lstatSync(path.join(parentDir,dir))
      if(state.isDirectory()){
        
        result.push(...(getAllMd(path.join(parentDir,dir))))
      }else if(dir.indexOf(".md")>-1){
        //判断路径中中是否含有.md
        result.push({path:path.join(parentDir,dir),name:dir.substring(0,dir.length-3)})
        
      }
      
    }
    return result;
  }
}
let out = getAllMd(__dirname)
let a="";
for(let i of out){
  a+=`[${i.name}](${i.path})\n`
}

fs.writeFileSync('./res1.txt',a)



