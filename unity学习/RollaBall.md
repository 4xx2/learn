---
title: "RollaBall"
output:
    word_document:
        path: RollaBall.docx
        toc: true
        toc_depth: 6
        number_sections: true
---
## FixedUpdate和Update的区别是什么
在Unity中，`FixedUpdate`和`Update`都是用于脚本中的两个不同的函数，用于处理游戏逻辑和更新物体状态。它们在执行时机和频率上有一些重要的区别：
> 要用update，需要加上deltaTime，从而保证连续的动画效果
1. **Update（每帧调用）**：
   - `Update` 函数在每一帧都被调用，通常用于处理与输入、移动、动画和游戏逻辑相关的事务。
   - 由于它是每帧调用的，所以它不受固定的时间间隔影响，帧率较高时调用次数会增加，帧率较低时调用次数会减少。
   - 适用于需要实时响应输入和不受固定时间步长限制的情况。

2. **FixedUpdate（固定时间间隔调用）**：
   - `FixedUpdate` 函数在固定的时间间隔内被调用，通常默认为每秒50次（可以通过`Time.fixedDeltaTime`来获取固定的时间间隔）。
   - 主要用于处理物理相关的事务，因为物理引擎通常在固定时间步长内进行模拟，所以将物理计算放在这里可以获得更稳定的结果。
   - 避免了在不同帧率下产生不一致的物理效果。
   - 适用于涉及刚体、碰撞检测和物理模拟的操作。

总之，区分`Update`和`FixedUpdate`的主要点在于：
- `Update` 用于处理帧率相关的游戏逻辑，适用于与输入和动画有关的操作。
- `FixedUpdate` 用于处理固定时间间隔的物理模拟，适用于与刚体、碰撞和物理效果有关的操作。
```csharp
    private void FixedUpdate()
    {
        Vector3 movement = new Vector3 (movementX, 0.0f, movementY);
        rb.AddForce(movement * speed);
    }
```
## InputSystem
Unity Input System 是 Unity 游戏引擎的一个新输入系统，用于处理游戏中的用户输入。它提供了更灵活、可定制和可扩展的方式来管理输入，并且相对于之前的输入系统具有更好的性能。

以下是 Unity Input System 的一些特点和优势：

1. **统一的输入管理**：Unity Input System 提供了一个统一的方式来处理不同平台和设备的输入，使得在不同设备上的输入处理更加一致。

2. **支持多种输入设备**：除了支持常见的键盘和鼠标输入外，它还支持游戏手柄、触摸屏、虚拟现实设备等多种输入方式。

3. **延迟和响应性**：Input System 在处理输入上具有更低的延迟，能够更准确地响应玩家的操作，这对于需要高度精准输入的游戏非常重要。

4. **输入处理管线**：Input System 提供了输入处理管线，可以通过配置来修改和增强输入数据的处理过程，从而满足不同类型游戏的需求。

5. **输入映射和绑定**：使用 Input System，你可以定义自定义的输入映射和绑定，使得玩家可以自行配置输入设置，从而提升可订制性。

6. **虚拟按键**：Input System 支持创建虚拟按键，这些按键可以代表多个实际的输入，使得设计复杂的控制方案变得更加容易。

7. **可扩展性**：Input System 允许开发者通过编写插件来扩展其功能，满足特定游戏的需求。

要开始使用 Unity Input System，你需要在 Unity 中导入 Input System 包，并且了解其基本的配置、输入处理和事件处理机制。官方文档提供了详细的教程和示例，帮助你逐步了解和应用这个新的输入系统。注意，因为技术和软件可能会有更新，建议查阅最新版本的 Unity Input System 文档以获取最准确和最新的信息。
## LateUpdate和Update的区别
在 Unity 中，除了 `Update` 函数外，还有一个叫做 `LateUpdate` 的函数。这两者在脚本中的执行时机和用途上有一些区别。
```csharp
// 因为摄像头的update和对象移动的update执行顺序不确定，所以推荐使用lateupdate
void LateUpdate() //当所有Update执行完后，才会执行LateUpadate
{
    transform.position = offset + player.transform.position;
}
```
1. **Update（每帧调用）**：
   - `Update` 函数在每一帧都会被调用。这是一个常用的函数，用于处理游戏逻辑、用户输入、移动、动画以及其他与帧率相关的操作。
   - 由于它在每一帧都被调用，所以如果你需要在游戏逻辑中处理实时的操作，例如玩家输入或者移动物体，那么你可以使用 `Update` 函数。

2. **LateUpdate（每帧调用，但在 Update 之后）**：
   - `LateUpdate` 函数也在每一帧被调用，但在 `Update` 函数之后执行。
   - 这个函数的主要用途是确保在 `Update` 函数执行后，所有的对象已经完成了其状态更新。这对于涉及相机跟随或对象之间位置同步等操作非常有用。
   - 例如，如果你在 `Update` 中移动了一个对象，而另一个对象需要跟随这个移动，那么你可以在 `LateUpdate` 中更新跟随对象的位置，以确保它在跟随源对象之后更新。

总结来说，`Update` 用于处理实时游戏逻辑和操作，而 `LateUpdate` 则用于确保在一帧中的所有对象状态都已经更新之后再执行一些操作，通常用于相机控制、位置同步等场景。这样可以防止对象之间的不同步现象。
## Unity中的移动
# transform
`Transform` 是一个组件（Component）,用于定义物体的位置、旋转和缩放。每个 GameObject（游戏对象）在 Unity 中都附带一个 Transform 组件，用于管理其在世界空间中的变换信息。

Transform 组件具有以下几个主要属性：
Position（位置）： 表示物体在世界空间中的位置坐标。
Rotation（旋转）： 表示物体的旋转角度和方向。
Scale（缩放）： 表示物体在每个轴上的缩放因子。

Transform 组件允许你在场景中定位、旋转和缩放游戏对象。你可以通过修改 Transform 的属性来实现这些变换操作。这对于控制游戏对象的外观、位置和动作非常重要。

在 Unity 中，transform 是 MonoBehaviour 的一个属性，用于访问所附加的游戏对象的 Transform 组件。**你无需显式获取 Transform 组件，因为 transform 已经提供了对该组件的引用。**

以下是一些 `Transform` 常用的方法：

1. **移动和位置：**
   - `Translate(Vector3 translation)`：将物体按照指定的位移移动。
   - `Translate(float x, float y, float z)`：将物体按照指定的 X、Y 和 Z 轴位移移动。
   - `position`：获取或设置物体的世界空间位置。
```csharp
        // 朝Vector3指定的方向移动
        transform.Translate(new Vector3(0,0,1));
        // 移动对象---改变transform的属性position
        transform.position = targetPosition;
```
2. **旋转：**
   - `Rotate(Vector3 eulerAngles)`：按照欧拉角旋转物体。
   - `Rotate(float xAngle, float yAngle, float zAngle)`：按照指定的欧拉角绕 X、Y 和 Z 轴旋转物体。
   - `LookAt(Transform target)`：使物体朝向指定目标的位置。
## 预制件
Unity的预制件（Prefabs）是一种在游戏开发中非常有用的概念，它们允许开发人员创建和管理游戏中的可复用元素。预制件是一种将对象、组件和属性打包为一个可在场景中多次使用的模板。通过使用预制件，您可以轻松地创建相似的对象，而无需每次都从头开始构建它们。
   - 新建文件夹，命名为Prefabs，将对象拖入文件夹即可成为预制件。
## 碰撞检测 OnTriggerEnter
OnTriggerEnter 是Unity中用于处理触发器碰撞事件的函数。当一个游戏对象的触发器（Trigger）与另一个游戏对象的碰撞体相交时，会调用位于脚本中的 OnTriggerEnter 函数。这让您可以在两个物体之间发生碰撞时执行自定义的代码逻辑。
以下是关于 OnTriggerEnter 的简要介绍：

触发时机： 当一个游戏对象的触发器与另一个游戏对象的碰撞体**相交**时，OnTriggerEnter 函数会被调用。这通常在游戏对象进入触发器所定义的区域时发生。

脚本位置： 您需要将包含 OnTriggerEnter 函数的脚本组件附加到具有触发器的游戏对象上。

参数： OnTriggerEnter 函数带有一个参数，即 Collider other。这个参数表示与当前触发器相交的另一个碰撞体（通常是普通碰撞体）。您可以使用 other 参数来访问相交的碰撞体的信息。

实现逻辑： 在 OnTriggerEnter 函数中，您可以编写逻辑来响应碰撞。您可以根据相交的对象类型、标签等进行判断，并执行适当的操作，如触发事件、修改状态、改变分数等。
## 标签 CompareTag
在Unity中，标签（Tag）是一种用于标识游戏对象的字符串，您可以将标签附加到游戏对象上，以便在编程中识别和区分不同类型的对象。CompareTag 是一个常用的函数，用于比较游戏对象的标签，以确定它们是否匹配。以下是对 CompareTag 的简要介绍：

作用： CompareTag 函数用于检查一个游戏对象的标签是否与指定的标签匹配。它是在编写脚本时判断对象类型的常用方法。

用法： CompareTag 函数是 MonoBehaviour 类的一个成员函数，可以在脚本中使用。它接受一个字符串参数，用于指定要比较的标签。

返回值： CompareTag 函数返回一个布尔值，表示标签是否匹配。如果游戏对象的标签与传递的标签参数相匹配，函数将返回 true，否则返回 false。
## 触发器与普通碰撞体
在Unity中，触发器（Trigger）和普通碰撞体（Collider）都是用于处理游戏对象之间的碰撞和交互，但它们在实现方式和用途上存在一些区别：
> 普通碰撞体，会弹开。
> 触发器不会阻止物体运动，会发送触发事件。
1. **普通碰撞体（Collider）：**
   - 普通碰撞体用于定义游戏对象的实际碰撞形状，以确定物体之间的物理碰撞。
   - 当两个普通碰撞体相交时，它们会根据物理规则产生碰撞效果，如弹性、摩擦等。
   - 普通碰撞体可以用于实现物体之间的碰撞响应，比如物体之间互相推开、弹跳等。

2. **触发器（Trigger）：**
   - 触发器是一种特殊的碰撞体设置，可以被穿透而不会阻止物体的运动。
   - 当一个游戏对象的触发器与另一个游戏对象的碰撞体相交时，不会产生真实的物理碰撞效果。而是会发送碰撞事件，允许您在发生碰撞时执行自定义代码。
   - 触发器常用于实现触发事件，比如进入区域时触发、收集物品、触发对话等。


# 最初版

运动控制:
```csharp
    private void FixedUpdate()
    {
        Vector3 movement = new Vector3 (movementX, 0.0f, movementY);
        rb.AddForce(movement * speed);
    }
```
问题:没法精确控制小球移动;按键后,小球会一直受力,除非用相反的力去抵消.
解决:  // C#的协程功能
1.使用协程的方式控制移动:
```csharp
    public float smoothing = 1f; // 移动平滑度
    public Vector3 Target
    {
        get { return target; }
        set
        {
            target = value; // 设置目标位置

            StopCoroutine("Movement"); // 停止之前的移动协程
            StartCoroutine("Movement", target); // 启动新的移动协程，传递目标位置
        }
    }
    
    private Vector3 target; // 目标位置

    // 移动协程方法，接受目标位置的参数
    IEnumerator Movement(Vector3 target)
    {
        // 在物体与目标位置的距离大于0.05时执行循环
        while (Vector3.Distance(transform.position, target) > 0.05f)
        {
            // 使用Vector3.Lerp来平滑移动物体向目标位置
            transform.position = Vector3.Lerp(transform.position, target, smoothing * Time.deltaTime);

            yield return null; // 在每次迭代后等待一帧
        }
    }
```
2.通过鼠标点击确定运动位置:
```csharp
    void OnMouseDown()
    {
        // 从鼠标位置发射射线
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;

        // 进行射线检测
        Physics.Raycast(ray, out hit);

        // 检查射线是否击中了当前物体
        if (hit.collider.gameObject == gameObject)
        {
            // 计算新的目标位置，将其稍微抬高
            Vector3 newTarget = hit.point + new Vector3(0, 0.5f, 0);

            // 将新的目标位置设置为PropertiesAndCoroutines脚本中的属性
            coroutineScript.Target = newTarget;
        }
    }
```
# 鼠标控制:

问题:鼠标点击的精确度不够
解决:通过按键控制,让小球在当前位置移动一小段距离 //C#的事件
1.按钮点击作为一个事件,点击按钮后,触发事件
```csharp
using UnityEngine;
using System.Collections;

public class EventManager : MonoBehaviour 
{
    // 定义一个委托类型 ClickAction
    public delegate void ClickAction();
    
    // 声明一个静态事件 OnClicked，其他类可以订阅这个事件
    public static event ClickAction OnClicked;

    void OnGUI()
    {
        // 在屏幕中央创建一个按钮
        if (GUI.Button(new Rect(Screen.width / 2 - 50, 5, 100, 30), "Click"))
        {
            // 检查事件是否有订阅者，然后触发事件
            if (OnClicked != null)
                OnClicked();
        }
    }
}
```
2.小球订阅事件
```csharp
void OnEnable()
{
    // 当脚本启用时，订阅 UiController 中的 OnClicked 事件
    UiController.OnClickedUp += moveup;
    UiController.OnClickedDown += movedown;
    UiController.OnClickedRight += moveright;
    UiController.OnClickedLeft += moveleft;

}

void OnDisable()
{
    // 当脚本禁用时，取消订阅 UiController 中的 OnClicked 事件
    UiController.OnClickedUp -= moveup;
    UiController.OnClickedDown -= movedown;
    UiController.OnClickedLeft -= moveleft;
    UiController.OnClickedRight -= moveright;
}

void moveright()
{
    rb.velocity = Vector3.zero;
    coroutineScript.Target = transform.position + new Vector3(1f, 0f, 0f);
}

void moveleft()
{
    rb.velocity = Vector3.zero;
    coroutineScript.Target = transform.position + new Vector3(-1f, 0f, 0f);
}
```

# 按钮控制:
