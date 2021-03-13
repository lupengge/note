# USS样式和选择器

## uss选择器

### C#类型选择器

​	TypeName {...}  如 Button { ...}

### 名称选择器

​	匹配name属性值

​	#name {...}

### USS类选择器

​	工作方式和css中相同<br>	.class {...}

### 通用选择器

​	*{...} 匹配每一个元素 ，符号“*”表示通配符

### 后代选择器，空格

​	selector1 selector2 {...} <br>	从selector1选择器筛选出的所有元素的后代中用selector2进行筛选

### 子选择器

​	selector1 > selector2 {...} <br>	再selector1选出的元素的子带中进行selecto2筛选

### 多个选择器

​	多重选择器由两个或多个简单选择器组成，没有任何分隔符。它与所有与所有简单选择器匹配的元素匹配。selector1selector2 {...}<br>	Button.yellow {  background-color: yellow; }

## 伪类

### 支持的伪类

| 伪类        | 与元素匹配                               |
| :---------- | :--------------------------------------- |
| `:hover`    | 光标位于元素上。                         |
| `:active`   | 用户与元素进行交互。                     |
| `:inactive` | 用户停止与元素进行交互。                 |
| `:focus`    | 该元素具有焦点。                         |
| `:selected` | 不适用 Unity不使用此伪状态。             |
| `:disabled` | 元素设置为`enabled == false`。           |
| `:enabled`  | 元素设置为`enabled == true`。            |
| `:checked`  | 元素是一个Toggle元素，并且已启用。       |
| `:root`     | 元素是根元素（可视树中的最高级别元素）。 |

### 伪类链接

​	可以将伪类链接在一起，以将相同的样式应用于多个并发状态。例如，当用户将指针悬停在其上方时，以下USS规则将the`:checked`和`:hover`伪类链接在一起以更改选中`Toggle`元素的颜色。<br>	Toggle:checked:hover {  background-color: yellow; }

### 根伪类

​	该`:root`伪类的可视化树最高的元素相匹配。它与其他受支持的伪类略有不同，因为您可以单独使用它来定义样式表影响的元素的默认样式。

例如，以下USS规则设置默认字体。任何没有从更特定的样式规则中获取其字体的元素都将使用该字体。

```css
:root {
  -unity-font: url("../Resources/fonts/OpenSans-Regular.ttf");
}
```

`:root`选择器的常见用法是声明“全局”变量（自定义属性），其他样式规则可以使用它来代替特定值。

# 事件

## 事件

### 事件的绑定

​	例如，以下代码为 `MouseDownEvent` 注册两个回调：

```c#
    // 对鼠标按下事件注册回调
        myElement.RegisterCallback<MouseDownEvent>(MyCallback);
        // 同上，而且将一些用户数据发送到回调
        myElement.RegisterCallback<MouseDownEvent, MyType>(MyCallbackWithData, myData);
```

回调签名应如下所示：

```c#
void MyCallback(MouseDownEvent evt) { /* ... */ }
void MyCallbackWithData(MouseDownEvent evt, MyType data) { /* ... */ }
```

### 自定义事件

​	合成和发送自定义事件<br>		1.从事件池中获取一个事件对象。 <br>		2.填写事件属性。  <br>		3.将事件包含在 `using` 块中以确保其返回到事件池。  <br>		4.将事件传递给 `element.SendEvent()`。

```c#
void SynthesizeAndSendKeyDownEvent(IPanel panel, KeyCode code,
     char character = '\0', EventModifiers modifiers = EventModifiers.None)
{
    // 创建 UnityEngine.Event 以保存初始化数据。
    // 此外，此事件将转发给 IMGUIContainer.m_OnGUIHandler
    var evt = new Event() {
        type = EventType.KeyDownEvent,
        keyCode = code,
        character = character,
        modifiers = modifiers
    };

    using (KeyDownEvent keyDownEvent = KeyDownEvent.GetPooled(evt))
    {
        panel.SendEvent(keyDownEvent);
    }
}
```

## 事件类型参考

本主题将提供每种事件类型的概要。请参阅 API 文档了解每个事件成员及其用途的完整描述。

### 捕获事件

实现 `IMouseCaptureEvent` 的事件。

#### MouseCaptureEvent

元素接受鼠标捕获时发送 `MouseCaptureEvent`。

`target`：接受捕获的元素。

#### MouseCaptureOutEvent

元素释放鼠标捕获或以其他方式失去鼠标捕获时发送 `MouseCaptureOutEvent`。

`target`：失去捕获的元素。

### 更改事件

实现 `IChangeEvent` 的事件。

#### ChangeEvent

`ChangeEvent<T>` 是元素值更改时发送的通用事件。通常在控件更改时发送。对于 `InputEvent` 控件，不会针对控件中的每个输入事件发送此事件，而是仅在值更改时发送。通常是控件失去焦点或按下 `Enter` 键时。

`<T>` ：值的类型。

`target` ：发生值更改的元素。

`previousValue` ：旧控件值。

`newValue` ：新控件值。

### 命令事件

实现 `ICommandEvent` 的事件。

`target` ：获得键盘焦点的元素。如果没有元素获得焦点，则为 null。

`commandName` ：用于验证或执行的命令。

#### ValidateCommandEvent

此事件由 IMGUI 发送，同时可确定该命令是否由面板中的元素处理。

#### ExecuteCommandEvent

当面板中的元素执行命令时，IMGUI 将发送此事件。

### 拖放事件

拖放操作期间发送的事件。

#### DragExitedEvent

已取消拖放操作。放置目标未接受拖动元素。

#### DragUpdatedEvent

拖动的元素移到放置目标上方。如果放置目标愿意接受拖动的元素，则此事件的回调应设置 `DragAndDrop.visualMode` 以确保在用户松开鼠标键时发送 `DragPerformEvent`。

#### DragPerformEvent

拖动的元素已放置在接受它们的目标上。拖放操作现在已完成。

#### DragEnterEvent

拖动的元素进入了新的 `VisualElement`。具体而言，此事件在拖动操作开始时发送。

#### DragLeaveEvent

拖动的元素离开了当前放置目标。具体而言，此事件在拖动操作结束时发送。

### 布局事件

#### GeometryChangedEvent

当元素的位置或尺寸发生变化时发送的事件。此类型的事件仅发送到事件目标。它们不会传播。

`target` ：具有新几何形状的元素。

`oldRect` ：元素先前的位置和尺寸。

`newRect` ：元素的新位置和尺寸。

### 焦点事件

实现 `IFocusEvent` 的事件。

在元素获得或失去键盘焦点时发送这些事件。有两组焦点事件：

- 在焦点发生变化之前沿着传播路径发送 `FocusOutEvent` 和 `FocusInEvent` 事件。
- 在焦点变化后仅立即将 `FocusEvent` 和 `BlurEvent` 事件发送到事件目标。

#### FocusOutEvent

当元素即将失去焦点时发送的事件。

`target` ：将失去焦点的元素。

`relatedTarget` ：将获得焦点的元素。

#### FocusInEvent

当元素即将获得焦点时发送的事件。

`target` ：将获得焦点的元素。

`relatedTarget` ：将失去焦点的元素。

#### BlurEvent

当元素失去焦点后发送的事件。

`target` ：失去焦点的元素。

`relatedTarget` ：获得焦点的元素。

#### FocusEvent

当元素获得焦点后发送的事件。

`target` ：获得焦点的元素。

`relatedTarget` ：失去焦点的元素。

### 输入事件

#### InputEvent

将数据输入到视觉元素（通常是控件）时发送的事件。此事件与 `ChangeEvent` 的不同之处在于，即使控件的值未更改，也会针对控件中的每个输入事件发送此事件。

`target` ：执行输入的元素。

`previousData` ：以前的数据。

`newData` ：新数据。

### 键盘事件

实现 `IKeyboardEvent` 的事件。

#### KeyDownEvent

用户按下键盘上的键时发送的事件。

`target` ：具有键盘焦点的元素。如果没有元素具有键盘焦点，则为面板的根元素。

#### KeyUpEvent

用户松开键盘上的键时发送的事件。

`target` ：具有键盘焦点的元素。如果没有元素具有键盘焦点，则为面板的根元素。

### 鼠标事件

实现 `IKeyboardEvent` 的事件。

当元素捕获鼠标时，鼠标事件仅发送到进行捕获的元素。无传播。

#### MouseDownEvent

用户按下其中一个鼠标键时发送的事件。

`target` ：如果一个元素接受了鼠标捕获，此元素便是捕获鼠标的元素。否则是光标下最上层的可选元素。

#### MouseUpEvent

用户松开其中一个鼠标键时发送的事件。

`target` ：如果一个元素接受了鼠标捕获，此元素便是捕获鼠标的元素。否则是光标下最上层的可选元素。

#### MouseMoveEvent

用户移动鼠标时发送的事件。

`target` ：如果一个元素接受了鼠标捕获，此元素便是捕获鼠标的元素。否则是光标下最上层的可选元素。

#### ContextClickEvent（已弃用）

用户按下并松开第三个鼠标键时发送的事件。此事件仅用于向后兼容 IMGUI。

#### WheelEvent

用户激活鼠标滚轮时发送的事件。

`target` ：如果一个元素接受了鼠标捕获，此元素便是捕获鼠标的元素。否则是光标下最上层的可选元素。

#### MouseEnterWindowEvent

鼠标进入窗口时发送的事件。

`target` ：如果一个元素接受了鼠标捕获，此元素便是捕获鼠标的元素。否则是光标下最上层的可选元素。

#### MouseLeaveWindowEvent

鼠标离开窗口时发送的事件。

`target` ：如果一个元素接受了鼠标捕获，此元素便是捕获鼠标的元素。否则为 null，因为光标不在元素上方。

#### MouseEnterEvent

鼠标进入元素或其后代之一时发送的事件。此事件与 `MouseOverEvent` 的不同之处在于，此事件将发送到鼠标进入的每个元素。此事件不会传播。

`target` ：鼠标光标下的元素或其后代之一。

#### MouseLeaveEvent

鼠标离开元素或其后代之一时发送的事件。此事件与 `MouseOutEvent` 的不同之处在于，此事件将发送到鼠标退出的每个元素。此事件不会传播。

`target` ：刚被鼠标光标退出或后代之一被鼠标光标退出的元素。

#### MouseOverEvent

鼠标进入元素时发送的事件。此事件与 `MouseEnterEvent` 的不同之处在于，此事件仅发送到鼠标进入的元素。.此事件不会传播。

`target` ：现在位于鼠标光标下的元素。

#### MouseOutEvent

鼠标离开元素时发送的事件。此事件与 `MouseLeaveEvent` 的不同之处在于，此事件仅发送到鼠标已退出的元素并会传播。

`target` ：鼠标光标刚退出的元素。

#### ContextualMenuPopulateEvent

当需要使用菜单项填充上下文菜单时由 `ContextualMenuManager` 发送的事件。

`target` ：要构建上下文菜单的元素。

### 面板事件

#### AttachToPanelEvent

在元素附加到 `IPanel` 后立即发送的事件。由于 面板的设置是递归的，因此元素的所有后代也会 接收该事件。

`target` ：要附加到面板的元素。

#### DetachFromPanelEvent

在元素与 `IPanel` 分离之前发送的事件。由于 面板的设置是递归的，因此元素的所有后代也会 接收该事件。

`target` ：要从面板分离的元素。

### 工具提示事件

#### TooltipEvent

在显示工具提示之前发送的事件。处理程序应该设置 `TooltipEvent.tooltip` 字符串和 `TooltipEvent.rect`。

`target` ：需要显示工具提示的元素。

### IMGUI 事件

#### IMGUIEvent

用于封装 IMGUI 特有事件的事件。



