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

3. **缩放：**
   - `localScale`：获取或设置物体的局部空间缩放。

4. **父子关系：**
   - `SetParent(Transform parent)`：设置物体的父对象。
   - `parent`：获取或设置物体的父对象。

5. **坐标转换：**
   - `TransformPoint(Vector3 position)`：将局部空间坐标转换为世界空间坐标。
   - `InverseTransformPoint(Vector3 position)`：将世界空间坐标转换为局部空间坐标。

6. **其它：**
   - `DetachChildren()`：解除物体与其所有子对象的父子关系。
   - `Find(string name)`：在子对象中查找具有指定名称的子对象。

## LookAt方法
在 Unity 中，LookAt 方法是 Transform 组件提供的一个功能，用于将一个物体的朝向（rotation）调整为面向另一个位置或物体。这在游戏开发中常用于实现目标跟随、视线对准等效果。
```csharp
//方法声明
public void LookAt(Transform target, Vector3 worldUp = Vector3.up);
```
这个方法会将调用它的物体的 旋转调整 为面向目标位置。调用后，物体的 Z 轴（前方）将指向目标位置，而 Y 轴（上方）将遵循给定的 worldUp 方向。这通常用于让一个物体或摄像头朝向另一个物体，以便实现目标跟随或视线对准。



## 对象移动
```csharp


// 限制目标位置在指定范围内
targetPosition.x = Mathf.Clamp(targetPosition.x, minX, maxX);
targetPosition.z = Mathf.Clamp(targetPosition.z, minZ, maxZ);

// 对象绕着 Y 轴旋转
// rotationAmount为旋转角度
transform.Rotate(Vector3.up, rotationAmount);

// 围绕目标对象进行旋转
transform.RotateAround(target.position, Vector3.up, rotationAmount);
```