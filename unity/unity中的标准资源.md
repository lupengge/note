### 添加标准资源到项目中

1.从unity官网下载standard assetsSetUp

2.点击安装

3.安装后就能在安装路径下"Editor/Standard Assets"下找到资源包

4.在project视图中将需要的资源包导入到项目中

###  轨迹渲染器

1.创建一个带有tril render的游戏对象或直接通过菜单中的GameObject中的effect-->trail创建

2.将要添加轨迹的游戏对象放到上面创建的游戏对象的子级下，将position设为（0，0，0）

3.调整tril render中的属性

4.当移动第一步创建的游戏对象时要添加轨迹的游戏对象也会移动并会渲染轨迹

###  实例化预制件示例

```c#
using UnityEngine;
public class InstantiationExample : MonoBehaviour 
{
    // 引用预制件。在 Inspector 中，将预制件拖动到该字段中。
    public GameObject myPrefab;

    // 该脚本将在游戏开始时简单地实例化预制件。
    void Start()
    {
        // 实例化为位置 (0, 0, 0) 和零旋转。
        Instantiate(myPrefab, new Vector3(0, 0, 0), Quaternion.identity);
    }
}
```

也能用`Resources.Load();`加载在项目中的资源然后进行类型转换成GameObject类型

*在拖入inspector进行赋值时，可以将含有某个类型的GameObject类型赋值给相应的类型*

### C#中的值类型和引用类型

值类型包括：整数、浮点数、布尔值、结构类型

引用类型：对象、字符串、数组

*多个字符串多次连接时应使用stringBuilder以减少内存的使用*

*函数结果中含有数组时，尽量将这个数组作为参数传入，不要再函数中新建一个数组对象，减少内存的使用*

### 欧拉角和Quaternin转换

unity游戏对象的rotation是Quaternion类型

1.将quaternion转换成euler用quaternion的eulerAngles属性

2.将Euler转换成Quaternion：`Quaternion.Euler(angles)`

### 选择加权散点型随机项

```c#
float Choose (float[] probs) {

    float total = 0;

    foreach (float elem in probs) {
        total += elem;
    }

    float randomPoint = Random.value * total;

    for (int i= 0; i < probs.Length; i++) {
        if (randomPoint < probs[i]) {
            return i;
        }
        else {
            randomPoint -= probs[i];
        }
    }
    return probs.Length - 1;
}
```

### 加权连续随机点

让随机数代入一个函数中，函数曲线平滑的地方权重就比较大

![线性曲线根本不对值进行加权；曲线上每个点的水平坐标等于垂直坐标。](https://docs.unity.cn/cn/2020.2/uploads/Main/WeightedRandomCurve-linear.png)

### 从数组中随机选出n项

1.C#实现

```c#
  static T[] chose<T>(T[] source, int numRequired)
  {
    T[] result = new T[numRequired];
    int numToChoose = numRequired;
    Random random = new Random();//c#中的Random
    for (int numLeft = source.Length; numLeft > 0; numLeft--)
    {
      float prob = (float)numToChoose / (float)numLeft;
      if (random.NextDouble() <= prob)
      {
        numToChoose--;
        result[numToChoose] = source[numLeft - 1];
        if (numToChoose == 0)
        {
          break;
        }
      }
    }
    return result;
  }
```

2.JavaScript代码

```javascript
a=[0,1,2,3,4,5,6,7,8,9];
function chose(source=a,num){
  chosen=[];
  source.forEach((element,index) => {
    chance=(num-chosen.length)/(10-index);
    if(Math.random()<chance){
      chosen[chosen.length]=element;
    }
  });
  return chosen;
}
console.log(chose(6));
```

### 从一组游戏对象中选出随机几个

```c#
Transform[] spawnPoints;
Transform[] ChooseSet (int numRequired) {
    Transform[] result = new Transform[numRequired];
    int numToChoose = numRequired;
    for (int numLeft = spawnPoints.Length; numLeft > 0; numLeft--) {
        float prob = (float)numToChoose/(float)numLeft;
        if (Random.value <= prob) {
            numToChoose--;
            result[numToChoose] = spawnPoints[numLeft - 1];
            if (numToChoose == 0) {
                break;
            }
        }
    }
    return result;
}
```

### 在scene中画线框