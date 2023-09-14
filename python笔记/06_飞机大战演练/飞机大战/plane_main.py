import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战游戏  主程序类"""

    def __init__(self):
        print("游戏开始")
        # 1.设置游戏窗口 (最好不要直接把窗口大小的值直接输入）(建议把固定的数值设置为常量）
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，创建精灵、精灵组
        self.__create_sprites()
        # 4.设置定时器事件 -创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 5.定时器事件 -发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建精灵、精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.background_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵
            self.__update_sprites()
            # 5.更新屏幕显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                # 发射子弹
                self.hero.fire()

        # 使用方法获取键盘按键 - 按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断对应按键 索引值 1
        if keys_pressed[pygame.K_d]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_a]:
            self.hero.speed = -2
        elif keys_pressed[pygame.K_w]:
            self.hero.speed2 = -2
        elif keys_pressed[pygame.K_s]:
            self.hero.speed2 = 2
        else:
            self.hero.speed = 0
            self.hero.speed2 = 0

    def __check_collide(self):
        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # 2.敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表有内容，则碰到了敌机
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()
            # 游戏结束
            self.__game_over()

    def __update_sprites(self):
        self.screen.fill((0, 0, 0))  # 填充黑色，测试背景

        self.background_group.update()
        self.background_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()  # 卸载所有pygame 模块
        exit()  # python内置函数 将正在进行的程序终止


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
