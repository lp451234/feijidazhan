import pygame
class Ui(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\life.png")
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

class BommUi(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\bomb.png")
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y