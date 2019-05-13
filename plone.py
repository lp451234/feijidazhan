import pygame
import random
import time
SCREEN_RECT = pygame.Rect(0,0,480,700)
ENEMY_SHOW = pygame.USEREVENT
ENEMY2_SHOW = pygame.USEREVENT+2
ENEMY_FAIR = pygame.USEREVENT+3
class Gameupdate(pygame.sprite.Sprite):
    def __init__(self,rul,speed=1):
        super().__init__()
        self.image = pygame.image.load(rul)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed
class Hero(Gameupdate):
    def __init__(self):
        self.bullet_group = pygame.sprite.Group()
        super().__init__(r".\images\images\me1.png")
        self.rect.y = SCREEN_RECT.height - 300
        self.rect.x = SCREEN_RECT.centerx - self.rect.centerx
    def update(self, *args):
        keys_pre = pygame.key.get_pressed()
        if keys_pre[pygame.K_RIGHT]:
            speed = 2
        elif keys_pre[pygame.K_LEFT]:
            speed = -2
        else:
            speed = 0
        if keys_pre[pygame.K_UP]:
            yspeed = -2
        elif keys_pre[pygame.K_DOWN]:
            yspeed = 2
        else:
            yspeed = 0
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
        self.rect.y += yspeed
        self.rect.x += speed
    def fair(self):
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.x = self.rect.centerx
            bullet.rect.y = self.rect.y - 20 * i
            bullet1 = Bullet()
            bullet1.rect.x = self.rect.x + 25
            bullet1.rect.y = self.rect.y - 15 * i
            bullet2 = Bullet()
            bullet2.rect.x = self.rect.x + 77
            bullet2.rect.y = self.rect.y - 15 * i
            self.bullet_group.add(bullet2)
            self.bullet_group.add(bullet1)
            self.bullet_group.add(bullet)


class Background(Gameupdate):
    def __init__(self):
        super().__init__(r".\images\images\background.png",2)

    def update(self, *args):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Bullet(Gameupdate):
    def __init__(self):
        super().__init__(r".\images\images\bullet1.png")
    def update(self, *args):
        self.rect.y -= 4
        if self.rect.y < 0:
            self.kill()
class EnemyBullet(Gameupdate):
    def __init__(self):
        super().__init__(r".\images\images\bullet2.png")
    def update(self, *args):
        self.rect.y += 4
        if self.rect.y > SCREEN_RECT.height:
            self.kill()
class Enemy(Gameupdate):
    def __init__(self):
        self.showboom_group = pygame.sprite.Group()
        super().__init__(r".\images\images\enemy1.png")
        self.speed = random.randint(1,4)
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
    def update(self, *args):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()
class Enemy2(Gameupdate):
    def __init__(self):
        self.enemy_bullet_group = pygame.sprite.Group()
        super().__init__(r".\images\images\enemy2.png",2)
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.xspeed = random.randint(-2,2)
    def update(self, *args):
        super().update()
        # self.enemyfair()
        self.rect.x += self.xspeed
        if self.rect.y > SCREEN_RECT.height:
            self.speed = -2
            self.xspeed = random.randint(-2, 2)
        elif self.rect.y < -1:
            self.speed = 2
            self.xspeed = random.randint(-2, 2)
        if self.rect.x < 0:
            self.xspeed = -self.xspeed
        elif self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.xspeed = -self.xspeed


    def enemyfair(self):
        enemybullet = EnemyBullet()
        enemybullet.rect.x = self.rect.centerx
        enemybullet.rect.y = self.rect.y + self.rect.height
        self.enemy_bullet_group.add(enemybullet)
