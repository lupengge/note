# unity学习

## unity

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

### 欧拉角和Quaternin转换

unity游戏对象的rotation是Quaternion类型

1.将quaternion转换成euler用quaternion的eulerAngles属性

2.将Euler转换成Quaternion：`Quaternion.Euler(angles)`

### 在scene中画自定义形状能用Gizmos类和Handles类

### 两种下载texture的方法

1.

```c#
using UnityEngine;
using System.Collections;
using UnityEngine.Networking;
 
public class MyBehaviour : MonoBehaviour {
	void Start() {
		StartCoroutine(GetTexture());
	}

	IEnumerator GetTexture() {
		UnityWebRequest www = UnityWebRequestTexture.GetTexture("http://www.my-server.com/image.png");
		yield return www.SendWebRequest();

		if (www.result != UnityWebRequest.Result.Success) {
				Debug.Log(www.error);
		}
		else {
				Texture myTexture = ((DownloadHandlerTexture)www.downloadHandler).texture;
		}
	}
}
```

2.使用helper getter

```c#
    IEnumerator GetTexture() {
            UnityWebRequest www = UnityWebRequestTexture.GetTexture("http://www.my-server.com/image.png");
            yield return www.SendWebRequest();

            Texture myTexture = DownloadHandlerTexture.GetContent(www);
        }
```

### 加权、散点型随机项

​	从几项中随机选出一个

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

### 加权、连续随机点

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

## C#不常用（[官方文档](https://docs.microsoft.com/zh-cn/dotnet/csharp/)）

### C#在值类型后加？

```c#
DateTime? date=null;
//等效于
Nullable<DateTime> date=null;
int? a =null;//等效于
Nullable<int> a=null;
```

### C#避免因值类型为null而抛出异常

1.通过if...else...语句

```c#
int result;
if(a == null)
{
    result = 0;
}
else
{
    result = (int)a;
}
```

2.通过“??”

```c#
int result = a ?? 0;
```

### C#中的数字类型、后缀u

> int(32位)
> int: –2147483648 to 2147483647 
> uint: 0 to 4294967295 
>
> long(64位)
> long: -9223372036854775808 to 9223372036854775807
> ulong: 0 to 18446744073709551615

### C#中的值类型和引用类型

值类型包括：整数、浮点数、布尔值、结构类型

引用类型：对象、字符串、数组

*多个字符串多次连接时应使用stringBuilder以减少内存的使用*

*函数结果中含有数组时，尽量将这个数组作为参数传入，不要再函数中新建一个数组对象，减少内存的使用*

## C#中的关键词

### sealed关键词

​	sealed关键词修饰的类是不能被继承的，不能被派生的，这种类通常被称作密封类<br>	被sealed关键词修饰的方法是不能被子类重写的

### base关键词

​	当子类重写父类方法后，base关键词用于在子类中访问父类的成员<br>	能在重写的方法后直接写上":base()",表示调用父类的这个方法

### in关键词

​	1.在foreach语句中使用<br>	2.在linq中的join in语句中使用<br>	3.方法参数关键词

### 方法参数

- [params](https://docs.microsoft.com/zh-cn/dotnet/csharp/language-reference/keywords/params) 指定此参数采用可变数量的参数。
- [in](https://docs.microsoft.com/zh-cn/dotnet/csharp/language-reference/keywords/in-parameter-modifier) 指定此参数由引用传递，但只由调用方法读取。
- [ref](https://docs.microsoft.com/zh-cn/dotnet/csharp/language-reference/keywords/ref) 指定此参数由引用传递，可能由调用方法读取或写入。
- [out](https://docs.microsoft.com/zh-cn/dotnet/csharp/language-reference/keywords/out-parameter-modifier) 指定此参数由引用传递，由调用方法写入。

## C#中的强类型委托（预定义委托）

### Action类型

​	Action类型表示返回值为void的委托类型。变体最对可以有16个输入参数

```c#
public delegate void Action();
public delegate void Action<in T>(T arg);
public delegate void Action<in T1, in T2>(T1 arg1, T2 arg2);
// Other variations removed for brevity.
```

### Function类型

​	对任何返回值的委托类型使用一种 `Func` 类型。按照约定，结果的类型始终是所有 `Func` 声明中的最后一个类型参数。

```c#
public delegate TResult Func<out TResult>();
public delegate TResult Func<in T1, out TResult>(T1 arg);
public delegate TResult Func<in T1, in T2, out TResult>(T1 arg1, T2 arg2);
// Other variations removed for brevity
```

### Predicate类型

​	Predicate类型表示返回值为bool类型的

```c#
public delegate bool Predicate<in T>(T obj);
```

