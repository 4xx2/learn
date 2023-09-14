class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        # 判断能否装入数量的子弹
        if count > self.model - self.bullet_count:
            print("没有足够空间")
            return
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count < 1:
            print("没有子弹")
            return
        self.bullet_count -= 1


class Soldier:
    def __init__(self, name):
        self.name = name
        # 新兵没有枪
        self.gun = None

    def fire(self):
        # 判断有没有枪
        # is 是身份运算符用于比较两个对象内存地址是否一致
        # == 是判断 变量的值是否相等  is 是判单两个对象是否是一个
        if self.gun is None:
            print("没有枪")
            return

        # 枪里有没有子弹
        if self.gun.bullet_count > 0:
            self.gun.shoot()
        else:
            self.gun.add_bullet(10)
            self.gun.shoot()
        print("突突突")


# 创建ak47
ak47 = Gun(50)
# 创建士兵许三多
xsd = Soldier("许三多")
# 给士兵一把枪
xsd.gun = ak47

xsd.fire()
