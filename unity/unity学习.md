# unity学习

## unity

### 资源

#### StreamingAssets文件夹

​	unity中的资源在打包生成可执行文件的时候都会进行压缩，但是StreamingAssets文件夹中的文件并不会进行压缩，编码格式并不会发生改变。获取这个文件夹的位置：`Application.streamingAssetsPath`,想获取其中的文件可以用system.io下的File或文件流等。

#### 加载资源的方式

- 只能在editor中使用的AssetDatabase
- AssetBundle类
- Resources.load()方法
- UnityWebRequest

#### 实例化预制体

```c#
GameObject prefab=Resources.load("");
Instantiate(prefab, position, rotation);
```

####  实例化预制件示例

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

#### ScriptableObject

​	ScriptableObject 是一个可独立于类实例来保存大量数据的数据容器。ScriptableObject 的一个主要用例是通过避免重复值来减少项目的内存使用量。如果项目有一个[预制件](http://localhost/unity/Manual/Prefabs.html)在附加的 MonoBehaviour 脚本中存储不变的数据，这将非常有用。<br>	每次实例化预制件时，都会产生单独的数据副本。这种情况下可以不使用该方法并且不存储重复数据，而是使用 ScriptableObject 来存储数据，然后通过所有预制件的引用访问数据。这意味着内存中只有一个数据副本。<br>	就像 MonoBehaviour 一样，ScriptableObject 派生自基本 Unity 对象，但与 MonoBehaviour 不同，不能将 ScriptableObject 附加到[游戏对象](http://localhost/unity/Manual/class-GameObject.html)。正确的做法是需要将它们保存为项目中的资源。<br>	如果使用 Editor，可以在编辑时和运行时将数据保存到 ScriptableObject，因为 ScriptableObject 使用 Editor 命名空间和 Editor 脚本。但是，在已部署的构建中，不能使用 ScriptableObject 来保存数据，但可以使用在开发期间设置的 ScriptableObject 资源中保存的数据。<br>	从 Editor 工具作为资源保存到 ScriptableObject 的数据将写入磁盘，因此将在会话之间一直保留。<br>ScriptableObjects 的主要用例为：

- 在 Editor 会话期间保存和存储数据
- 将数据保存为项目中的资源，以便在运行时使用

要使用 ScriptableObject，必须在应用程序的 **Assets** 文件夹中创建一个脚本，并使其继承自 `ScriptableObject` 类。您可以使用 [CreateAssetMenu](http://localhost/unity/ScriptReference/CreateAssetMenuAttribute.html) 属性，从而使用您的类轻松创建自定义资源。例如：

```c#
using UnityEngine;

[CreateAssetMenu(fileName = "Data", menuName = "ScriptableObjects/SpawnManagerScriptableObject", order = 1)]
public class SpawnManagerScriptableObject : ScriptableObject
{
    public string prefabName;

    public int numberOfPrefabsToCreate;
    public Vector3[] spawnPoints;
}
```

#### 添加标准资源到项目中

1.从unity官网下载standard assetsSetUp

2.点击安装

3.安装后就能在安装路径下"Editor/Standard Assets"下找到资源包

4.在project视图中将需要的资源包导入到项目中

#### 两种下载texture的方法

##### 1.UnityWebRequestTexture

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

##### 2.使用helper getter

```c#
IEnumerator GetTexture() {
  UnityWebRequest www = UnityWebRequestTexture.GetTexture("http://www.my-server.com/image.png");
  yield return www.SendWebRequest();

  Texture myTexture = DownloadHandlerTexture.GetContent(www);
}
```

###  轨迹渲染器的使用

1.创建一个带有tril render的游戏对象或直接通过菜单中的GameObject中的effect-->trail创建

2.将要添加轨迹的游戏对象放到上面创建的游戏对象的子级下，将position设为（0，0，0）

3.调整tril render中的属性

4.当移动第一步创建的游戏对象时要添加轨迹的游戏对象也会移动并会渲染轨迹

### 欧拉角和Quaternin转换

unity游戏对象的rotation是Quaternion类型

1.将quaternion转换成euler用quaternion的eulerAngles属性

2.将Euler转换成Quaternion：`Quaternion.Euler(angles)`

### 在scene中画自定义形状能用Gizmos类和Handles类

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

### unity设置不同屏幕适配

1. 画布(canvas)中的缩放器组件(Canvas Scaler)中的UI Scale Mode设置为“Scale With Screen Size”
2. 设置缩放器组件中的参考分辨率(reference Resolution)
3. 设置缩放器组件中的Match属性为0.5，这样当画布的宽度扩大到原来的1.5倍而高度缩短为原来的1/1.5，最终的缩放因子为1
4. 设置画布中元素的锚点

### 设置自动寻路和动画耦合

```c#
//		// Pull character towards agent
        //if (worldDeltaPosition.magnitude > agent.radius)
        //    transform.position = agent.nextPosition - 0.9f * worldDeltaPosition;
//或
void OnAnimatorMove () {
        // Update postion to agent position
        //transform.position = agent.nextPosition;

        // Update position based on animation movement using navigation surface height
        Vector3 position = anim.rootPosition;
        position.y = agent.nextPosition.y;
        transform.position = position;
    }
```

### 用Unity原生UGUI搭建一个目录树

首先看实现效果

![MenuTree](../images/MenuTree.gif)

1. 先弄一个主题框架，有标题（text），有content（一个scroll View,如果内容过多）

2. 设计目录树中的一级的UI并将它拖出来成为预制体<br>预制体中间留一个空的游戏对象,用来存放这一级的孩子节点

3. 写一个菜单节点的C#类

   ```c#
   /// <summary>
   /// 目录树中的其中一级
   /// </summary>
   class MenuItemData
   {
       public string name;
       public List<MenuItemData> children;
   }
   ```

   写一个json文档，存放目录树的结构，使这个目录树可以复用。

   在程序开始的时候加载，并序列化json文档

   ```c#
   try
   {
       string MenuData = File.ReadAllText(Path.Combine(Application.streamingAssetsPath, MenuDataPath));
       menuObject = JsonMapper.ToObject<MenuItemData>(MenuData);
       loadMenu(menuObject);
   }
   catch (IOException iOException)
   {
       Debug.LogWarning(iOException.Message);
   }
   ```

   ​	根据数据绘制UI

   ```c#
   void loadMenu(MenuItemData menuData)
   { 
     //在搭建主题框架的时候留了一个放目录内容的空游戏对象名叫“content”，这个脚本在目录树主体上挂
       GameObject contentObj = transform.Find("content").gameObject;
       for (int i = 0; i < menuData.children.Count; i++)
       {
           addItemToUI(menuData.children[i], contentObj, i);
       }
   }
   ```

   思路一：

   1. 后面addItemToUI用递归的方法生成每一个等级的UI
   2. 将级别较高的item在初始化时setActive(false)
   3. 根据数据设置ui中的文字
   4. 给item添加事件，item中有一个button。在事件中控制UI的位置变化
   5. 想给item的UI添加可配置的UI可以给MenuItemData类添加一个string字段，在json中写要调用的方法名称，然后用反射的方法，调用某一个类中的方法

   ```c#
   
   /// <summary>
   /// 将mentTree数据中的item变成游戏对象添加到UI中
   /// </summary>
   /// <param name="item">菜单中的一级</param>
   /// <param name="parent">要放进去的游戏对象，这个游戏对象应该由</param>
   /// <param name="index">这个item在原children列表中的index</param>
   void addItemToUI(MenuItemData item,GameObject parent, int index)
   {
       //实例化一个item游戏对象并将它添加到parent中的
       GameObject currentItem = Instantiate(menuItem, parent.transform);
   
       string parentNodeName = parent.transform.parent.gameObject.name;
       if (parentNodeName!="TreeMenu")
       {
           currentItem.name = parent.transform.parent.gameObject.name + "-" + index.ToString();
           currentItem.SetActive(false);
       }
       else
       {
           currentItem.name = index.ToString();
       }
           
       currentItem.transform.localPosition = new Vector3(0, -20 * index, 0);
       GameObject nextParent = currentItem.transform.Find("childItems").gameObject;
   
       currentItem.transform.Find("Text").gameObject.GetComponent<Text>().text = item.name;
   
       bool isOnBefore = false;
       //添加ui点击tree实现的监听
       currentItem.GetComponent<Button>().onClick.AddListener(() =>
       {
           currentItem.transform.GetChild(0).Rotate(new Vector3(0, 0, isOnBefore ? 90 : -90));
               
           if (isOnBefore)
           {
               moveAllAfterItem(currentItem.transform, NumOfActiveChildren(currentItem.transform) * 20);
               for (int i = 0; i < nextParent.transform.childCount; i++)
               {
                   nextParent.transform.GetChild(i).gameObject.SetActive(!isOnBefore);
               }
           }
           else
           {
               for (int i = 0; i < nextParent.transform.childCount; i++)
               {
                   nextParent.transform.GetChild(i).gameObject.SetActive(!isOnBefore);
               }
               moveAllAfterItem(currentItem.transform, -NumOfActiveChildren(currentItem.transform) * 20);
           }
   
           isOnBefore = !isOnBefore;
       });
   
       //将这个item数据的children添加到UI中
       for (int i = 0; i < item.children.Count; i++)
       {
           addItemToUI(item.children[i], nextParent, i);
       }
   }
   /// <summary>
   /// 遍历目录树，并将某个节点移动一个距离
   /// </summary>
   /// <param name="item">点击的游戏对象的transform</param>
   /// <param name="distance">要移动的距离</param>
   void moveAllAfterItem(Transform item,int distance)
   {
           
       string[] indexs = item.gameObject.name.Split('-');
   
       //目录树的起始节点
       Transform startNode = GameObject.Find("content").transform;
   
       Queue<Transform> pendingTransform = new Queue<Transform>();
       for(int i=0;i< startNode.childCount; i++)
       {
           pendingTransform.Enqueue(startNode.GetChild(i));
       }
           
   
       while (pendingTransform.Count>0)
       {
           //从堆栈中抛出一个transform，将它的下一层所有孩子压入堆栈
           Transform currentTransform = pendingTransform.Dequeue();
           for (int i = 0; i < currentTransform.GetChild(1).childCount; i++)
           {
               pendingTransform.Enqueue(currentTransform.GetChild(1).GetChild(i));
           }
               
           string[] currentindexs = currentTransform.gameObject.name.Split('-');
   
           //给的index[1,1,1]
           //当前index[2,0]
   
           //当根相同或长度为1且第
           if (currentTransform.gameObject.activeSelf)
           {
               for (int i = 0; i < (currentindexs.Length<indexs.Length?currentindexs.Length:indexs.Length); i++)
               {
                   if (currentindexs.Length < i+2 || currentindexs[i] == indexs[i])
                   {
                       if (int.Parse(indexs[i]) < int.Parse(currentindexs[i]))
                       {
                           currentTransform.localPosition = new Vector3(0, currentTransform.localPosition.y + distance, 0);
                           if (currentindexs.Length>1&&currentindexs[0]!=indexs[0])
                           {
                               currentTransform.localPosition = new Vector3(0, currentTransform.localPosition.y - distance, 0);
                           }
                           break;
                       }
                   }
               }
           }
       }
   }
   
   /// <summary>
   /// 返回该节点下面打开的所有节点
   /// </summary>
   /// <param name="menuItem"></param>
   /// <returns></returns>
   int NumOfActiveChildren(Transform menuItem)
   {
       int count = 0;
       Queue<Transform> pendingTransform = new Queue<Transform>();
   
       pendingTransform.Enqueue(menuItem);
   
       while (pendingTransform.Count>0)
       {
           Transform currentItem = pendingTransform.Dequeue();
           Transform nextParent = currentItem.Find("childItems");
           //先将这个节点所有的孩子节点入栈
           for (int i = 0; i < nextParent.childCount; i++)
           {
               pendingTransform.Enqueue(nextParent.GetChild(i));
           }
           if (currentItem.gameObject.activeInHierarchy)
           {
               count += 1;
           }
       }
       return count-1;
   }
   ```

## C#不常用

（[官方文档](https://docs.microsoft.com/zh-cn/dotnet/csharp/)）

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

### Array、ArrayList、list的区别

array最早出现，由于它在内存中是连续存储的，查找的速度非常快、赋值和修改元素很简单，但是它的长度是不能变化的，插入数据非常麻烦、在声明时需要给一个长度，长度过长会造成内存浪费。

ArrayList是命名空间System.Collections下的一部分，ArrayList对象的大小是按照其中存储的数据来动态扩充与收缩的。arrayList中读取和插入时会有一个拆箱和封箱的过程（Arraylist中实际存的是object，每次操作都有一个转换），这样就允许存入不同类型的数据，但是这样会带来很大的性能耗损。

List类是ArrayList类的泛型等效类，在声明list时要提供一个对象类型，并且list中只能存这个类型的对象，list没有封箱、拆箱的操作比arrayList性能强。

数组可以具有多个维度，而 ArrayList或 List< T> 始终只具有一个维度。但是，您可以轻松创建数组列表或列表的列表。特定类型（Object 除外）的数组 的性能优于 ArrayList的性能。 这是因为 ArrayList的元素属于 Object 类型；所以在存储或检索值类型时通常发生装箱和取消装箱操作。不过，在不需要重新分配时（即最初的容量十分接近列表的最大容量），List< T> 的性能与同类型的数组十分相近。

在决定使用 List\<T\> 还是使用ArrayList 类（两者具有类似的功能）时，记住List\<T\> 类在大多数情况下执行得更好并且是类型安全的。如果对List< T> 类的类型T 使用引用类型，则两个类的行为是完全相同的。但是，如果对类型T使用值类型，则需要考虑实现和装箱问题。

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

## Linq

### AsEnumerable和AsQueryable的区别

​	1.执行顺序不同。AsQueryable是在数据库中查询再返回数据，AsEnumerable是从数据库读取全部数据再在程序中查询。将Ienumerable\<T\>转换成IQueryable\<T\>后,当遇到连表查询的时候,能提高速度，因为先将数据从数据库转存到内存中.

## 由骑士旅行——寻路算法

1. 用深度优先算法进行技术，能找到两点之间路径的解
2. 比较各种路径的长度

