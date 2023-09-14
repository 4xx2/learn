class People:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return " %s 的体重是 %.1f" % (self.name, self.weight)

    def eat(self):
        print("吃一次增加一公斤")
        self.weight = self.weight + 1

    def run(self):
        print("跑步一次减少0.5公斤")
        self.weight = self.weight - 0.5


xming = People("小明", 75.0)
print(xming)
xming.eat()
xming.run()
print(xming)
