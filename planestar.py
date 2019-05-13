import pygame
from plone import *
HERO_FAIR = pygame.USEREVENT + 1
class PlaneGame(object):
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.enemy2_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(SCREEN_RECT.size)
        self.gameipm()
        pygame.time.set_timer(HERO_FAIR,500)
        pygame.time.set_timer(ENEMY_SHOW,1000)
        pygame.time.set_timer(ENEMY2_SHOW,10000)
        pygame.time.set_timer(ENEMY_FAIR,500)
    def star(self):
        print("游戏开始")
        while True:
            self.clock.tick(60)
            self.event()
            self.gameyunxing()
            self.__check_collide()


            pygame.display.update()

    def gameipm(self):
        bg1 = Background()
        bg2 = Background()
        bg2.rect.y = -SCREEN_RECT.height
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        self.enemy2 = Enemy2()
        self.enemy2 = pygame.sprite.Group(self.enemy2)
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    def gameyunxing(self):
        self.bg_group.update()
        self.bg_group.draw(self.window)
        self.hero_group.update()
        self.hero_group.draw(self.window)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.window)
        self.enemy_group.update()
        self.enemy_group.draw(self.window)
        self.enemy2_group.update()
        self.enemy2_group.draw(self.window)
        if self.enemy2_group.__len__() == 0:
            pass
        else:
            self.enemy2.enemy_bullet_group.update()
            self.enemy2.enemy_bullet_group.draw(self.window)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__quit()
            elif event.type == HERO_FAIR:
                self.hero.fair()
            if event.type == ENEMY_SHOW:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            if event.type == ENEMY2_SHOW:
                self.enemy2 = Enemy2()
                self.enemy2_group.add(self.enemy2)
            if event.type == ENEMY_FAIR:
                if self.enemy2_group.__len__() == 0:
                    pass
                else:
                    self.enemy2.enemyfair()

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy2_group,True,True)
        b = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True,True)
        if self.enemy2_group.__len__() == 0:
            pass
        else:
            pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy2.enemy_bullet_group, True, True)
            a = pygame.sprite.groupcollide(self.hero_group, self.enemy2.enemy_bullet_group, True,True)
            if len(a) > 0 :
                self.__quit()
        if len(b) > 0 :
            self.__quit()
    def __quit(self):
        pygame.quit()
        exit()

if __name__ == "__main__":
    wan = PlaneGame()
    wan.star()

