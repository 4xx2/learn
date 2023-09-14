class Animal:
    def __init__(self, name):
        self.name = name

        # 私有属性/方法 不会被继承，
        # 子类可以通过继承的父类方法访问父类私有属性
        self.__num1 = 100

    # 静态方法：是使用static关键字修饰的方法，又叫类方法.属于类的，
    # 不属于对象， 在实例化对象之前就可以通过类名.方法名调用静态方法
    def drink(self):
        print("喝")

    def eat(self):
        print("%s 吃" % self.name)

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class B:
    def test(self):
        print("1234")


# 多继承
class Dog(Animal, B):
    def dark(self):
        print("汪汪")

    # 子类可以重写父类的方法
    def sleep(self):
        # 可以用super（）关键字 调用父类的方法
        super().sleep()
        print("狗睡觉")

        # 另一种调用父类方法的方法,需要使用父类名称
        # 不推荐使用 因为 更改父类后，需要更改
        Animal.sleep(self)


# 创建狗对象
wangCai = Dog("旺财")

wangCai.run()
wangCai.dark()
wangCai.eat()

# 子类重写方法后，子类对象只会调用重写的方法
wangCai.sleep()

# 多继承可以使用所有父类方法
wangCai.test()

# mro是python内置的方法，可以查看 方法搜索顺序
print(Dog.__mro__)
