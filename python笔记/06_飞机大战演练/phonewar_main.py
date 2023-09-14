import pygame
import phonewar_tools

"""游戏初始化"""
pygame.init()

# 1.设置游戏窗口
screen = pygame.display.set_mode((480, 700))
# 2.创建游戏时钟
clock = pygame.time.Clock()
# 3.创建精灵、精灵组
phoneHero = phonewar_tools.PhoneHero("/06_飞机大战演练/images/me1.png")

phone_group = pygame.sprite.Group(phoneHero)

"""游戏循环"""
while True:
    # 1.设置刷新帧率
    clock.tick(60)
    # 2.事件监听
    for event in pygame.event.get():
        # 判断是否是退出事件
        if event.type == pygame.QUIT:
            pygame.quit()  # 卸载所有pygame 模块
            exit()  # python内置函数 将正在进行的程序终止

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                phoneHero.update("left")
            elif event.key == pygame.K_d:
                phoneHero.update("right")
            elif event.key == pygame.K_w:
                phoneHero.update("up")
            elif event.key == pygame.K_s:
                phoneHero.update("down")

    # 3.碰撞检测
    # 4.更新/绘制精灵
    phone_group.draw(screen)
    # 5.更新屏幕显示
    pygame.display.update()
