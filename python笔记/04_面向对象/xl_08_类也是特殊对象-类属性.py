class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    # 类属性：与类相关的属性
    count = 0

    # 实例方法
    def __init__(self, name):
        self.name = name

        # 每次创建对象都让 类属性的值加一
        Tool.count += 1

    # 类方法,前面要写@classmethod
    @classmethod
    def show_tool_count(cls):
        print(cls.count)

    # 静态方法:不访问实例属性 也不访问类属性
    @staticmethod
    def static():
        print("静态方法")


# 创建工具
tool1 = Tool("1")

# 输出工具数目
print(Tool.count)

# 可以用对象调用类属性，python先在tool1对象中查找count，
# 找不到，会向上查找类中有没有count
# 不推荐
print(tool1.count)

# 注意
# 使用tool1.count = 99 相当于在对象tool1中创建了一个count属性
tool1.count = 99
print(tool1.count)
print(Tool.count)

tool2 = Tool("2")
# 使用类方法
Tool.show_tool_count()

# 调用静态方法
Tool.static()
