# 导入模块顺序：官方-》第三方-》应用程序
import random

import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 游戏帧率
FRAME_PER_SEC = 60
# 背景图像存储位置
BACKGROUND_BATH = "E:/Python/python笔记/images/background.png"
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 敌机图片位置
ENEMY_BATH = "E:/Python/python笔记/images/enemy1.png"
# 英雄图片位置
HERO = "E:/Python/python笔记/images/me1.png"
# 英雄发射子弹事件  _  用户事件是一个常量，让用户事件加一即可
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """背景 游戏精灵"""

    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__(BACKGROUND_BATH)
        # 判断是否是替换图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__(ENEMY_BATH)
        # 2.指定敌机初始随机速度
        self.speed = random.randint(2, 3)
        # 3.指定敌机初始随机位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        # 1.调用父类方法，保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，需要从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("从精灵组删除敌机")
            # kill方法可以将精灵从所有精灵组中移出，自动销毁
            self.kill()

    def __del__(self):
        # print("精灵删除会调用该方法销毁敌机")
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法，设置图片和速度
        super().__init__(HERO, speed=0)
        # 增加垂直方向速度
        self.speed2 = 0
        # 2.设置英雄初始位置
        self.rect.bottom = SCREEN_RECT.height - 120
        self.rect.centerx = SCREEN_RECT.centerx
        # 创建子弹精灵组属性
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed2
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y < 100:
            self.rect.y = 100
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        """发射子弹"""
        for i in (0, 1, 2):
            bullet = Bullet()

            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("E:/Python/python笔记/images/bullet1.png", speed=-2)

    def update(self):
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom <= 100:
            self.kill()
