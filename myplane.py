import pygame

class Me(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(r".\images\images\me2.png").convert_alpha()
        self.img1 = pygame.image.load(r".\images\images\me1.png").convert_alpha()
        self.img_boom = []
        self.img_boom.append(pygame.image.load(r".\images\images\me_destroy_1.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\me_destroy_2.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\me_destroy_3.png"))
        self.img_boom.append(pygame.image.load(r".\images\images\me_destroy_4.png"))
        self.rect = self.img.get_rect()
        self.rect.x = 200
        self.rect.y = 550
        self.speed = 10
        self.lifes = True
        self.life = 3
        self.boom_num = 3
        self.mask = pygame.mask.from_surface(self.img)

    def up(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = 0
    def down(self):
        self.rect.y += self.speed
        if self.rect.y > 650 - self.rect.height:
            self.rect.y = 650 - self.rect.height
    def left(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
    def right(self):
        self.rect.x += self.speed
        if self.rect.x > 480 - self.rect.width:
            self.rect.x = 480 - self.rect.width