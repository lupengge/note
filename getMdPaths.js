const fs = require('fs')
const os = require('os')
const path = require('path')

/**
 * 
 * @param {string} parentDir 入口路径
 * @returns {Array}
 */
function getAllMd(parentDir) {
  let result = []
  if (fs.readdirSync(parentDir).length == 0) {
    return result;
  } else {
    childDirs = fs.readdirSync(parentDir)
    for (let dir of childDirs) {
      if (dir == "node_modules") continue

      let state = fs.lstatSync(path.join(parentDir, dir))
      if (state.isDirectory()) {

        result.push(...(getAllMd(path.join(parentDir, dir))))
      } else if (dir.indexOf(".md") > -1) {
        //判断路径中中是否含有.md
        let parentName = path.basename(parentDir, "");
        result.push({ 
          path: path.join(parentDir, dir), 
          name: dir.substring(0, dir.length - 3), 
          parent: parentName 
        })
      }

    }
    return result;
  }
}

let out = getAllMd(__dirname)
console.log(out);

out = out.sort((a,b)=>{
  return a.parent[0].charCodeAt()-b.parent[0].charCodeAt()
})

let a = "\n";
let lastParentName = "";
for (let i of out) {
  let name = i.name;
  if (lastParentName !== i.parent) {
    a += `### ${i.parent}\n`
    lastParentName = i.parent;
  }
  i.path = i.path.substr(__dirname.length).replace(/\\/g, '/')
  a += `[${name}](${i.path})  \n`
}

// fs.writeFileSync('./res.txt',a)

let content = fs.readFileSync('./README.md', 'utf-8')
content = content.split("<!-- 所有文档 -->")
content[1] = a;

fs.writeFileSync('README.md', content.join('<!-- 所有文档 -->'), { flag: "w+" })

console.log('\33[32;4m更新首页readme成功')

let htmlContent = fs.readFileSync('index.html',{encoding:"utf-8"})

let ex = /paths\: \[(.*)\]\,/gs

let htmlResult= htmlContent.replace( ex,`paths\: \['${out.map(a=>a.path).join("','")}'\]\,`)

fs.writeFileSync('index.html',htmlResult)
console.log('更新首页html成功\x1b[0m')






