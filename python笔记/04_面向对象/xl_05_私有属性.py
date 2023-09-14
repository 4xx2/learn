class Woman:
    def __init__(self, name, age):
        self.name = name
        # 属性前加__ 表示是私有属性
        self.__age = age

    # 方法前加__表示是私有方法，无法在对象外调用私有方法
    def secret(self):
        # 对象的方法内部，可以访问对象的私有属性
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaoMei = Woman("小美", 18)

# 外界不能访问私有属性
# print(xiaoMei.__age)
xiaoMei.secret()

# 如果想在外部访问私有属性或者方法，可以在前面加 _类名__属性/方法
print(xiaoMei._Woman__age)
