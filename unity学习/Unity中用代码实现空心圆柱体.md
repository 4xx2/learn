# Unity中用代码实现空心圆柱体
## mesh
在计算机图形学和三维图形渲染中，"Mesh"（网格）是一个常用的概念，用于描述三维模型的表面几何形状。它由一组顶点、边和面组成，定义了物体的外形和结构。网格是构建和渲染三维场景的基本元素之一。

具体来说，一个Mesh包含以下几个重要的元素：
**顶点**（Vertices）：顶点是三维空间中的一个点，通常由坐标（X、Y、Z）表示。多个顶点构成了物体的外形。**Vector3表示三维点，还有Vector2和Vector4。** 在网格中，每个顶点都可以包含额外的信息，如法线（用于光照计算）、纹理坐标（用于贴图）等。
**边**（Edges）：边是连接两个顶点的线段，定义了网格的几何形状。边在渲染过程中通常不直接显示，而是通过连接顶点的方式来定义面。
**面**（Faces）：面是由三个或四个顶点组成的多边形，用于定义物体的外形。面的组合形成了物体的几何形状。在三维图形中，三角形是最常见的面，因为它可以简单且有效地表示任何多边形。

Mesh在三维图形中扮演着重要的角色，它们被用于表示物体的外观、形状和结构。三维建模工具可以用来创建和编辑Mesh，而在图形引擎中，Mesh通常是由模型文件中的顶点、法线、纹理坐标等数据构建而成。在渲染时，图形引擎会处理Mesh的数据，并根据材质、光照等进行渲染，最终呈现出逼真的三维场景。
## 四面体模型的mesh
这段代码演示了在Unity中使用Mesh来创建一个简单的四面体模型。这个四面体模型是由四个顶点和四个三角形组成的。
**详细说明**
```csharp
Mesh mesh = new Mesh(); // 创建一个新的Mesh

// 定义四个顶点坐标
Vector3 p0 = new Vector3(0, 0, 0);
Vector3 p1 = new Vector3(1, 0, 0);
Vector3 p2 = new Vector3(0.5f, 0, Mathf.Sqrt(0.75f));
Vector3 p3 = new Vector3(0.5f, Mathf.Sqrt(0.75f), Mathf.Sqrt(0.75f) / 3);

// 计算顶点坐标的中心
Vector3 center = (p0 + p1 + p2 + p3) / 4;

// 将顶点坐标调整为以中心为原点的单位向量
p0 = (p0 - center).normalized;
p1 = (p1 - center).normalized;
p2 = (p2 - center).normalized;
p3 = (p3 - center).normalized;

// 设置Mesh的顶点坐标和三角形索引
mesh.vertices = new Vector3[] { p0, p1, p2, p3 };
mesh.triangles = new int[]{
   0,1,2,
   0,2,3,
   2,1,3,
   0,3,1
};

// 将Mesh赋值给MeshFilter组件以显示在场景中
MeshFilter meshFilter = GetComponent<MeshFilter>();
if (meshFilter == null)
    meshFilter = gameObject.AddComponent<MeshFilter>();
meshFilter.mesh = mesh;
```

通过上述代码，你在Unity中创建了一个四面体模型。这个代码块的主要步骤包括：

1. 创建一个新的`Mesh`对象。
2. 定义四个顶点的坐标，并计算这些坐标的中心。
3. 将顶点坐标调整为以中心为原点的单位向量。
4. 设置`Mesh`的顶点坐标和三角形索引，以定义四个三角形。
5. 将创建的`Mesh`赋值给一个物体的`MeshFilter`组件，从而将模型渲染到场景中。

这段代码演示了如何通过定义顶点和三角形来手动创建一个简单的几何模型。在实际开发中，可以使用更复杂的技术和工具来创建更复杂的模型。
## 完整代码
```csharp
public class CreateHollowClinderCreateEditor
{
    static Vector3 ptStart = new Vector3(-10.0f, 0f, 0f);//定义起始点
    static Vector3 ptEnd = new Vector3(80.0f, 0f, 0f);//定义终止点，后续用
    static float innerRadius = 10.0f, outterRadius = 11.0f;//内径和外径
    static string meshPrefabPath = "Assets/Models/Mesh/";//圆锥Mesh保存路径
    static string meshName = "HollowClinder.asset";//圆锥Mesh的名称为
    //unity可以自定义菜单项，右键3D Object/HollowClinder
    [MenuItem("GameObject/3D Object/HollowClinder", false, priority = 8)]

    public static void CreateHollowClinder()
    {//静态方法，调用类时执行；
        SpawnHollowClinderInHierarchy();
    }

    public static GameObject SpawnHollowClinderInHierarchy()
    {
        Mesh chunkMesh = new Mesh();
        if (!File.Exists(meshPrefabPath + meshName))
        {
            //计算垂直于轴的起始向量
            Vector3 vec1 = ptEnd - ptStart;

            //Vector3.up:一个预定义的 Vector3 静态变量，表示一个指向上方向的单位向量。在Unity中，这个向量的值是 (0, 1, 0)
            Vector3 vec2 = Vector3.up;
            float a = Vector3.Angle(vec1, vec2);//计算两个向量之间的夹角
            if (Mathf.Approximately(a, 0.0f))//判断浮点数是否近似相等
            {
                vec2 = Vector3.right;//bector3的静态变量，指向右的单位向量
            }
            Vector3 vecStart = Vector3.Cross(vec1, vec2);//cross计算两个向量的叉积（叉乘）//右手法则

            //**计算开始面内圆点、外圆点，结束面内圆点、外圆点**
            List<Vector3> pointsStartInner = new List<Vector3>();
            List<Vector3> pointsStartOutter = new List<Vector3>();
            List<Vector3> pointsEndtInner = new List<Vector3>();
            List<Vector3> pointsEndOutter = new List<Vector3>();

            //对象初始化时objStartInner.transform.position为（0，0，0）
            GameObject objStartInner = GameObject.CreatePrimitive(PrimitiveType.Sphere);//创建球体对象
            GameObject objStartOutter = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            GameObject objEndInner = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            GameObject objEndOutter = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            objStartInner.transform.position = ptStart + innerRadius * vecStart.normalized;
            objStartOutter.transform.position = ptStart + outterRadius * vecStart.normalized;
            objEndInner.transform.position = ptEnd + innerRadius * vecStart.normalized;
            objEndOutter.transform.position = ptEnd + outterRadius * vecStart.normalized;//normalized用于获取该向量的单位向量

            int devide = 30;//圆划分为多少等分
            float angleStep = 360.0f / (float)devide;

            float ang = 0.0f;
            for (ang = 0.0f; ang < 360.0f; ang += angleStep)
            {
                objStartInner.transform.RotateAround(ptStart, vec1, angleStep);//绕轴vec1旋转，开始点是ptStart，转角度是angleStep
                objStartOutter.transform.RotateAround(ptStart, vec1, angleStep);
                objEndInner.transform.RotateAround(ptEnd, vec1, angleStep);
                objEndOutter.transform.RotateAround(ptEnd, vec1, angleStep);

                pointsStartInner.Add(objStartInner.transform.position);
                pointsStartOutter.Add(objStartOutter.transform.position);
                pointsEndtInner.Add(objEndInner.transform.position);
                pointsEndOutter.Add(objEndOutter.transform.position);
            }
            GameObject.DestroyImmediate(objStartInner);//销毁游戏对象
            GameObject.DestroyImmediate(objStartOutter);
            GameObject.DestroyImmediate(objEndInner);
            GameObject.DestroyImmediate(objEndOutter);

            //**构建曲面**
            List<Vector3> vertexs = new List<Vector3>();
            //AddRange用于将另一个列表的所有元素添加到当前列表中
            vertexs.AddRange(pointsStartInner);//开始面内圆点
            vertexs.AddRange(pointsEndtInner); //结束面内圆点
            vertexs.AddRange(pointsStartOutter);//开始面外圆点
            vertexs.AddRange(pointsEndOutter); //结束面外圆点


            List<int> triangles = new List<int>();
            //构建内表面
            int startIndex = 0 * devide;
            int EndIndex = 0 * devide + devide;
            for (int i = startIndex; i < EndIndex; i++)
            {
                //边界面处
                int iNext = i + 1;
                int dNext = i + devide + 1;
                if (iNext >= startIndex + devide)
                    iNext = startIndex;

                if (dNext >= startIndex + 2 * devide)
                    dNext = startIndex + devide;

                triangles.Add(i);
                triangles.Add(i + devide);
                triangles.Add(iNext);

                triangles.Add(iNext);
                triangles.Add(i + devide);
                triangles.Add(dNext);
            }

            //构建外表面
            startIndex = 2 * devide;
            EndIndex = 2 * devide + devide;
            for (int i = startIndex; i < EndIndex; i++)
            {
                //边界面处
                int iNext = i + 1;
                int dNext = i + devide + 1;
                if (iNext >= startIndex + devide)
                    iNext = startIndex;

                if (dNext >= startIndex + 2 * devide)
                    dNext = startIndex + devide;

                triangles.Add(i);
                triangles.Add(iNext);
                triangles.Add(i + devide);

                triangles.Add(iNext);
                triangles.Add(dNext);
                triangles.Add(i + devide);
            }

            //构建上表面
            startIndex = 0 * devide;
            EndIndex = 0 * devide + devide;
            for (int i = startIndex; i < EndIndex; i++)
            {
                //边界面处
                int iNext = i + 1;
                int dNext = i + 2 * devide + 1;
                if (iNext >= startIndex + devide)
                    iNext = startIndex;

                if (dNext >= startIndex + 3 * devide)
                    dNext = startIndex + 2 * devide;

                triangles.Add(i);
                triangles.Add(iNext);
                triangles.Add(i + 2 * devide);

                triangles.Add(iNext);
                triangles.Add(dNext);
                triangles.Add(i + 2 * devide);
            }

            //构建下表面
            startIndex = 1 * devide;
            EndIndex = 1 * devide + devide;
            for (int i = startIndex; i < EndIndex; i++)
            {
                //边界面处
                int iNext = i + 1;
                int dNext = i + 2 * devide + 1;
                if (iNext >= startIndex + devide)
                    iNext = startIndex;

                if (dNext >= startIndex + 3 * devide)
                    dNext = startIndex + 2 * devide;

                triangles.Add(i);
                triangles.Add(i + 2 * devide);
                triangles.Add(iNext);

                triangles.Add(iNext);
                triangles.Add(i + 2 * devide);
                triangles.Add(dNext);
            }
            chunkMesh.vertices = vertexs.ToArray();
            chunkMesh.triangles = triangles.ToArray();

            chunkMesh.RecalculateNormals();//重新计算Mesh的法线
            /*法线用于渲染表面的光照效果，如果Mesh的顶点数据发生了变化，
            可能需要重新计算法线以确保渲染效果正确。*/
            chunkMesh.RecalculateBounds();
            /*重新计算Mesh的边界框（Bounds）。边界框是一个盒子，完全包围了Mesh，它在渲染、碰撞等方面有用。*/
            if (!Directory.Exists(meshPrefabPath))
            /* 检查指定的文件夹路径是否存在，如果不存在，则创建一个文件夹。这是为了确保保存Mesh的路径存在。*/
                Directory.CreateDirectory(meshPrefabPath);
            AssetDatabase.CreateAsset(chunkMesh, meshPrefabPath + meshName);
            AssetDatabase.SaveAssets();//保存assets
            AssetDatabase.Refresh();//刷新Asset数据库
        }
        else
        {/*
        AssetDatabase.LoadAssetAtPath<Mesh>(meshPrefabPath + meshName):
         这是一个调用 Unity 的 AssetDatabase 类的方法。
         它的作用是在指定路径下加载一个资源，并将其转换为 Mesh 类型。
         在这里，meshPrefabPath + meshName 是资源的完整路径，其中 meshPrefabPath 是文件夹路径，meshName 是文件名。
         <Mesh> 表示你希望将加载的资源转换为 Mesh 类型。
         注意，这段代码需要在Unity编辑器中运行，因为它使用了 AssetDatabase 类，
         这是一个编辑器特有的类，不适用于游戏运行时。
        */
            chunkMesh = AssetDatabase.LoadAssetAtPath<Mesh>(meshPrefabPath + meshName);
        }

        GameObject obj = new GameObject("HollowClinder");
        MeshFilter mf = obj.AddComponent<MeshFilter>();
        MeshRenderer mr = obj.AddComponent<MeshRenderer>();
        mr.material = new Material(Shader.Find("Standard"));
        mf.sharedMesh = chunkMesh;
        return obj;
    }
}
```

