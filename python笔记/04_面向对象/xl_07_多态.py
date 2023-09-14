class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 在玩耍" % (self.name, dog.name))
        dog.game()


class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 简单玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 天上玩耍" % self.name)


person = Person("人")
dog1 = Dog("狗")
xiaoTianDog = XiaoTianDog("哮天犬")

person.game_with_dog(dog1)
person.game_with_dog(xiaoTianDog)
