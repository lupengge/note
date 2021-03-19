# 学到的C#知识点

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

### extension(扩展)方法

​	在C# 3.0中，扩展方法允许您扩充任何类，甚至是标记为封装的类。扩展方法就是将静态方法（必须声明成static）插入到某个类和其子类中

```c#
namespace MyExtensionMethods
{
  public static class Extension
  {
   //this后面的类型指示要给那个类添加扩展方法，除了这个参数指示对象自己，还能添加其他参数，放到this参数后面
    public static void NoSpaces(this string s)
    {
        return s.Replace(" ", "");
    }
  }
}
```



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

## 网络编程

### 1.tcp和udp的区别

​	TCP：（传输控制协议）含义：是面向连接的协议，也就是说，在收发数据前，必须和对方建立可靠的连接。可靠传输<br>	UDP：（用户数据报协议）含义：是一个非连接的协议，传输数据之前源端和终端不建立连接，当它想传送时就简单地去抓取来自应用程序的数据，并尽可能快的把它扔到网络上。不可靠传输，可能会丢包<br>	Http： (hypertext transport protocol)超文本网络传输协议<br>	FTP: (File Transfer Protocol）文件传输协议。较大文件的网络上传输的协议

1. tcp必须建立可靠的连接，udp无连接
2. tcp对系统资源的要求较多，udp对系统资源的要求较少
3. udp程序结构比较简单
4. tcp是一种流模式的协议，udp是一种数据报模式的协议
5. TCP保证数据的正确性，udp可能会丢包
6. tcp保证数据顺序，udp不保证
7. 传输速度：http<tcp<udp

### 2.IP地址、端口号和终结点

​	ip地址：ip（Internet Protocol）网络上电脑的唯一标识<br>	端口号：电脑上应用程序的标识，0-1024预留给系统应用使用。两台带闹闹通讯本质上是电脑上的应用程序的通讯(IP地址和端口号)<br>	终结点:endpoint ip地址+端口号

常用端口号：

| http |  ftp  | ssh  | Telnet | SMTP |      | DNS  | BootP(server/client) | TFTP | SNMP |
| :--: | :---: | :--: | :----: | :--: | :--: | :--: | :------------------: | :--: | :--: |
|  80  | 20/21 |  22  |   23   |  25  |      |  53  |        67/68         |  69  | 161  |

其中前几个是TCP协议，后几个是UDP协议



