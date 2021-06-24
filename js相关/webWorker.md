## web worker

浏览器会在后台启动一个独立的线程负责web work代码的运行。[Worker - Web API 接口参考 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/API/Worker)

创建一个专用Web worker，它只执行URL指定的脚本。使用 [Blob URL](https://wiki.developer.mozilla.org/en-US/docs/Web/API/Blob) 作为参数亦可。

### 使用blob动态创建worker 的例子：

```javascript
var myTask = `
    var i = 0;
    function timedCount(){
        i = i+1;
        postMessage(i);
        setTimeout(timedCount, 1000);
    }
    timedCount();
`;

var blob = new Blob([myTask]);
var myWorker = new Worker(window.URL.createObjectURL(blob));
```



### worker和主线程之间的通信

worker和主线曾之间通过onMessage()和postMessage()方法进行通信，

```javaScrip
var myTask = `
    onmessage = function (e) {
        var data = e.data;
        data.push('hello');
        console.log('worker:', data); // worker: [1, 2, 3, "hello"]
        postMessage(data);
    };
`;

var blob = new Blob([myTask]);
var myWorker = new Worker(window.URL.createObjectURL(blob));

myWorker.onmessage = function (e) {
    var data = e.data;
    console.log('page:', data); // page: [1, 2, 3, "hello"]
    console.log('arr:', arr); // arr: [1, 2, 3]
};

var arr = [1,2,3];
myWorker.postMessage(arr);
```



### SharedWorker和Dedicated Worker

这两个分别代表两种特定类型的worker，sharedworker可以从几个浏览器上下文访问，例如几个窗口、iframe或其他worker，而Dedicated Worker只能为一个页面所使用。