import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\enemy1.png")
        self.img_boom  = []
        self.img_boom.append(pygame.image.load(r".\images\images\enemy1_down1.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy1_down2.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy1_down3.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy1_down4.png"))
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0,480 - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1,4)
        self.life = True
        self.mask = pygame.mask.from_surface(self.img)
    def down(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.boom()
    def boom(self):
        self.rect.x = random.randint(0, 480 - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 4)
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\enemy2.png")
        self.img_boom = []
        self.img_boom.append(pygame.image.load(r".\images\images\enemy2_down1.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy2_down2.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy2_down3.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy2_down4.png"))
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0,480 - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1,3)
        self.life = True
        self.life_num = 4
        self.mask = pygame.mask.from_surface(self.img)
    def down(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.boom()
    def boom(self):
        self.rect.x = random.randint(0, 480 - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 3)
class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img1 = pygame.image.load(r".\images\images\enemy3_n1.png")
        self.img2 = pygame.image.load(r".\images\images\enemy3_n2.png")
        self.img_boom = []
        self.img_boom.append(pygame.image.load(r".\images\images\enemy3_down1.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy3_down2.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy3_down3.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy3_down4.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy3_down5.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\enemy3_down6.png"))
        self.rect = self.img1.get_rect()
        self.rect.x = random.randint(0,480 - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1,2)
        self.life = True
        self.life_num = 8
        self.mask = pygame.mask.from_surface(self.img1)
    def down(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.boom()
    def boom(self):
        self.rect.x = random.randint(0, 480 - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 2)