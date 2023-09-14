import pygame
from 飞机大战演练.飞机大战 import plane_sprites

# 游戏循环前，是游戏初始化——》设置游戏窗口；绘制图像初始位置；设置游戏时钟；
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像数据
background = pygame.image.load("/06_飞机大战演练/images/background.png")
# 2.blit方法绘制图像
screen.blit(background, (0, 0))

# 绘制英雄图像
phone = pygame.image.load("/06_飞机大战演练/images/me1.png")
screen.blit(phone, (200, 500))

# update更新屏幕
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义 reck 类型 记录飞机的初始位置
phone_position = phone.get_rect()
phone_position.x = 200
phone_position.y = 500

# 创建敌机精灵
enemy = plane_sprites.Plane("E:/Python/python笔记/images/enemy1.png")
enemy1 = plane_sprites.Plane("E:/Python/python笔记/images/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环，意味着游戏正式开始——》设置刷新帧率；检测用户交互；更新图片位置；更新屏幕显示；
while True:
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        print(event)
        # 判断是否是退出事件
        if event.type == pygame.QUIT:
            pygame.quit()  # 卸载所有pygame 模块
            exit()  # python内置函数 将正在进行的程序终止

    # 飞机向上飞行
    phone_position.y -= 5

    if phone_position.y <= -126:
        phone_position.y = 700

    screen.blit(background, (0, 0))  # 绘制背景
    screen.blit(phone, phone_position)  # 绘制飞机

    # 让精灵组调用update，draw方法
    # update 让组中所有精灵更新位置
    # draw 在screen上绘制所有精灵
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()  # 更新屏幕
