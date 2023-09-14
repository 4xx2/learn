class Cat:
    # self 就表示调用方法的对象自己
    def eat(self):
        print("%s爱喝水" % self.name)

    # 初始化方法 两个下划线开头  __init__  初始化方法在创建对象时自动调用
    # def __init__(self):
    #     # 初始化时 定义属性
    #     self.name = "Tom"
    def __init__(self, new_name="cat"):
        self.name = new_name

    def __del__(self):
        print("del  对象 从内存中销毁时自动 调用")

    def __str__(self):
        # 必须返回一个字符串，当使用str方法时，
        # 后续print 将不再输出对象所在地址，而是print出该字符串
        return "我是猫 %s" % self.name


# 创建对象
tom = Cat("tom")

# 在类的外部可以给对象增加属性
# tom.name = "tom"
tom.eat()

# 使用print，可以看到这个对象对应的地址
print(tom)

# del 关键字可以删除对象
del tom
