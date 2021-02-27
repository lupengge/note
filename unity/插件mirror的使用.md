# 插件Mirror的使用

> [官方文档](https://mirror-networking.gitbook.io/docs/)

## 一.客户端和服务器之间的信息传递

​	客户端==》服务器：在客户端执行的代码部分调用带有[Command]特性的方法，通过方法的参数传递信息。

​	服务器==》客户端：在服务器执行的代码部分调用带有[ClientRpc]特性的方法，通过方法的参数传递信息。

### 1.传递参数时默认支持的参数类型和自定义参数

#### 	默认支持的参数类型

1. Basic C# types (byte, int, char, uint, UInt64, float, string, etc)
2. Built-in Unity math type (Vector3, Quaternion, Rect, Plane, Vector3Int, etc) 
3. URI
4. NetworkIdentity
5. Game object with a NetworkIdentity component attached
6. Structures with any of the above
7. Classes as long as each field has a supported data type
8. ScriptableObject as long as each field has a supported data type
9. Arrays of any of the above
10. ArraySegments of any of the above

#### 自定义类型

​	想要使mono能够帮我们传递自定义类型的参数，就要自定义这个参数的序列化器，应为在网络传输过程中交换的数据类型都是字符串，我们自定义的类型mono中并没有对应的序列化器，不能将他们转换成字符传进行传输。

> ​	自定义序列化器的例子
>
> ```c#
> public class Item
> {
>     public string Name;
> }
> public class Armour : Item
> {
>     public int Protection;
>     public int weight;
> }
> public class Potion : Item
> {
>     public int Health;
> }
> 
> /// <summary>
> /// item序列化器
> /// </summary>
> public static class ItemSerializer
> {
>     private const byte ITEM_ID = 0;
>     private const byte POTION_ID = 1;
>     private const byte ARMOUR_ID = 2;
> 
>     public static void WriteItem(this NetworkWriter writer, Item item)
>     {
>         if (item is Potion potion)
>         {
>             writer.WriteByte(POTION_ID);
>             writer.WriteString(potion.Name);
>             writer.WritePackedInt32(potion.Health);
>         }
> 
>         if (item is Armour armour)
>         {
>             writer.WriteByte(ARMOUR_ID);
>             writer.WriteString(armour.Name);
>             writer.WritePackedInt32(armour.Protection);
>             writer.WritePackedInt32(armour.weight);
>         }
>         else
>         {
>             writer.WriteByte(ITEM_ID);
>             writer.WriteString(item.Name);
>         }
>     }
> 
>     public static Item ReadItem(this NetworkReader reader)
>     {
>         byte id = reader.ReadByte();
>         switch (id)
>         {
>             case POTION_ID:
>                 return new Potion
>                 {
>                     Name = reader.ReadString(),
>                     Health = reader.ReadPackedInt32()
>                 };
>             case ARMOUR_ID:
>                 return new Armour
>                 {
>                     Name = reader.ReadString(),
>                     Protection = reader.ReadPackedInt32(),
>                     weight = reader.ReadPackedInt32()
>                 };
>             case ITEM_ID:
>                 return new Item
>                 {
>                     Name = reader.ReadString()
>                 };
>             default:
>                 throw new Exception($"Unknown ItemType :{id}");
>         }
>     }
> }
> 代码原文链接：https://blog.csdn.net/farcor_cn/article/details/110360424
> 
> ```
>
> 当使用的参数不是上面列举的类型的时候，另一端接收到的参数就是null



## 二.权限

拥有一个物体的权限才能修改这个物体，server默认拥有全部物体的修改权限

### 1.获取权限的方式

1. 玩家预制体在生成时就被自动赋予了对应的客户端的权限

2. 玩家在服务器上用Spawn方法生成物体的时候可以设置这个物体的权限

3.  修改已有的物体的权限。

   ```c#
   //生成物体时添加对应的权限
   NetworkServer.Spawn(obj, GetComponent<NetworkIdentity>().connectionToClient);
   //这个代码的意思是生成的这个物体属于第二个参数关联的客户端
   
   //修改已经生成的物体的权限
   //otherIdentity是一个NetworkIdentity 类型表示物体的identify
   otherIdentity.AssignClientAuthority(base.connectionToClient);//将该id的物体权限转到该客户端下
   ```

   当你使用[Command]或[ClientRpc]特性进行修改物体的时候，当你没有权限的时候时修改不了的，这时候并不是网络传输的问题。

   