import os
from itertools import count
import pygame
from player_car import Car
from enemy_car import Enemy
import settings

pygame.init()

#设置窗口位置
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' %(50, 70)
#界面搭建
screen = pygame.display.set_mode((200, 600))
pygame.display.set_caption('F1方程式')

#实例
player_car = Car(screen)

locationgroup = (0, -120, -240, -360, -480)
enemycargroup = pygame.sprite.Group()
for lo in locationgroup:
    speed = 5
    enemycargroup.add(Enemy(screen, lo, speed))

scores = count(0)

#主循环
while True:
    '''玩家汽车控制循环部分'''
    player_car.check_events() #首先必须要把退出循环写在最前面
    screen.fill((255, 255, 255)) #每次循环的第一步，必须是清屏一次
    player_car.car_move() #重新确定内存中汽车的数据
    player_car.bliteme() #将更新的数据反应在屏幕上

    '''敌人汽车控制循环部分'''
    for carlist in enemycargroup.sprites():
        carlist.enemycar_move()
        screen.blit(carlist.image_car, carlist.rect)
        settings.game_over(player_car, enemycargroup, carlist)

    '''游戏设置部分'''
    settings.print_text(scores, screen)

    pygame.display.update()