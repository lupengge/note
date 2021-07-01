# 一、使用MutationObserver监听Dom

[MutationObserver \- Web API 接口参考 \| MDN \(mozilla\.org\)](https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver)，MutationObserver接口提供了监视对DOM树所做更改的能力。它被设计为旧的Mutation Events功能的替代品，该功能是DOM3 Events规范的一部分。

``` javaScript
// 选择需要观察变动的节点
const targetNode = document.getElementById('some-id');

// 观察器的配置（需要观察什么变动）
const config = { attributes: true, childList: true, subtree: true };

// 当观察到变动时执行的回调函数
const callback = function(mutationsList, observer) {
    for(let mutation of mutationsList) {
        if (mutation.type === 'childList') {
            console.log('A child node has been added or removed.');
        }
        else if (mutation.type === 'attributes') {
            console.log('The ' + mutation.attributeName + ' attribute was modified.');
        }
    }
};

// 创建一个观察器实例并传入回调函数
const observer = new MutationObserver(callback);

// 以上述配置开始观察目标节点
observer.observe(targetNode, config);
//config


// 之后，可停止观察
observer.disconnect();
```

# 二、监听js代码中对象属性的变化

## 1.使用getter和setter监听对象属性的变化，

Object.defineProperty()是一个用于修改已有属性或为对象定义新属性的函数

``` javaScript
//Object.defineProperty(obj,prop,description)
description={
	value,//Object,属性的值,默认值,undefined
	writable,//bool,属性是否可以修改,默认值false
	enumerable,//bool,属性是否被循环遍历枚举,默认值false
	configurable,//bool,属性是否可以删除，描述符是否配置,默认值false
	get,//function,属性被读取时被调用的函数,默认值undefined
	set,//function,属性被赋值时调用的函数,默认值undefined
}
var tool={
    type:"point",
    onTypeChange:undefined
}
//不能同时设置get，set和value,实际的值存在这个对象的_type属性中
Object.defineProperties(tool, {
	type: {
		set: function (newVal) {
			
            //可以在这执行,
            if(typeof(this.onTypeChange)==="function"){
                this.onTypeChange(newVal,this._type)
            }
            this._type = newVal;
		},
		get: function () {
			return this._type
		}
	}
})
```