import random
import pygame
CREATE_ENEMY_EVENT = pygame.USEREVENT
SCREEN_RECT = pygame.Rect(0,0,480,700)
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Backgroud(Gamesprite):
    def update(self):
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height
class Bullet(Gamesprite):
    def __init__(self):
        super().__init__(r".\images\images\bullet1.png",-2)
    def update(self, *args):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

class Hero(Gamesprite):

    def __init__(self,yspeed=0):
        self.bullets = pygame.sprite.Group()
        self.yspeed = yspeed
        super().__init__(r".\images\images\me1.png",0)
        self.rect.x = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
    def update(self, *args):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.speed = -2
        else:
            self.speed = 0
        if keys_pressed[pygame.K_UP]:
            self.yspeed = -2
        elif keys_pressed[pygame.K_DOWN]:
            self.yspeed = 2
        else:
            self.yspeed = 0
        self.rect.y += self.yspeed
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
        for i in (1,2,3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)
class Enemy(Gamesprite):
    def __init__(self):
        super().__init__(r".\images\images\enemy1.png")
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()
    # def xiaohui(self):
        # self.image = pygame.image.load(r".\images\images\enemy1_down1.png")
        # self.image = pygame.image.load(r".\images\images\enemy1_down2.png")
        # self.image = pygame.image.load(r".\images\images\enemy1_down3.png")
        # bg = pygame.image.load(r".\images\images\enemy1_down1.png")