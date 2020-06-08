import os
import time
from collections import deque
import pygame
from player_car import Car
import settings
import lives

pygame.init()

#设置窗口位置
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' %(50, 70)
#界面搭建
screen = pygame.display.set_mode((200, 600))
pygame.display.set_caption('F1方程式')
#创建对象
palyer_car_lives = 3
player_car = Car(screen)
locationgroup = (0, -120, -240, -360, -480)

enemycargroup = pygame.sprite.Group()
settings.enemy_generate(locationgroup, enemycargroup, screen)

livesgroup = pygame.sprite.Group()
settings.life_generate(palyer_car_lives, screen, livesgroup)

#分数
starttime = time.time()
#最高分数初始化
playerscorelists = deque([settings.read_score()], maxlen=1)

#主循环
while True:
    '''玩家汽车控制循环部分'''
    player_car.check_events() #首先必须要把退出循环写在最前面
    screen.fill((255, 255, 255)) #每次循环的第一步，必须是清屏一次
    player_car.car_move() #重新确定内存中汽车的数据
    player_car.bliteme() #将更新的数据反应在屏幕上
    '''游戏设置部分'''
    highest_score = playerscorelists[0]
    settings.print_highesttext(screen, highest_score)

    text_x = int(settings.text_getscore(starttime))
    settings.print_text(screen, text_x)

    speed = int(text_x ** 0.4)

    for life_left in livesgroup:
        life_left.update()
        screen.blit(life_left.image_life, life_left.rect)

    '''敌人汽车控制循环部分'''
    for carlist in enemycargroup.sprites():
        carlist.enemycar_move(speed)
        screen.blit(carlist.image_car, carlist.rect)
        '''碰撞触发事件'''
        if pygame.sprite.spritecollideany(player_car, enemycargroup):
            #重置enemy_car
            settings.enemy_reset(enemycargroup)
            settings.enemy_generate(locationgroup, enemycargroup, screen)
            #最高分数
            palyer_car_lives -= 1
            livesgroup.empty()
            settings.life_generate(palyer_car_lives, screen, livesgroup)
            if palyer_car_lives == 0:
                starttime = time.time()
                palyer_car_lives = 3
                settings.highesttext_getscore(text_x, highest_score, playerscorelists)
                settings.life_generate(palyer_car_lives, screen, livesgroup)
    pygame.display.update()