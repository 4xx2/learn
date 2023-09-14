import pygame
import sys

pygame.init()

# 主屏幕
screen = pygame.display.set_mode((400, 700))
# 图片surface
plane = pygame.image.load("/06_飞机大战演练/images/me1.png")

# 获取图片位置信息(position相当于图片对应的矩形框？）
position = plane.get_rect()
print(position)
# 把图片矩形框的中心点设置到 屏幕正下方
position.center = (200, 650)
print(position.center)

screen.blit(plane, position)

# 子弹
bullet = pygame.image.load("/06_飞机大战演练/images/bullet1.png")
position2 = bullet.get_rect()

# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
while True:
    # 图片偏移量
    site = [0, 0]

    position2.center = (100, 650)
    site2 = [0, 4]

    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # 终止程序，确保退出程序
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                site[0] -= 10
            if event.key == pygame.K_d:
                site[0] += 10
    # 移动图像
    position = position.move(site)
    # 将界面填充黑色
    screen.fill((0, 0, 0), rect=(0, 0, 400, 700))

    screen.blit(plane, position)  # 绘制飞机
    screen.blit(bullet, position2)

    pygame.display.flip()  # 更新屏幕内容
