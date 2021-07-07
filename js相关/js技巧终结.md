## 给函数参数设置默认值

```javascript
//使用Object.assign()方法
const DEFAULTS = {
  logLevel: 0,
  outputFormat: 'html'
};

function processContent(options) {
  options = Object.assign({}, DEFAULTS, options);
  console.log(options);
  // ...
}

//参数解构赋值，结合es6中的函数参数设置默认值
function fetch(url, { body = '', method = 'GET', headers = {} }={}) {
  console.log(method);
}
```

## 属性的可枚举性

es5中for...in循环、Object.keys()、JSON.stringfy()会忽略descriptor中enumerable属性为false的属性，es6新增一个Object.assign()也会忽略

```javascript
//给对象添加一个不会被循环到的属性
Object.defineProperty(a,"z",{	
	"value":3,
    enumerable:false,
    writeable:true,
    configurable:true
})
```

## Null传导运算符

```javascript
//之前要读取message.body.user.firstName的安全写法
const firstName = (message
  && message.body
  && message.body.user
  && message.body.user.firstName) || 'default';
//使用null传导运算符(?.),
const firstName = message?.body?.user?.firstName || 'default';
//上面的三个?.只要有一个返回null或underfined就不会再往下运算，而是返回underfined


/* 四种写法
obj?.prop // 读取对象属性
obj?.[expr] // 同上
func?.(...args) // 函数或对象方法的调用
new C?.(...args) // 构造函数的调用
*/

    
```

## 自定义类的迭代运算方法

```javaScript
class Collection {
  *[Symbol.iterator]() {
    let i = 0;
    while(this[i] !== undefined) {
      yield this[i];
      ++i;
    }
  }
}

let myCollection = new Collection();
myCollection[0] = 1;
myCollection[1] = 2;
for(let value of myCollection) {
  console.log(value);
}
// 1
// 2
let b=[...myCollection] // [1,2]
```

## 通过proxy监听对象

```javascript
var obj = new Proxy(a, {
  get: function (target, key, receiver) {
    console.log(`getting ${key}!`);
    return Reflect.get(target, key, receiver);
  },
  set: function (target, key, value, receiver) {
    console.log(`setting ${key}!`);
    return Reflect.set(target, key, value, receiver);
  }
});

//其中a为被代理的对象

//get 函数中target就是指被代理的m对象，，receiver指这个代理对象
```

