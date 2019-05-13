import pygame
import random
class AddBoom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\bomb_supply.png")
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.rect.x = random.randint(0,480-self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 4
    def down(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.kill()
class Bulletbuji(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(r".\images\images\bullet_supply.png")
        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img)
        self.rect.x = random.randint(0,480-self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 4
    def down(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.kill()