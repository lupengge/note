[原文]([ES2015 •巴别尔·德维尔·德维尔·德维尔·德金 (docschina.org)](https://babel.docschina.org/docs/en/learn.html))

> > ### 埃斯6费图雷斯
> >
> > 这份文件最初取自卢克·霍班的优秀[es6功能](https://git.io/es6features)回购。去给它一个明星在吉特胡布！
>
> > #### 雷普尔
> >
> > 请务必尝试这些功能在在线[REPL。](/repl)
>
> [](#introduction)介绍
> -------------------
>
> > ECMAScript 2015 是 2015 年 6 月批准的 ECMAScript 标准。
>
> ES2015 是该语言的重大更新，也是自 ES5 于 2009 年标准化以来对该语言的第一次重大更新。这些功能在主要的JavaScript发动机中正在[实施](https://kangax.github.io/es5-compat-table/es6/)。
>
> 有关[ECMAScript 2015](http://www.ecma-international.org/ecma-262/6.0/index.html)语言的完整规范，请参阅 ES2015 标准。
>
> [](#ecmascript-2015-features)ECMA脚本 2015 功能
> -------------------------------------------
>
> ### [](#arrows-and-lexical-this)箭和词汇这
>
> 箭头是使用语法的函数速记。它们在语法上类似于 C#、Java 8 和咖啡脚本中的相关功能。他们支持表达和陈述机构。与函数不同，箭头与周围代码共享相同的词汇。如果箭头位于其他函数内，则它共享其父函数的"参数"变量。`=>``this`
>
>     // Expression bodies
>     var odds = evens.map(v => v + 1);
>     var nums = evens.map((v, i) => v + i);
>     
>     // Statement bodies
>     nums.forEach(v => {
>       if (v % 5 === 0)
>         fives.push(v);
>     });
>     
>     // Lexical this
>     var bob = {
>       _name: "Bob",
>       _friends: [],
>       printFriends() {
>         this._friends.forEach(f =>
>           console.log(this._name + " knows " + f));
>       }
>     };
>     
>     // Lexical arguments
>     function square() {
>       let example = () => {
>         let numbers = [];
>         for (let number of arguments) {
>           numbers.push(number * number);
>         }
>     
>         return numbers;
>       };
>     
>       return example();
>     }
>     
>     square(2, 4, 7.5, 8, 11.5, 21); // returns: [4, 16, 56.25, 64, 132.25, 441]
>
>
> ### [](#classes)类
>
> ES2015 类是基于原型的 OO 模式的句法糖。单一方便的声明形式使类模式更易于使用，并鼓励互操作性。类支持基于原型的继承、超级呼叫、实例和静态方法以及构造器。
>
>     class SkinnedMesh extends THREE.Mesh {
>       constructor(geometry, materials) {
>         super(geometry, materials);
>     
>         this.idMatrix = SkinnedMesh.defaultMatrix();
>         this.bones = [];
>         this.boneMatrices = [];
>         //...
>       }
>       update(camera) {
>         //...
>         super.update();
>       }
>       static defaultMatrix() {
>         return new THREE.Matrix4();
>       }
>     }
>
>
> ### [](#enhanced-object-literals)增强对象字体
>
> 对象字面扩展，以支持在构造中设置原型、分配速记、定义方法和进行超级呼叫。这些也使对象字面和类声明更加紧密地结合在一起，并让基于对象的设计受益于一些相同的便利性。`foo: foo`
>
>     var obj = {
>         // Sets the prototype. "__proto__" or '__proto__' would also work.
>         __proto__: theProtoObj,
>         // Computed property name does not set prototype or trigger early error for
>         // duplicate __proto__ properties.
>         ['__proto__']: somethingElse,
>         // Shorthand for ‘handler: handler’
>         handler,
>         // Methods
>         toString() {
>          // Super calls
>          return "d " + super.toString();
>         },
>         // Computed (dynamic) property names
>         [ "prop_" + (() => 42)() ]: 42
>     };
>
>
> > 该属性需要原生支持，并在以前的 ECMAScript 版本中被弃用。大多数发动机现在支持该属性，但[有些不](https://kangax.github.io/compat-table/es6/#__proto___in_object_literals)支持。此外，请注意，只有[Web 浏览器](http://www.ecma-international.org/ecma-262/6.0/index.html#sec-additional-ecmascript-features-for-web-browsers)才能实现它，因为它在[附件 B 中](http://www.ecma-international.org/ecma-262/6.0/index.html#sec-object.prototype.__proto__)。它可在节点中找到。`__proto__`
>
> ### [](#template-strings)模板字符串
>
> 模板字符串为构建字符串提供语法糖。这类似于佩尔、Python 等的字符串插值功能。可选地添加标签，以便自定义字符串结构，避免注资攻击或从字符串内容构建更高级的数据结构。
>
>     // Basic literal string creation
>     `This is a pretty little template string.`
>     
>     // Multiline strings
>     `In ES5 this is
>      not legal.`
>     
>     // Interpolate variable bindings
>     var name = "Bob", time = "today";
>     `Hello ${name}, how are you ${time}?`
>     
>     // Unescaped template strings
>     String.raw`In ES5 "\n" is a line-feed.`
>     
>     // Construct an HTTP request prefix is used to interpret the replacements and construction
>     GET`http://foo.org/bar?a=${a}&b=${b}
>         Content-Type: application/json
>         X-Credentials: ${credentials}
>         { "foo": ${foo},
>           "bar": ${bar}}`(myOnReadyStateChangeHandler);
>
>
> ### [](#destructuring)破坏
>
> 构造允许使用模式匹配绑定，并支持匹配的阵列和对象。损毁是故障软的，类似于标准对象查找，未找到时产生值。`foo["bar"]``undefined`
>
>     // list matching
>     var [a, ,b] = [1,2,3];
>     a === 1;
>     b === 3;
>     
>     // object matching
>     var { op: a, lhs: { op: b }, rhs: c }
>            = getASTNode()
>     
>     // object matching shorthand
>     // binds `op`, `lhs` and `rhs` in scope
>     var {op, lhs, rhs} = getASTNode()
>     
>     // Can be used in parameter position
>     function g({name: x}) {
>       console.log(x);
>     }
>     g({name: 5})
>     
>     // Fail-soft destructuring
>     var [a] = [];
>     a === undefined;
>     
>     // Fail-soft destructuring with defaults
>     var [a = 1] = [];
>     a === 1;
>     
>     // Destructuring + defaults arguments
>     function r({x, y, w = 10, h = 10}) {
>       return x + y + w + h;
>     }
>     r({x:1, y:2}) === 23
>
>
> ### [](#default--rest--spread)默认+休息+点差
>
> 受卡的默认参数值。在函数调用中将数组转换为连续参数。将尾随参数绑定到数组。休息取代了对常见病例的需求，并更直接地处理常见病例。`arguments`
>
>     function f(x, y=12) {
>       // y is 12 if not passed (or passed as undefined)
>       return x + y;
>     }
>     f(3) == 15
>
>
>     function f(x, ...y) {
>       // y is an Array
>       return x * y.length;
>     }
>     f(3, "hello", true) == 6
>
>
>     function f(x, y, z) {
>       return x + y + z;
>     }
>     // Pass each elem of array as argument
>     f(...[1,2,3]) == 6
>
>
> ### [](#let--const)让+康斯特
>
> 块范围绑定结构。 是新的。 是单一分配。静态限制可防止在分配前使用。`let``var``const`
>
>     function f() {
>       {
>         let x;
>         {
>           // this is ok since it's a block scoped name
>           const x = "sneaky";
>           // error, was just defined with `const` above
>           x = "foo";
>         }
>         // this is ok since it was declared with `let`
>         x = "bar";
>         // error, already declared above in this block
>         let x = "inner";
>       }
>     }
>
>
> ### [](#iterators--forof)行程+为。之
>
> 迭代对象启用自定义迭代，如 CLR 可识别或爪哇迭代。概括为基于迭代器的迭代。不需要实现一个阵列，启用像LINQ这样的懒惰设计模式。`for..in``for..of`
>
>     let fibonacci = {
>       [Symbol.iterator]() {
>         let pre = 0, cur = 1;
>         return {
>           next() {
>             [pre, cur] = [cur, pre + cur];
>             return { done: false, value: cur }
>           }
>         }
>       }
>     }
>     
>     for (var n of fibonacci) {
>       // truncate the sequence at 1000
>       if (n > 1000)
>         break;
>       console.log(n);
>     }
>
>
> 迭代基于这些鸭型接口（仅使用[TypeScript](https://www.typescriptlang.org/)类型语法进行阐述）：
>
>     interface IteratorResult {
>       done: boolean;
>       value: any;
>     }
>     interface Iterator {
>       next(): IteratorResult;
>     }
>     interface Iterable {
>       [Symbol.iterator](): Iterator
>     }
>
>
> > #### 通过聚填充支持
> >
> > 为了使用传路器，你必须包括巴别[多填充](/docs/usage/polyfill)物。
>
> ### [](#generators)发电机
>
> 发电机简化了使用和.宣布为函数\*的函数返回生成器实例。发电机是转速器的子类型，包括附加和。这些使值能够流回生成器，返回值（或投掷）的表达形式也是如此。`function*``yield``next``throw``yield`
>
> 注意：还可用于启用"等待"式的同步编程，另见ES7[建议](https://github.com/lukehoban/ecmascript-asyncawait)。`await`
>
>     var fibonacci = {
>       [Symbol.iterator]: function*() {
>         var pre = 0, cur = 1;
>         for (;;) {
>           var temp = pre;
>           pre = cur;
>           cur += temp;
>           yield cur;
>         }
>       }
>     }
>     
>     for (var n of fibonacci) {
>       // truncate the sequence at 1000
>       if (n > 1000)
>         break;
>       console.log(n);
>     }
>
>
> 生成器接口是（仅使用[类型脚本](https://www.typescriptlang.org/)类型语法进行阐述）：
>
>     interface Generator extends Iterator {
>         next(value?: any): IteratorResult;
>         throw(exception: any);
>     }
>
>
> > #### 通过聚填充支持
> >
> > 为了使用发电机，你必须包括巴别[多填充](/docs/usage/polyfill)物。
>
> ### [](#comprehensions)理解
>
> 在巴别6.0中删除
>
> ### [](#unicode)统一码
>
> 支持完整 Unicode 的非突破性添加，包括字符串中的新单码字面形式和处理代码点的新 RegExp 模式，以及在 21 位代码点级别处理字符串的新 API。这些新增服务支持在 JavaScript 中构建全球应用。`u`
>
>     // same as ES5.1
>     "𠮷".length == 2
>     
>     // new RegExp behaviour, opt-in ‘u’
>     "𠮷".match(/./u)[0].length == 2
>     
>     // new form
>     "\u{20BB7}" == "𠮷"
>     "𠮷" == "\uD842\uDFB7"
>     
>     // new String ops
>     "𠮷".codePointAt(0) == 0x20BB7
>     
>     // for-of iterates code points
>     for(var c of "𠮷") {
>       console.log(c);
>     }
>
>
> ### [](#modules)模块
>
> 组件定义模块的语言级支持。从流行的 JavaScript 模块加载器 （AMD， 共同JS） 编码模式。主机定义的默认加载器定义的运行时间行为。隐式非同步模型-在请求的模块可用并处理之前，不会执行代码。
>
>     // lib/math.js
>     export function sum(x, y) {
>       return x + y;
>     }
>     export var pi = 3.141593;
>
>
>     // app.js
>     import * as math from "lib/math";
>     console.log("2π = " + math.sum(math.pi, math.pi));
>
>
>     // otherApp.js
>     import {sum, pi} from "lib/math";
>     console.log("2π = " + sum(pi, pi));
>
>
> 其他一些功能包括：`export default``export *`
>
>     // lib/mathplusplus.js
>     export * from "lib/math";
>     export var e = 2.71828182846;
>     export default function(x) {
>         return Math.exp(x);
>     }
>
>
>     // app.js
>     import exp, {pi, e} from "lib/mathplusplus";
>     console.log("e^π = " + exp(pi));
>
>
> > #### 模块格式设置器
> >
> > Babel 可以将 ES2015 模块转换为多种不同的格式，包括通用.js、AMD、系统和 UMD。你甚至可以创建自己的。有关详细信息，请参阅[模块文档](/docs/plugins/)。
>
> ### [](#module-loaders)模块加载器
>
> > #### 不是ES2015的一部分
> >
> > 这在 ECMAScript 2015 规范中作为实施定义。最终的标准将在 WHATWG 的[装载机规范](https://whatwg.github.io/loader/)中，但目前这项工作正在进行中。以下是之前的 ES2015 草案。
>
> 模块装载机支持：
>
> *   动态加载
> *   国家隔离
> *   全球名称空间隔离
> *   编译钩
> *   嵌套虚拟化
>
> 可以配置默认模块加载器，并可以构建新的加载器，以便在孤立或受约束的上下文中评估和加载代码。
>
>     // Dynamic loading – ‘System’ is default loader
>     System.import("lib/math").then(function(m) {
>       alert("2π = " + m.sum(m.pi, m.pi));
>     });
>     
>     // Create execution sandboxes – new Loaders
>     var loader = new Loader({
>       global: fixup(window) // replace ‘console.log’
>     });
>     loader.eval("console.log(\"hello world!\");");
>     
>     // Directly manipulate module cache
>     System.get("jquery");
>     System.set("jquery", Module({$: $})); // WARNING: not yet finalized
>
>
> > #### 需要额外的聚填充物
> >
> > 由于巴别默认使用普通.js模块，因此不包括模块装载机 API 的聚填充物。到[这里](https://github.com/ModuleLoader/es6-module-loader)来。
>
> > #### 使用模块加载器
> >
> > 要使用此，您需要告诉巴别使用模块格式化器。也一定要检查出[系统.js](https://github.com/systemjs/systemjs)`system`
>
> ### [](#map--set--weakmap--weakset)地图+设置+弱地图+弱集
>
> 用于常见算法的有效数据结构。弱图提供无泄漏对象键侧桌。
>
>     // Sets
>     var s = new Set();
>     s.add("hello").add("goodbye").add("hello");
>     s.size === 2;
>     s.has("hello") === true;
>     
>     // Maps
>     var m = new Map();
>     m.set("hello", 42);
>     m.set(s, 34);
>     m.get(s) == 34;
>     
>     // Weak Maps
>     var wm = new WeakMap();
>     wm.set(s, { extra: 42 });
>     wm.size === undefined
>     
>     // Weak Sets
>     var ws = new WeakSet();
>     ws.add({ data: 42 });
>     // Because the added object has no other references, it will not be held in the set
>
>
> > #### 通过聚填充支持
> >
> > 为了支持地图，集，弱地图，和弱集在所有环境中，你必须包括巴别[多填充](/docs/usage/polyfill)。
>
> ### [](#proxies)代理
>
> 代理允许创建具有托管对象可用的全系列行为的对象。可用于拦截、对象虚拟化、记录/分析等。
>
>     // Proxying a normal object
>     var target = {};
>     var handler = {
>       get: function (receiver, name) {
>         return `Hello, ${name}!`;
>       }
>     };
>     
>     var p = new Proxy(target, handler);
>     p.world === "Hello, world!";
>
>
>     // Proxying a function object
>     var target = function () { return "I am the target"; };
>     var handler = {
>       apply: function (receiver, ...args) {
>         return "I am the proxy";
>       }
>     };
>     
>     var p = new Proxy(target, handler);
>     p() === "I am the proxy";
>
>
> 所有运行时级元操作都可用陷阱：
>
>     var handler =
>     {
>       // target.prop
>       get: ...,
>       // target.prop = value
>       set: ...,
>       // 'prop' in target
>       has: ...,
>       // delete target.prop
>       deleteProperty: ...,
>       // target(...args)
>       apply: ...,
>       // new target(...args)
>       construct: ...,
>       // Object.getOwnPropertyDescriptor(target, 'prop')
>       getOwnPropertyDescriptor: ...,
>       // Object.defineProperty(target, 'prop', descriptor)
>       defineProperty: ...,
>       // Object.getPrototypeOf(target), Reflect.getPrototypeOf(target),
>       // target.__proto__, object.isPrototypeOf(target), object instanceof target
>       getPrototypeOf: ...,
>       // Object.setPrototypeOf(target), Reflect.setPrototypeOf(target)
>       setPrototypeOf: ...,
>       // for (let i in target) {}
>       enumerate: ...,
>       // Object.keys(target)
>       ownKeys: ...,
>       // Object.preventExtensions(target)
>       preventExtensions: ...,
>       // Object.isExtensible(target)
>       isExtensible :...
>     }
>
>
> > #### 无支持功能
> >
> > 由于 ES5 的限制，代理不能转皮或多填充。请参阅[各种 JavaScript 引擎](https://kangax.github.io/compat-table/es6/#test-Proxy)的支持。
>
> ### [](#symbols)符号
>
> 符号启用对象状态的访问控制。符号允许属性按键键（如ES5）或。符号是一种新的原始类型。调试中使用的可选参数 - 但不是标识的一部分。符号是独一无二的（如基因），但不是私人的，因为它们通过反射功能（如） 暴露出来。`string``symbol``name``Object.getOwnPropertySymbols`
>
>     (function() {
>     
>       // module scoped symbol
>       var key = Symbol("key");
>     
>       function MyClass(privateData) {
>         this[key] = privateData;
>       }
>     
>       MyClass.prototype = {
>         doStuff: function() {
>           ... this[key] ...
>         }
>       };
>     
>       // Limited support from Babel, full support requires native implementation.
>       typeof key === "symbol"
>     })();
>     
>     var c = new MyClass("hello")
>     c["key"] === undefined
>
>
> > #### 通过聚填充提供有限支持
> >
> > 有限的支持需要巴别[多填充](/docs/usage/polyfill)物。由于语言限制，某些功能无法转溢或填充。有关详细信息，请参阅核心.js[的警告部分](https://github.com/zloirock/core-js#caveats-when-using-symbol-polyfill)。
>
> ### [](#subclassable-built-ins)子机密内置
>
> 在 ES2015 中，内置的（如）和 DOM 可以子分类。`Array``Date``Element`
>
>     // User code of Array subclass
>     class MyArray extends Array {
>         constructor(...args) { super(...args); }
>     }
>     
>     var arr = new MyArray();
>     arr[1] = 12;
>     arr.length == 2
>
>
> > #### 部分支持
> >
> > 内置子机密性应逐案评估，因为此类类别**可以**分门别类，而许多类别（如**）不能由于**ES5 发动机的限制。`HTMLElement``Date``Array``Error`
>
> ### [](#math--number--string--object-apis)数学+数字+字符串+对象API
>
> 许多新的库新增，包括核心数学库、阵列转换助手和对象.分配以供复制。
>
>     Number.EPSILON
>     Number.isInteger(Infinity) // false
>     Number.isNaN("NaN") // false
>     
>     Math.acosh(3) // 1.762747174039086
>     Math.hypot(3, 4) // 5
>     Math.imul(Math.pow(2, 32) - 1, Math.pow(2, 32) - 2) // 2
>     
>     "abcde".includes("cd") // true
>     "abc".repeat(3) // "abcabcabc"
>     
>     Array.from(document.querySelectorAll("*")) // Returns a real Array
>     Array.of(1, 2, 3) // Similar to new Array(...), but without special one-arg behavior
>     [0, 0, 0].fill(7, 1) // [0,7,7]
>     [1,2,3].findIndex(x => x == 2) // 1
>     ["a", "b", "c"].entries() // iterator [0, "a"], [1,"b"], [2,"c"]
>     ["a", "b", "c"].keys() // iterator 0, 1, 2
>     ["a", "b", "c"].values() // iterator "a", "b", "c"
>     
>     Object.assign(Point, { origin: new Point(0,0) })
>
>
> > #### 来自聚填充物的有限支持
> >
> > 这些 API 大多由巴别[聚填区](/docs/usage/polyfill)支持。但是，由于各种原因（例如， 需要大量的额外代码来支持）。你可以[在这里](https://github.com/addyosmani/es6-tools#polyfills)找到更多的聚填充物。`String.prototype.normalize`
>
> ### [](#binary-and-octal-literals)二进制和八角字形
>
> 为二进制 （） 和八角形 （） 添加了两个新的数字字体形式。`b``o`
>
>     0b111110111 === 503 // true
>     0o767 === 503 // true
>
>
> > #### 仅支持字面形式
> >
> > 巴别只能改变，不能。`0o767``Number("0o767")`
>
> ### [](#promises)承诺
>
> 承诺是异步编程的图书馆。承诺是未来可能提供的价值的一流代表。承诺用于许多现有的 JavaScript 库。
>
>     function timeout(duration = 0) {
>         return new Promise((resolve, reject) => {
>             setTimeout(resolve, duration);
>         })
>     }
>     
>     var p = timeout(1000).then(() => {
>         return timeout(2000);
>     }).then(() => {
>         throw new Error("hmm");
>     }).catch(err => {
>         return Promise.all([timeout(100), timeout(200)]);
>     })
>
>
> > #### 通过聚填充支持
> >
> > 为了支持承诺，你必须包括巴别[多填充](/docs/usage/polyfill)。
>
> ### [](#reflect-api)反映 API
>
> 充分反射 API，暴露对象上的运行时间级元操作。这实际上是代理 API 的反向，并允许拨打与代理陷阱相同的元操作对应的呼叫。特别适用于实施代理。
>
>     var O = {a: 1};
>     Object.defineProperty(O, 'b', {value: 2});
>     O[Symbol('c')] = 3;
>     
>     Reflect.ownKeys(O); // ['a', 'b', Symbol(c)]
>     
>     function C(a, b){
>       this.c = a + b;
>     }
>     var instance = Reflect.construct(C, [20, 22]);
>     instance.c; // 42
>
>
> > #### 通过聚填充支持
> >
> > 为了使用反射API，你必须包括巴别[多填充](/docs/usage/polyfill)物。
>
> ### [](#tail-calls)尾部呼叫
>
> 尾部位置的呼叫保证不会无限增长堆栈。使递归算法在面对无限制输入时安全。
>
>     function factorial(n, acc = 1) {
>         "use strict";
>         if (n <= 1) return acc;
>         return factorial(n - 1, n * acc);
>     }
>     
>     // Stack overflow in most implementations today,
>     // but safe on arbitrary inputs in ES2015
>     factorial(100000)
>
>
> > #### 在巴别尔 6 中暂时删除
> >
> > 由于支持全球支持尾部呼叫的复杂性和性能影响，因此仅支持明确的自引用尾部递归。由于其他错误而删除，并将重新实施。
