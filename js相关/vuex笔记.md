# vuex文档笔记
  vuex是一个专门为vue应用程序开发的状态管理模式，帮助我们管理共享状态
##在跟组件注册store，所有的子组件都能访问到
  ```javaScript
    new Vue({
      el: '#app',
      store: store,
    })
    ///使用vue-cli创建项目直接添加vuex组件，自动配置
  ```
## state
  就是存储的属性，和vue实例中的data遵循相同的规则。
  想要在组件中获取vuex中的状态
  使用计算属性：

  ```JavaScript
    // 创建一个 Counter 组件
    const Counter = {
      template: `<div>{{ count }}</div>`,
      computed: {
        count () {
          return store.state.count
        }
        /*
        使用辅助函数mapState()
        ...mapState(["count"])或
        ...mapState({
          count:state=>state.count
        })
        */
      }
    }
  ```
## Getters
  就是vue中的计算属性(computed)
  在组件中使用：
  ```javaScript
    computed: {
      doneTodosCount () {
        return this.$store.getters.doneTodosCount
      }
    }
  /*
    使用辅助函数mapGetterss
      computed: {
      // 使用对象展开运算符将 getter 混入 computed 对象中
      ...mapGetters([
        'doneTodosCount',
        'anotherGetter',
        // ...
      ])
      或使用别名
      ...mapGetters({
          // 把 `this.doneCount` 映射为 `this.$store.getters.doneTodosCount`
          doneCount: 'doneTodosCount'
        })
  */
  }
  ```
## Mutations
  就是vue中的自定义事件，更改 Vuex 的 store 中的状态的唯一方法是提交 mutation。使用Mutation，在逐渐中提交Mutation，或使用mapMutations辅助函数将组件中的methods映射为store.commit调用。

```javaScript
import { mapMutations } from 'vuex'

export default {
  // ...
  methods: {
    ...mapMutations([
      'increment', // 将 `this.increment()` 映射为 `this.$store.commit('increment')`

      // `mapMutations` 也支持载荷：
      'incrementBy' // 将 `this.incrementBy(amount)` 映射为 `this.$store.commit('incrementBy', amount)`
    ]),
    ...mapMutations({
      add: 'increment' // 将 `this.add()` 映射为 `this.$store.commit('increment')`
    })
  }
}
```

### 提交载荷(Paylod)

可以向store.commit传入额外的参数，默认传一个字符串类型的mutation名

```JavaScript
// ...
mutations: {
  increment (state, n) {
    state.count += n
  }
}

store.commit('increment',10);
//可以载荷可以是一个对象
mutations: {
  increment (state, payload) {
    state.count += payload.amount
  }
}

store.commit('increment',{amount:10});

//对象风格的写法
mutations: {
  increment (state, payload) {
    state.count += payload.amount
  }
}

store.commit({
    type:'increment',
    amount:10
});


```



##   Actions

​	专门用来处理异步操作的，action提交的是mutation，不直接更改状态。Action通过Store.dispatch方法触发。

```JavaScript
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment (state) {
      state.count++
    }
  },
  actions: {
    increment (context) {
      context.commit('increment')
    }
  /*或用es2015中的参数析构
  actions:{
  	increment({commit}){
  		commit('increment');
  	}
  }
  
  */
  }
})

//分发Action,并添加载荷
	// 以载荷形式分发
    store.dispatch('incrementAsync', {
      amount: 10
    })

    // 以对象形式分发
    store.dispatch({
      type: 'incrementAsync',
      amount: 10
    })

```

