import pygame
class Bollet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\bullet1.png")
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.life = True
        self.speed = 15
        self.mask = pygame.mask.from_surface(self.img)

    def down(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            # self.boom(x,y)
            self.kill()
    def boom(self,x,y):
        self.life = True
        self.rect.x = x
        self.rect.y = y
    def __del__(self):
        # print("删除子弹")
        pass
class Bullet2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\bullet2.png")
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.img)
        self.speed = 15
    def down(self):
        self.rect.y -= self.speed
        if self.rect.y < 0 :
            self.kill()