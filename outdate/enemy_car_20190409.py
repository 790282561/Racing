import pygame
from time import sleep
from pygame.sprite import Sprite
from random import choice

class Enemy(Sprite):
    def __init__(self, filename, initial_position):
        super(Enemy, self).__init__()

        #载入图像
        self.image_old = pygame.image.load(filename)
        self.image_car = pygame.transform.scale(self.image_old, (40, 50))

        #获取矩形框
        self.rect = self.image_car.get_rect()

        #矩形框确定位置
        self.rect.topleft = initial_position



    # def bliteme(self):
    #     self.rect.move_ip(0, 10)
    #     sleep(0.02)
    #     if self.rect.y > 600:
    #         self.rect.centerx = self.screen_rect.centerx + choice([-20, 20])
    #         self.rect.y = 0
    #
    #     for self.lo in self.locationgroup:
    #         self.rect_enemy = pygame.Rect(self.lo, (40, 50))
    #
    #         self.rect_enemy.move_ip(0, 10)
    #         sleep(0.02)
    #
    #         if self.rect_enemy.y > 660:
    #             self.rect_enemy.y = 0

def enemy_car_group():
    screen = pygame.display.set_mode((200, 550))
    enemygroup = []
    locationgroup = ([80, 0],
                     [80, 110],
                     [80, 220],
                     [80, 330],
                     [80, 440],
                     )
    # locationgroup = ([choice([80, 120]), 0],
    #                  [choice([80, 120]), 110],
    #                  [choice([80, 120]), 220],
    #                  [choice([80, 120]), 330],
    #                  [choice([80, 120]), 440],
    #                 )
    for lo in locationgroup:
        enemygroup.append(Enemy("敌人赛车.png", lo))
    for enemylist in enemygroup:
        enemylist.rect.move_ip(0, 10)
        sleep(0.02)
        screen.blit(enemylist.image_car, enemylist.rect)
        pygame.time.delay(0)