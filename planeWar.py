import pygame
import myplane
import enemy
import bollet
import ui
import bujilei
def add_bullet2(x,y):
    asdw = bollet.Bullet2(x,y)
    bullets2.add(asdw)
def add_bubuji():
    asd = bujilei.Bulletbuji()
    bulletbuji_group.add(asd)
def add_add_boom():
    addadd = bujilei.AddBoom()
    add_boom_group.add(addadd)
def add_boom_ui(group,num,x,y):
    for i in range(num):
        uibomm = ui.BommUi(x-60*(i+1),y)
        group.add(uibomm)
def add_ui(group,num,x,y):
    for i in range(num):
        lifeui = ui.Ui(x+50*i,y)
        group.add(lifeui)
def add_enemy1(group1,group2,num):
    for i in range(num):
        enemy1 = enemy.Enemy()
        group1.add(enemy1)
        group2.add(enemy1)
def add_enemy2(group1,group2,num):
    for i in range(num):
        enemy2 = enemy.Enemy2()
        group1.add(enemy2)
        group2.add(enemy2)
def add_enemy3(group1,group2,num):
    for i in range(num):
        enemy3 = enemy.Enemy3()
        group1.add(enemy3)
        group2.add(enemy3)
def add_bullet(group,num,x,y):
    for i in range(num):
        bullet = bollet.Bollet(x,y+15*i)
        group.add(bullet)
def boomboomboom():
    if hero.boom_num > 0 :
        hero.boom_num -= 1
        for i in enemyalls:
            i.life = False

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load(r".\images\images\background.png")
hero = myplane.Me()
enemy_boom_n = 0
enemy2_boom_n = 0
enemy3_boom_n = 0
hero_boom_n = 0
enemyalls = pygame.sprite.Group()
enemy1s = pygame.sprite.Group()
enemy2s = pygame.sprite.Group()
enemy3s = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
uis = pygame.sprite.Group()
boom_uis = pygame.sprite.Group()
add_boom_group = pygame.sprite.Group()
bulletbuji_group =pygame.sprite.Group()
add_ui(uis,hero.life,0,0)
add_boom_ui(boom_uis,hero.boom_num,470,0)
life_num = True
def quit():
    print("退出游戏...")
    pygame.quit()
    exit()
def xquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

iem = True
runing = 100
gametime = 1800
zidan = 0
while True:
    gametime -= 1
    if gametime == 0:
        gametime = 1800
    if not(gametime%10):
        if not zidan:
            add_bullet(bullets,1,hero.rect.centerx,hero.rect.y)
        else:
            add_bullet2(hero.rect.centerx,hero.rect.y)
            add_bullet2(hero.rect.x, hero.rect.y)
            add_bullet2(hero.rect.x+hero.rect.width, hero.rect.y)
            zidan -= 1
    if not (gametime%60):
        add_enemy1(enemyalls, enemy1s, 1)
    if not (gametime%200):
        add_enemy2(enemyalls, enemy2s, 1)
    if not (gametime%900):
        add_bubuji()
    if not (gametime%600):
        add_enemy3(enemyalls, enemy3s, 1)
    if not (gametime%1800):
        add_add_boom()
    runing -= 1
    if runing == 0:
        runing = 100
    if runing%5 == 0:
        iem = not iem
    screen.blit(bg, (0, 0))
    for enem3 in enemy3s:
        if enem3.life:
            enem3.down()
            if iem:
                screen.blit(enem3.img1,(enem3.rect.x,enem3.rect.y))
            else:
                screen.blit(enem3.img2,(enem3.rect.x,enem3.rect.y))
        else:
            if not (runing%3):
                screen.blit(enem3.img_boom[enemy3_boom_n],(enem3.rect.x,enem3.rect.y))
                enemy3_boom_n = (enemy3_boom_n+1)%6
                if enemy3_boom_n == 0:
                    enem3.kill()
                    life_num = True
    for enem2 in enemy2s:
        if enem2.life:
            enem2.down()
            screen.blit(enem2.img,(enem2.rect.x,enem2.rect.y))
        else:
            if not (runing%3):
                screen.blit(enem2.img_boom[enemy2_boom_n],(enem2.rect.x,enem2.rect.y))
                enemy2_boom_n = (enemy2_boom_n+1)%4
                if enemy2_boom_n == 0:
                    enem2.kill()
                    life_num = True
    for enem1 in enemy1s:
        if enem1.life:
            enem1.down()
            screen.blit(enem1.img,(enem1.rect.x,enem1.rect.y))
        else:
            if not (runing%3):
                screen.blit(enem1.img_boom[enemy_boom_n],(enem1.rect.x,enem1.rect.y))
                enemy_boom_n = (enemy_boom_n+1)%4
                if enemy_boom_n == 0 :
                    enem1.kill()
                    life_num = True
    buji = pygame.sprite.spritecollide(hero,add_boom_group,True,pygame.sprite.collide_mask)
    if buji:
        if hero.boom_num < 5:
            hero.boom_num += 1
            boom_uis.add(ui.BommUi(470-60*hero.boom_num,0))
    buji2 = pygame.sprite.spritecollide(hero,bulletbuji_group,True,pygame.sprite.collide_mask)
    if buji2:
        print()
        zidan += 30
    pengzhuang = pygame.sprite.spritecollide(hero,enemyalls,False,pygame.sprite.collide_mask)
    if pengzhuang:
        hero.lifes = False
        for i in pengzhuang:
            i.life = False
            if life_num:
                hero.life -= 1
                n = hero.life
                for i in uis:
                    if n == 0:
                        i.kill()
                    n -= 1
                life_num = False


    for i in bullets:
        boom_boom = pygame.sprite.spritecollide(i,enemyalls,False,pygame.sprite.collide_mask)
        if boom_boom:
            i.kill()
            for n in boom_boom:
                if n in enemy2s or n in enemy3s:
                    n.life_num -= 1
                    if n.life_num == 0:
                        n.life = False
                else:
                    n.life = False
    for i in bullets2:
        boom_boom = pygame.sprite.spritecollide(i,enemyalls,False,pygame.sprite.collide_mask)
        if boom_boom:
            i.kill()
            for n in boom_boom:
                if n in enemy2s or n in enemy3s:
                    n.life_num -= 1
                    if n.life_num == 0:
                        n.life = False
                else:
                    n.life = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:  # 键被按下
            if event.key == pygame.K_a:
                boomboomboom()
    if hero.lifes:
        if iem:
            # print("显示一号")
            screen.blit(hero.img,(hero.rect.x,hero.rect.y))
        else:
            # print("显示二号")
            screen.blit(hero.img1,(hero.rect.x,hero.rect.y))

    else:
        if not runing%3:
            screen.blit(hero.img_boom[hero_boom_n],(hero.rect.x,hero.rect.y))
            hero_boom_n = (hero_boom_n+1)%4
            if not hero_boom_n:
                print(hero.life)
                if hero.life:
                    hero.rect.x = 200
                    hero.rect.y = 550
                    hero.lifes = True
                else:
                    quit()
    xquit()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        hero.right()
    if keys_pressed[pygame.K_LEFT]:
        hero.left()
    if keys_pressed[pygame.K_UP]:
        hero.up()
    if keys_pressed[pygame.K_DOWN]:
        hero.down()
    for i in bulletbuji_group:
        i.down()
        screen.blit(i.img,(i.rect.x,i.rect.y))
    for i in add_boom_group:
        i.down()
        screen.blit(i.img,(i.rect.x,i.rect.y))
    for bull in bullets:
        bull.down()
        screen.blit(bull.img,(bull.rect.x,bull.rect.y))
    for buk in bullets2:
        buk.down()
        screen.blit(buk.img,(buk.rect.x,buk.rect.y))
    for i in uis:
        screen.blit(i.img,(i.rect.x,i.rect.y))
    n_bomm = hero.boom_num
    for i in boom_uis:
        screen.blit(i.img,(i.rect.x,i.rect.y))
        if n_bomm == 0 :
            i.kill()
        n_bomm -= 1
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
