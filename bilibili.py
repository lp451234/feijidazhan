import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(r".\images\images\me2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # self.width,self.height = bg_size[0],bg_size[1]
        # self.rect.left,self.rect.top = (self.width - self.rect.width) // 2 ,self.height - self.rect.height -60
        self.speed = 10