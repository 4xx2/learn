---
title: "unity笔记"
output:
    word_document:
        path: unity笔记.docx
        toc: true
        toc_depth: 3
        number_sections: true
---
# 创建属性
在C#中，属性（Property）是一种特殊的成员，用于封装类的字段（字段是类中存储数据的变量）并提供对它们的访问方法。属性允许你定义一种方式来控制类中数据的读取和写入，同时提供了类似字段的访问语法，使得代码更加清晰和易读。

属性通常由两个访问器方法组成，分别是"get"和"set"方法，用于获取和设置属性的值。这些方法允许你在访问属性时执行特定的逻辑，例如验证输入或计算属性的值。

```csharp
using UnityEngine;
using System.Collections;

public class Player
{
    //成员变量可以称为字段。
    private int experience;

    //Experience 是一个基本属性
    public int Experience
    {
        // 可以通过去掉get/set方法，将属性设置为只写/只读
        get
        {
            //其他一些代码
            return experience;
        }
        set
        {
            //其他一些代码
            experience = value;
        }
    }

    //Level 是一个将经验值自动转换为玩家等级的属性
    public int Level
    {
        get
        {
            return experience / 1000;
        }
        set
        {
            experience = value * 1000;
        }
    }

    // 属性的简写！！
    //这是一个自动实现的属性的示例
    public int Health{ get; set;}
}
```
```csharp
using UnityEngine;
using System.Collections;

public class Game : MonoBehaviour 
{
    void Start () 
    {
        Player myPlayer = new Player();

        //属性可以像变量一样使用
        myPlayer.Experience = 5;
        int x = myPlayer.Experience;
    }
}
```
# 三元运算符
```csharp
    //这是一个三元运算的示例，其中根据
    //变量“health”选择一条消息。
    message = health > 0 ? "Player is Alive" : "Player is Dead";
```
# 泛型
C# 中的泛型是一种强大的编程特性，允许你编写具有参数化类型的代码，以增加代码的灵活性、可重用性和类型安全性。泛型允许你定义类、结构、方法和委托等，这些可以在运行时指定具体的数据类型。

以下是关于 C# 泛型的一些重要概念和用法：

1. **泛型类（Generic Classes）**：
   - 使用泛型类，你可以创建一个在实例化时指定类型参数的类。这样的类通常用于容器类、数据结构和算法。
   - 例如，C# 中的 `List<T>` 类是一个泛型类，你可以创建 `List<int>` 以存储整数，或者 `List<string>` 以存储字符串。

```csharp
List<int> intList = new List<int>();
intList.Add(1);
intList.Add(2);
```

2. **泛型方法（Generic Methods）**：
   - 除了泛型类，C# 还支持泛型方法，这允许你在方法级别使用类型参数。
   - 泛型方法可以在不同的数据类型上工作，而不需要为每个数据类型编写不同的方法。
   
```csharp
public T Max<T>(T a, T b) where T : IComparable<T>
{
    return a.CompareTo(b) > 0 ? a : b;
}
```

3. **泛型约束（Generic Constraints）**：
   - 你可以使用泛型约束来限制允许的类型参数。这可以通过 `where` 关键字来实现。
   - 例如，你可以使用 `where T : IComparable<T>` 约束来确保类型 `T` 实现了 `IComparable<T>` 接口，以便在 `Max` 方法中进行比较。
   - `where`约束通常有四类：class（引用类型）、struct（值类型）、new（）（不含参数的公共构造函数）、MonoBehaviour（该类及其衍生类）、接口。

4. **泛型接口（Generic Interfaces）**：
   - C# 中的接口也可以是泛型的，这意味着你可以定义可以在不同数据类型上实现的泛型接口。
   
```csharp
public interface IRepository<T>
{
    T GetById(int id);
    void Add(T entity);
}
```

5. **协变性和逆变性（Covariance and Contravariance）**：
   - C# 4.0 引入了协变性和逆变性，这允许你在泛型类型之间建立更灵活的转换关系。这在委托、接口和数组等情境中特别有用。

```csharp
IEnumerable<Animal> animals = new List<Dog>(); // 协变性
Action<Derived> action = (Base b) => { /*...*/ }; // 逆变性
```

泛型在 C# 中广泛应用，它们提供了类型安全性和代码重用的好处。通过在编译时进行类型检查，泛型使得代码更加健壮，并且能够减少不必要的装箱和拆箱操作，提高了性能。泛型使得你能够编写更加通用和可扩展的代码，而不需要针对每种数据类型编写大量重复的代码。
# 继承
在派生类中，如果不使用 base 关键字来显式调用基类构造函数，则将隐式调用无参数构造函数（若有）。
如果基类没有提供无参数构造函数，派生类必须使用 base 显式调用基类构造函数。
```csharp
//这是基类，
//也称为父类。
public class Fruit 
{
    public string color;
    
    //这是 Fruit 类的第一个构造函数，
    //不会被任何派生类继承。
    public Fruit() 
    {
        color = "orange";
        Debug.Log("1st Fruit Constructor Called");
    }

    //这是 Fruit 类的第二个构造函数，
    //不会被任何派生类继承。
    public Fruit(string newColor)
    {
        color = newColor;
        Debug.Log("2nd Fruit Constructor Called");
    }
}

public class Apple : Fruit 
{
    //这是 Apple 类的第一个构造函数。
    //它立即调用父构造函数，甚至
    //在它运行之前调用。
    public Apple() 
    {
        //注意 Apple 如何访问公共变量 color，
        //该变量是父 Fruit 类的一部分。
        color = "red";
        Debug.Log("1st Apple Constructor Called");
    }

    //这是 Apple 类的第二个构造函数。
    //它使用“base”关键字指定
    //要调用哪个父构造函数。
    public Apple(string newColor) : base(newColor)
    {
        //请注意，该构造函数不会设置 color，
        //因为基构造函数会设置作为参数
        //传递的 color。
        Debug.Log("2nd Apple Constructor Called");
    }
}
```
# 成员隐藏
在C#中，`new` 关键字在继承中主要用于成员隐藏（Member Hiding）。成员隐藏是一种子类（派生类）重新定义父类（基类）成员的行为，以改变其行为或提供不同的实现。当在子类中使用 `new` 关键字定义一个与父类成员名称相同的成员时，它会告诉编译器，子类的成员是一个新的成员，而不是继承自父类的成员。

以下是关于 `new` 关键字在继承中的主要作用：

1. **成员隐藏**：
   - 使用 `new` 关键字，子类可以隐藏父类的成员，包括方法、属性、字段等。
   - 当子类隐藏了父类的成员时，子类的成员和父类的成员具有相同的名称，但它们是两个不同的成员，而且没有覆盖父类的成员。

2. **编译时静态确定**：
   - 使用 `new` 关键字隐藏成员时，方法调用的解析是在编译时静态确定的，而不是在运行时动态确定的（这与方法覆盖不同）。
   - 这意味着无论使用父类还是子类的引用，都会调用该引用的声明类型中定义的成员。

3. **不支持多态性**：
   - 使用 `new` 关键字隐藏的成员不支持多态性（Polymorphism）。
   - 这意味着无论使用哪个类的引用，都会调用该引用类型中定义的成员，而不会根据实际对象的类型来确定。

```csharp
    // Enemy继承Humanoid，Orc继承Enemy；
    // Enemy和Orc的Yell方法用new修饰
        Humanoid human = new Humanoid();
        Humanoid enemy = new Enemy();
        Humanoid orc = new Orc();

        //注意每个 Humanoid 变量如何包含
        //对继承层级视图中
        //不同类的引用，但每个变量都调用 Humanoid Yell() 方法。
        human.Yell();
        enemy.Yell();
        orc.Yell();
        // 继承时，使用new修饰方法，调用时，由编译类型决定调用哪个方法
```

展示了如何在子类中使用 `new` 关键字来隐藏父类的方法。请注意，成员隐藏通常用于需要在子类中提供不同行为或更改成员实现的情况。如果你希望支持多态性，并在运行时根据对象的实际类型来确定调用的方法版本，可以使用方法覆盖（使用 `virtual` 和 `override` 关键字）来实现。

#####  "编译时类型"（Compile-Time Type）和 "运行时类型"（Runtime Type）
在编程中，有两个重要的类型相关概念，它们是 "编译时类型"（Compile-Time Type）和 "运行时类型"（Runtime Type）。这两个概念用于描述变量或表达式在编译时和运行时的类型信息。

1. **编译时类型（Compile-Time Type）**：
   - 编译时类型是指编译器在编译代码时所知道的类型。它是根据变量或表达式的声明来确定的，通常是在代码编写期间就已经确定的。
   - 编译时类型通常决定了哪些成员（方法、属性、字段等）可以访问，以及编译时是否可以通过编译器的类型检查。

```csharp
Animal animal = new Dog(); // 编译时类型是 Animal
```

在上述示例中，`animal` 的编译时类型是 `Animal`，因为它是根据声明的类型 `Animal` 而不是实际对象类型来确定的。

2. **运行时类型（Runtime Type）**：
   - 运行时类型是指在程序实际运行时，变量或表达式所引用的对象的类型。它是在运行时根据对象的实际类型来确定的。
   - 运行时类型通常决定了哪些方法和成员实际上会被调用。

```csharp
Animal animal = new Dog(); // 运行时类型是 Dog
```

在上述示例中，`animal` 的运行时类型是 `Dog`，因为它实际上引用了一个 `Dog` 类型的对象。

编译时类型和运行时类型的区别在于，编译时类型是在编译代码时静态确定的，而运行时类型是在程序实际运行时动态确定的。这是多态性（Polymorphism）的一个关键概念，多态性允许在运行时根据对象的实际类型来调用适当的方法。
# 覆盖
在C#中，`virtual` 和 `override` 是用于实现方法覆盖（Method Overriding）和多态性（Polymorphism）的关键字。它们通常用于继承层次结构中，以允许派生类重写基类中的方法。

1. **virtual 关键字**：
   - `virtual` 关键字用于基类中的方法声明，表示该方法可以在派生类中被重写。
   - 基类中的虚拟方法有一个默认的实现，但可以被派生类重写以提供不同的实现。
   - 虚拟方法允许多态性，这意味着在运行时，根据对象的实际类型来调用适当的方法版本。

2. **override 关键字**：
   - `override` 关键字用于派生类中的方法声明，表示该方法是对基类中虚拟方法的重写。
   - 重写方法必须具有与基类中虚拟方法相同的名称、参数列表和返回类型。
   - 重写方法可以提供不同的实现，覆盖基类中的虚拟方法。

```csharp
public class Animal
{
    public virtual void MakeSound()
    {
        Console.WriteLine("Animal makes a sound");
    }
}

public class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Dog barks");
    }
}
```

在上述示例中，`MakeSound` 方法在基类 `Animal` 中被声明为虚拟方法，允许派生类 `Dog` 通过使用 `override` 来提供不同的实现。当你创建 `Dog` 类的对象并调用 `MakeSound` 方法时，将根据对象的实际类型调用适当版本的方法。

# 扩展方法（Extension Methods）
C# 中的扩展方法（Extension Methods）是一种强大的功能，它允许你向现有的类型添加新的方法，而无需修改原始类型的定义。扩展方法通常用于为.NET框架中的内置类型或自定义类型添加额外的功能，提高代码的可读性和可维护性。

以下是有关C#中扩展方法的重要信息：

**扩展方法的定义**：
   - 扩展方法必须定义在静态类中。
   - 扩展方法必须是静态方法。
   - 第一个参数必须使用 this 关键字修饰，并指定要扩展的类型。这个参数是方法的目标类型，表示你要为哪种类型添加新的方法。
   - 扩展方法的定义示例：
```csharp
//创建一个包含所有扩展方法的类
//是很常见的做法。此类必须是静态类。
public static class ExtensionMethods
{
    //扩展方法即使像普通方法一样使用，
    //也必须声明为静态。请注意，第一个
    //参数具有“this”关键字，后跟一个 Transform
    //变量。此变量表示扩展方法会成为
    //哪个类的一部分。
    public static void ResetTransformation(this Transform trans)
    {
        trans.position = Vector3.zero;
        trans.localRotation = Quaternion.identity;
        trans.localScale = new Vector3(1, 1, 1);
    }
}
```
**使用扩展方法**：
   - 在使用扩展方法之前，需要导入包含扩展方法的命名空间。// 命名空间类似java的包。
   - 扩展方法可以像实例方法一样调用，不过调用时不需要显式传递目标类型的实例。
   - 使用扩展方法的示例：

```csharp
using UnityEngine;
using System.Collections;

public class SomeClass : MonoBehaviour 
{
    void Start () {
        //请注意，即使方法声明中
        //有一个参数，也不会将任何参数传递给
        //此扩展方法。调用此方法的
        //Transform 对象会自动作为
        //第一个参数传入。
        transform.ResetTransformation();
    }
}
```

**扩展方法的命名习惯**：
   - 扩展方法通常以目标类型的名称作为前缀，以便清晰地表示它是一个扩展方法。
   - 示例：如果扩展 `string` 类型，方法名称可以以 `String` 作为前缀。

**扩展方法的限制**：
   - 扩展方法不能修改原始类型的定义，只能添加新方法。
   - 扩展方法不能访问私有成员或内部状态，只能使用公共接口和公共成员。

扩展方法是C#中的一种强大功能，可以帮助你将代码组织得更清晰，并使其具有更好的可读性和可维护性。它们通常用于为第三方库或.NET框架中的类型添加自定义功能，以满足特定项目的需求，同时又不必修改这些类型的源代码。这使得扩展方法成为一种有用的工具，特别是在扩展或定制现有类库时。

# 命名空间
```csharp
using UnityEngine;
using System.Collections;

namespace SampleNamespace
{
    public class SomeClass : MonoBehaviour 
    {
        void Start () 
        {

        }
    }
}
```
在C#中，你可以使用命名空间中的类有多种方式，具体取决于你的代码的结构和需求。以下是几种常见的使用命名空间中的类的方法：

1. **使用完全限定名称**：
   - 这是最基本的方式，通过使用完全限定名称，你可以在不导入命名空间的情况下直接使用类。
   - 完全限定名称包括命名空间、类名和可能的嵌套类的名称。
   
```csharp
MyNamespace.MyClass myObject = new MyNamespace.MyClass();
```

2. **使用 `using` 语句导入命名空间**：
   - 使用 `using` 关键字导入命名空间，这样就可以在代码中直接使用命名空间中的类，而不需要使用完全限定名称。
   
```csharp
using MyNamespace;

MyClass myObject = new MyClass();
```

3. **使用别名**：
   - 可以为命名空间或类创建别名，以避免命名冲突或缩短名称。
   
```csharp
using alias = MyNamespace.MyClass;

alias myObject = new alias();
```

4. **静态导入**（仅适用于C# 6.0及更高版本）：
   - 可以使用 `using static` 关键字来导入命名空间中的静态成员，以便在代码中直接使用静态成员而不需要使用类名。
   
```csharp
using static MyNamespace.MyClass;

int result = MyStaticMethod();
```

5. **把类写在命名空间内**
这样可以在类中使用命名空间的类
```csharp
namespace SampleNamespace
{
    public class SomeClass : MonoBehaviour 
    {
        void Start () 
        {

        }
    }
}
```
# 列表和字典
```csharp
using UnityEngine;
using System.Collections;
using System; //这允许 IComparable 接口

//这是您将存储在
//不同集合中的类。为了使用
//集合的 Sort() 方法，此类需要
//实现 IComparable 接口。
public class BadGuy : IComparable<BadGuy>
{
    public string name;
    public int power;

    public BadGuy(string newName, int newPower)
    {
        name = newName;
        power = newPower;
    }

    //IComparable 接口需要
    //此方法。
    public int CompareTo(BadGuy other)
    {
        if(other == null)
        {
            return 1;
        }

        //返回力量差异。
        return power - other.power;
    }
}
```
```csharp
using UnityEngine;
using System.Collections;
using System.Collections.Generic; // 允许使用列表，字典

public class SomeClass : MonoBehaviour
{
    void Start () 
    {
        //这是创建列表的方式。注意如何在
        //尖括号 (< >) 中指定类型。
        List<BadGuy> badguys = new List<BadGuy>();

        //这里将 3 个 BadGuy 添加到列表
        badguys.Add( new BadGuy("Harvey", 50));
        badguys.Add( new BadGuy("Magneto", 100));
        badguys.Add( new BadGuy("Pip", 5));

        badguys.Sort();

        foreach(BadGuy guy in badguys)
        {
            print (guy.name + " " + guy.power);
        }

        //这会清除列表，使其
        //为空。
        badguys.Clear();
    }
}
```
```csharp
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class SomeOtherClass : MonoBehaviour 
{
    void Start ()
    {
        //这是创建字典的方式。注意这是如何采用
        //两个通用术语的。在此情况中，您将使用字符串和
        //BadGuy 作为两个值。
        Dictionary<string, BadGuy> badguys = new Dictionary<string, BadGuy>();

        BadGuy bg1 = new BadGuy("Harvey", 50);
        BadGuy bg2 = new BadGuy("Magneto", 100);

        //可以使用 Add() 方法将变量
        //放入字典中。
        badguys.Add("gangster", bg1);
        badguys.Add("mutant", bg2);

        BadGuy magneto = badguys["mutant"];

        BadGuy temp = null;

        //TryGetValue 这是一种访问字典中值的更安全
        //但缓慢的方法。
        if(badguys.TryGetValue("birds", out temp))
        {
            //成功！
        }
        else
        {
            //失败！
        }
    }
}
```

# 协程
以下是带有注释的C#脚本示例，它演示了如何使用协程在Unity中平滑地移动一个物体到目标位置，并在到达目标后等待一段时间后完成协程：

```csharp
using UnityEngine;
using System.Collections;

public class CoroutinesExample : MonoBehaviour
{
    public float smoothing = 1f; // 移动平滑度
    public Transform target; // 目标位置的Transform组件

    void Start ()
    {
        StartCoroutine(MyCoroutine(target)); // 启动协程
    }

    // 自定义协程方法，接受目标位置的Transform作为参数
    IEnumerator MyCoroutine (Transform target)
    {
        // 在物体与目标位置的距离大于0.05时执行循环
        while(Vector3.Distance(transform.position, target.position) > 0.05f)
        {
            // 使用Vector3.Lerp来平滑移动物体向目标位置
            transform.position = Vector3.Lerp(transform.position, target.position, smoothing * Time.deltaTime);

            yield return null; // 在每次迭代后等待一帧
        }

        print("Reached the target."); // 在到达目标后输出消息

        yield return new WaitForSeconds(3f); // 等待3秒钟

        print("MyCoroutine is now finished."); // 输出协程完成的消息
    }
}
```

上述代码使用了协程来实现平滑移动，通过 `Vector3.Lerp` 方法将物体移动到目标位置，然后等待3秒钟后完成协程。这是一个在Unity中常见的协程用法，用于实现平滑动画效果和延迟操作。

以下是带有注释的C#脚本示例，它演示了如何使用属性和协程在Unity中平滑地移动一个物体到目标位置：

```csharp
using UnityEngine;
using System.Collections;

public class PropertiesAndCoroutines : MonoBehaviour
{
    public float smoothing = 7f; // 移动平滑度
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
    IEnumerator Movement (Vector3 target)
    {
        // 在物体与目标位置的距离大于0.05时执行循环
        while(Vector3.Distance(transform.position, target) > 0.05f)
        {
            // 使用Vector3.Lerp来平滑移动物体向目标位置
            transform.position = Vector3.Lerp(transform.position, target, smoothing * Time.deltaTime);

            yield return null; // 在每次迭代后等待一帧
        }
    }
}
```

上述代码定义了一个名为 `PropertiesAndCoroutines` 的脚本，其中包含一个属性 `Target`，允许你设置物体的目标位置。当设置目标位置时，它会停止之前的移动协程并启动新的协程以平滑地移动物体到新的目标位置。这种结构允许你通过更改目标位置属性来控制物体的移动，而不需要手动管理协程的启动和停止。

以下是带有注释的C#脚本示例，它演示了如何使用点击事件设置物体的目标位置，该目标位置由 `PropertiesAndCoroutines` 脚本中的属性控制：
// 使用在环境对象上。
```csharp
using UnityEngine;
using System.Collections;

public class ClickSetPosition : MonoBehaviour
{
    public PropertiesAndCoroutines coroutineScript; // 引用PropertiesAndCoroutines脚本

    // 当鼠标点击物体时调用
    void OnMouseDown ()
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
}
```

这个脚本通过 `OnMouseDown` 方法监听鼠标点击事件。当鼠标点击当前物体时，它会发射一条射线从鼠标位置，检测射线是否与物体碰撞。如果射线击中了当前物体，它会计算一个新的目标位置（稍微抬高一点），然后将新的目标位置设置为 `PropertiesAndCoroutines` 脚本中的 `Target` 属性。这将触发 `PropertiesAndCoroutines` 脚本中的协程，使物体平滑地移动到新的目标位置。这种方法可用于实现点击移动物体的交互。

进行**射线检测的部分**，射线检测是一种常用的技术，通常用于确定从摄像机位置发出的射线是否与场景中的物体相交。下面我会对这段代码进行详细解释：

1. `Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);`：
   - 这一行代码创建了一条射线 `ray`。它使用了 `Camera.main` 来获取场景中主摄像机（Main Camera）的引用，并使用 `ScreenPointToRay` 方法将鼠标的屏幕坐标（`Input.mousePosition`）转换为一条射线。
   - 换句话说，它从摄像机的位置（通常是玩家视角的位置）沿着鼠标光标所在的屏幕坐标发射一条射线。

2. `RaycastHit hit;`：
   - 这一行代码声明了一个 `RaycastHit` 类型的变量 `hit`。`RaycastHit` 用于存储射线检测结果，包括被射线击中的物体的信息。

3. `Physics.Raycast(ray, out hit);`：
   - 这一行代码执行射线检测操作。它使用 `Physics.Raycast` 方法，将之前创建的射线 `ray` 发射到场景中，并将结果存储在 `hit` 变量中。
   - 如果射线与场景中的一个物体相交，那么 `Physics.Raycast` 会返回 `true`，表示射线击中了某个物体，并且 `hit` 变量中存储了被击中物体的信息。如果射线没有击中物体，则返回 `false`。

总结起来，这段代码的目的是在鼠标点击位置发射一条射线，然后检测该射线是否与场景中的任何物体相交。如果相交，`hit` 变量将包含关于被击中物体的信息，包括位置、法线等。这通常用于处理与鼠标点击相关的交互，例如在点击物体时执行某些操作，或确定点击位置是否在可交互物体上。

# 四元数
概念：
1. **欧拉角（Euler Angles）**：
   - 欧拉角是一种用于描述物体旋转的常见方式，它将旋转分解为绕坐标轴的三个基本旋转：俯仰（Pitch）、偏航（Yaw）和滚动（Roll）。
   - 俯仰围绕X轴旋转，偏航围绕Y轴旋转，滚动围绕Z轴旋转。
   - 尽管欧拉角直观且易于理解，但它们容易受到万向节锁问题的影响，这会导致在某些情况下失去部分旋转自由度。

2. **万向节锁（Gimbal Lock）**：
   - 万向节锁是指在使用欧拉角时可能遇到的问题，当两个旋转轴趋向于对齐时，可能会导致失去一个自由度。
   - 例如，当俯仰和滚动轴趋于对齐时，偏航轴的旋转将受到限制，从而导致旋转失去一部分自由度，这被称为万向节锁。
   - 为了解决这个问题，通常会使用四元数来代替欧拉角。

3. **四元数（Quaternions）**：
   - 四元数是一种用于表示旋转的数学工具，它具有四个分量（实部和虚部），通常表示为（w, x, y, z）。
   - 四元数在计算机图形学和游戏开发中广泛用于表示旋转，因为它们不容易受到万向节锁问题的影响，并且执行旋转操作更高效。
   - 四元数提供了一种紧凑的方式来表示旋转，可以通过插值来平滑过渡，例如在动画中使用。

总结来说，欧拉角是一种直观但容易受到限制的旋转表示方式，而四元数是一种更复杂但更强大的旋转表示方式，可以更好地处理复杂的旋转操作和避免万向节锁问题。在实际应用中，选择使用哪种方式通常取决于具体需求和场景。

在C#中，四元数（Quaternion）是一个用于表示三维空间中的旋转的数据类型。四元数是一种非常强大和有效的数学工具，特别在计算机图形学、游戏开发和机器人控制等领域中广泛应用。以下是关于C#中的四元数的重要信息：

**四元数的结构**：
   - 在C#中，四元数通常表示为一个具有四个分量的结构，分别是w、x、y和z。这四个分量一般用来表示旋转。
   - 四元数的结构通常如下所示：
     ```csharp
     struct Quaternion
     {
         public float w;
         public float x;
         public float y;
         public float z;
     }
     ```

**旋转表示**：
   - 四元数是一种非常灵活的方式来表示绕任意轴的旋转。一个四元数可以用来表示从一个方向到另一个方向的旋转。
   - 与欧拉角不同，四元数不容易受到万向节锁问题的影响，因此它们更适合处理复杂的旋转操作。

**创建四元数**：
   - 在C#中，可以使用`Quaternion`结构的构造函数或静态方法来创建四元数。
   - 例如，可以使用`Quaternion.Euler`创建一个表示欧拉角旋转的四元数，或者使用`Quaternion.AngleAxis`创建一个表示绕特定轴的旋转的四元数。

**旋转操作**：
   - 四元数支持一系列旋转操作，例如乘法、插值和转换。你可以将一个四元数与另一个四元数相乘来组合多个旋转，也可以使用`Quaternion.Lerp`和`Quaternion.Slerp`来插值两个四元数以实现平滑的旋转过渡。

`Quaternion.Lerp` 和 `Quaternion.Slerp` 都是Unity游戏引擎中用于插值（interpolate）两个四元数的函数。它们允许你在两个旋转之间创建平滑的过渡，用于实现旋转动画、相机控制和其他需要平滑旋转效果的情况。下面分别介绍这两个函数：

1. **Quaternion.Lerp**（线性插值）：
   - `Quaternion.Lerp` 用于在两个四元数之间进行线性插值，从一个旋转过渡到另一个旋转。
   - 语法：`Quaternion.Lerp(from, to, t)`，其中 `from` 是起始四元数，`to` 是目标四元数，`t` 是插值系数，通常在0到1之间。
   - `t` 值越接近0，结果越接近 `from`，`t` 值越接近1，结果越接近 `to`。
   - `Quaternion.Lerp` 提供了线性的插值，旋转速度在过渡过程中是恒定的，可能导致过渡不够平滑。

2. **Quaternion.Slerp**（球形插值）：
   - `Quaternion.Slerp` 用于在两个四元数之间进行球形插值，从一个旋转过渡到另一个旋转，保持旋转的球形插值特性。
   - 语法：`Quaternion.Slerp(from, to, t)`，同样，`from` 是起始四元数，`to` 是目标四元数，`t` 是插值系数。
   - `Quaternion.Slerp` 提供了球形插值，旋转速度在过渡过程中是变化的，以保持平滑的过渡。这通常导致更自然的旋转动画。


```csharp
using UnityEngine;
using System.Collections;

public class GravityScript : MonoBehaviour 
{
    public Transform target; // 目标点的Transform组件

    void Update () 
    {
        // 计算相对位置，使物体的前进方向指向目标点（稍微抬高一点）
        Vector3 relativePos = (target.position + new Vector3(0, 1.5f, 0)) - transform.position;

        // 计算旋转，使物体面向目标点
        Quaternion rotation = Quaternion.LookRotation(relativePos);

        // 获取当前物体的本地旋转
        Quaternion current = transform.localRotation;

        // 使用球形插值（Slerp）将当前旋转平滑地过渡到新旋转
        transform.localRotation = Quaternion.Slerp(current, rotation, Time.deltaTime);

        // 向前移动物体（模拟向目标点移动，这里每秒移动3个单位）
        transform.Translate(0, 0, 3 * Time.deltaTime);
    }
}

```

**LookRotation** 
`Quaternion.LookRotation` 是Unity游戏引擎中的一个函数，用于创建一个四元数（Quaternion），该四元数可以将一个游戏对象的Z轴方向指向给定的目标点或方向。这个函数通常用于控制游戏对象的朝向或旋转。

函数的一般语法如下：
```csharp
Quaternion.LookRotation(forward, upwards);
```
其中，参数含义如下：
- `forward`：一个表示游戏对象前进方向的向量，通常是指向目标点的向量。
- `upwards`（可选）：一个表示游戏对象上方方向的向量。如果不提供此参数，将默认为（0, 1, 0），即世界空间中的上方。

`Quaternion.LookRotation` 返回一个四元数，该四元数表示了游戏对象应该旋转的方向，以使其前进方向朝向 `forward`，并且上方方向与 `upwards` 参数所指定的方向一致。通常，你可以将这个返回的四元数应用于游戏对象的旋转。

```csharp
using UnityEngine;
using System.Collections;

public class LookAtScript : MonoBehaviour 
{
    public Transform target;


    void Update () 
    {
        // 使用LookRotation函数创建一个旋转四元数，将游戏对象指向目标点
        // 将游戏对象的旋转设置为新的旋转四元数
        Vector3 relativePos = target.position - transform.position;
        transform.rotation = Quaternion.LookRotation(relativePos);
    }
}
```

**性能和计算效率**：
   - 虽然四元数的数学运算相对复杂，但在实际计算中通常比欧拉角更高效，因为它们需要较少的计算和内存。

C#中的四元数是一种强大的工具，用于处理三维空间中的旋转。它们提供了一种灵活且有效的方式来表示和操作旋转，特别适用于需要精确控制和平滑动画效果的应用程序。在Unity等游戏引擎中，四元数是常用的旋转表示方式。

# 委托
该脚本演示了委托的基本功能和用法：
```csharp
using UnityEngine;

public class DelegateScript : MonoBehaviour 
{
    // 定义一个委托类型 MyDelegate，该委托可以关联接受整数参数的方法
    delegate void MyDelegate(int num);
    MyDelegate myDelegate; // 创建一个委托实例

    void Start () 
    {
        // 将委托关联到 PrintNum 方法
        myDelegate = PrintNum;

        // 调用委托，实际上会执行 PrintNum 方法
        myDelegate(50);

        // 将委托关联到 DoubleNum 方法
        myDelegate = DoubleNum;

        // 调用委托，实际上会执行 DoubleNum 方法
        myDelegate(50);
    }

    // 这是一个接受整数参数的方法，用于打印参数值
    void PrintNum(int num)
    {
        print ("Print Num: " + num);
    }

    // 这是另一个接受整数参数的方法，用于将参数值加倍并打印结果
    void DoubleNum(int num)
    {
        print ("Double Num: " + num * 2);
    }
}
```

这个脚本演示了如何使用委托来关联不同的方法，并通过委托来调用这些方法。委托允许你在运行时决定要调用哪个方法，从而增加了代码的灵活性和可扩展性。在这个示例中，`myDelegate` 可以关联两个不同的方法，并在运行时切换它们，然后通过调用委托来执行这些方法。

**多播委托**
下面是带有注释的 `MulticastScript` 脚本，该脚本演示了多播委托的用法：

```csharp
using UnityEngine;
using System.Collections;

public class MulticastScript : MonoBehaviour 
{
    // 声明一个多播委托类型 MultiDelegate，该委托不接受参数
    delegate void MultiDelegate();
    MultiDelegate myMultiDelegate; // 创建一个多播委托实例

    void Start () 
    {
        // 向多播委托添加两个方法，这两个方法将按照添加的顺序执行
        myMultiDelegate += PowerUp;
        myMultiDelegate += TurnRed;

        // 检查多播委托是否为空（null）
        if (myMultiDelegate != null)
        {
            // 调用多播委托，将执行 PowerUp 和 TurnRed 两个方法
            myMultiDelegate();
        }
    }

    // 这是第一个方法，用于打印一条消息
    void PowerUp()
    {
        print("Orb is powering up!");
    }

    // 这是第二个方法，用于改变对象的颜色为红色
    void TurnRed()
    {
        // 修改对象的材质颜色为红色
        renderer.material.color = Color.red;
    }
}
```

这个脚本演示了多播委托的用法。多播委托允许将多个方法关联到同一个委托实例上，并且在调用委托时，这些方法会按照它们被添加到委托的顺序执行。在这个示例中，`myMultiDelegate` 关联了两个方法 `PowerUp` 和 `TurnRed`，并且在调用委托时，这两个方法都会被执行。

多播委托在事件处理、消息传递和回调机制等方面非常有用，它允许你将多个方法注册到一个事件上，并以统一的方式触发它们。

# 特性
**[Range]**
下面是带有注释的 `SpinScript` 脚本，该脚本演示了如何使用特性 `[Range]`：

```csharp
using UnityEngine;
using System.Collections;

public class SpinScript : MonoBehaviour 
{
    // 使用 [Range(min, max)] 特性来限定 speed 字段的取值范围在 -100 到 100 之间
    [Range(-100, 100)] public int speed = 0;

    void Update () 
    {
        // 在每一帧中，根据 speed 的值绕 Y 轴旋转物体
        transform.Rotate(new Vector3(0, speed * Time.deltaTime, 0));
    }
}
```

在这个示例中，我们使用了 `[Range(min, max)]` 特性来限定 `speed` 字段的取值范围。这个特性允许编辑器在 Inspector 窗口中显示一个滑动条，让用户可以轻松设置 `speed` 的值，同时确保该值在 -100 到 100 的范围内。这是一个很常见的用例，用于在编辑器中调整参数值，而无需手动输入数字。

特性 `[Range]` 是 Unity 中常用的一个内置特性，用于提供更友好的编辑器界面，以便开发人员可以更轻松地调整参数值。注意，特性可以应用于字段、属性、方法等各种程序元素，以满足不同的需求。

**[ExecuteInEditMode]**
这是一个使用了 `[ExecuteInEditMode]` 特性的示例脚本。下面是对该脚本的简要介绍和注释：

```csharp
using UnityEngine;
using System.Collections;

// 使用 [ExecuteInEditMode] 特性，使脚本在编辑模式下也可以运行
[ExecuteInEditMode]
public class ColorScript : MonoBehaviour 
{
    void Start()
    {
        // 设置物体的共享材质颜色为红色
        renderer.sharedMaterial.color = Color.red;
    }
}
```

在这个示例中，`ColorScript` 脚本使用了 `[ExecuteInEditMode]` 特性，这意味着该脚本会在编辑模式下运行。通常情况下，Unity 中的脚本只在播放模式下才会运行，但使用了 `[ExecuteInEditMode]` 特性的脚本可以在编辑模式下执行，这对于一些编辑器扩展或自动化任务非常有用。

在 `Start` 方法中，脚本将物体的共享材质颜色设置为红色。这个示例演示了如何在编辑器中使用脚本来更改物体的属性，例如材质颜色。在编辑模式下运行脚本可以让你在编辑器中预览和调整这些属性，而不必进入播放模式。

# 事件
下面是带有注释的三个脚本，它们演示了使用事件来实现对象之间的通信：

### EventManager.cs

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

### TeleportScript.cs

```csharp
using UnityEngine;
using System.Collections;

public class TeleportScript : MonoBehaviour 
{
    void OnEnable()
    {
        // 当脚本启用时，订阅 EventManager 中的 OnClicked 事件
        EventManager.OnClicked += Teleport;
    }

    void OnDisable()
    {
        // 当脚本禁用时，取消订阅 EventManager 中的 OnClicked 事件
        EventManager.OnClicked -= Teleport;
    }

    void Teleport()
    {
        // 在事件触发时，随机改变物体的 Y 坐标
        Vector3 pos = transform.position;
        pos.y = Random.Range(1.0f, 3.0f);
        transform.position = pos;
    }
}
```

### TurnColorScript.cs

```csharp
using UnityEngine;
using System.Collections;

public class TurnColorScript : MonoBehaviour 
{
    void OnEnable()
    {
        // 当脚本启用时，订阅 EventManager 中的 OnClicked 事件
        EventManager.OnClicked += TurnColor;
    }

    void OnDisable()
    {
        // 当脚本禁用时，取消订阅 EventManager 中的 OnClicked 事件
        EventManager.OnClicked -= TurnColor;
    }

    void TurnColor()
    {
        // 在事件触发时，随机改变物体的材质颜色
        Color col = new Color(Random.value, Random.value, Random.value);
        renderer.material.color = col;
    }
}
```

这三个脚本一起演示了如何使用事件来触发不同的行为。`EventManager` 脚本包含一个 `ClickAction` 委托和一个静态事件 `OnClicked`，当按钮被点击时，会触发该事件。`TeleportScript` 和 `TurnColorScript` 分别订阅了 `OnClicked` 事件，并在事件触发时执行不同的操作，一个是随机改变物体的 Y 坐标，另一个是随机改变物体的材质颜色。这种方式实现了对象之间的松耦合通信，使它们可以独立地响应事件而无需直接调用彼此的方法。

事件和公开委托变量都允许对象之间进行通信，但它们有一些重要的区别：

**事件**：

1. **封装性**：事件是一种封装机制，它限制了对委托的直接访问。事件只能通过 `+=`（添加订阅者）和 `-=`（移除订阅者）来操作，不能像委托一样直接调用。

2. **安全性**：事件通常更安全，因为只允许添加和移除订阅者，不允许直接调用委托。这可以防止未经授权的代码触发事件。

3. **约定**：事件通常遵循一种命名约定，以 `EventName` 或 `SomethingHappened` 的形式命名，使代码更具可读性和一致性。

4. **适用性**：事件通常用于类外部（订阅者）与类内部（发布者）之间的通信，以实现松耦合。

示例：
```csharp
public class Button
{
    public event Action Clicked; // 声明一个事件

    public void OnClick()
    {
        if (Clicked != null)
            Clicked(); // 触发事件
    }
}
```

**公开委托变量**：

1. **可直接调用**：公开委托变量允许外部代码直接调用委托，这意味着外部代码可以随时触发委托。

2. **更少的封装**：委托变量的访问级别通常比事件更直接，因此更容易被外部代码滥用。

3. **适用性**：公开委托变量通常用于需要外部代码频繁触发委托的情况，或者用于公开事件的底层委托以供高级用户使用。

示例：
```csharp
public class Calculator
{
    public Func<int, int, int> Add; // 公开委托变量

    public Calculator()
    {
        Add = (a, b) => a + b; // 初始化委托
    }
}
```

总的来说，事件和公开委托变量都有各自的用途和优点。事件通常更适合实现发布-订阅模式，以确保代码的安全性和可维护性。公开委托变量适用于需要外部代码频繁触发委托的情况，但需要谨慎使用以确保代码的可靠性和安全性。