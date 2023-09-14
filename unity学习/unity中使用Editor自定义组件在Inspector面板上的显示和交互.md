# unity中使用Editor自定义组件在Inspector面板上的显示和交互
# 代码使用介绍
```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor; // 导入编辑器

[CustomEditor(typeof(MeshCreator))]
public class GeneratorEditor : Editor //继承Editor，用于自定义MeshCreator组件的Inspector界面。
{
    public override void OnInspectorGUI()//这个方法是一个自定义编辑器的入口点，在这里你可以自定义组件的Inspector面板。
    {
        DrawDefaultInspector();//这个方法绘制了组件默认的Inspector界面

        //target 是一个特殊的关键字，表示当前正在编辑的组件或对象的目标
        MeshCreator script = (MeshCreator)target;//获取当前编辑的MeshCreator组件。

        //GUILayout.Button 是一个Unity GUI布局函数，用于创建一个按钮，并返回一个布尔值来表示按钮是否被点击。
        if (GUILayout.Button("Create Mesh"))
        {
            script.CreateMesh();
        }
    }
}
```
