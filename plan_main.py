import pygame
from plane_sprites import *
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class PlaneGameMain(object):
    def __init__(self):
        print("游戏初始化。。。")
        self.__create_sprites()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        # self.__create_sprites()
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
    def starGame(self):
        print("开始游戏。。。")
        while True:
            self.clock.tick(60)

            self.__event_handler()

            self.__check_collide()

            self.__update_sprites()

            pygame.display.update()



    def __event_handler(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group,
                                   True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGameMain.__game_over(self)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGameMain.__game_over(self)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            if event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)



    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()

    def __create_sprites(self):
        bg1 = Backgroud(r".\images\images\background.png")
        bg2 = Backgroud(r".\images\images\background.png")
        bg2.rect.y = -bg1.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.enemy_group = pygame.sprite.Group()
if __name__ == '__main__':
    game = PlaneGameMain()
    game.starGame()