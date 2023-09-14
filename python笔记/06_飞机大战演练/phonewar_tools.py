import pygame


class PhoneHero(pygame.sprite.Sprite):
    """英雄飞机精灵"""
    def __init__(self, image_path, speed=5):
        super().__init__()  # 调用父类init方法
        # 飞机的图像、位置、速度
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (240, 650)
        self.speed = speed

    def update(self, way):
        if way == "up":
            self.rect.y -= self.speed
        elif way == "down":
            self.rect.y += self.speed
        elif way == "left":
            self.rect.x -= self.speed
        elif way == "right":
            self.rect.x += self.speed

