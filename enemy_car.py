import pygame
from time import sleep
from pygame.sprite import Sprite
from random import choice

class Enemy(Sprite):
    def __init__(self, screen, position):
        super(Enemy, self).__init__()

        #载入图像
        self.image_old = pygame.image.load("敌人赛车.png")
        self.image_car = pygame.transform.scale(self.image_old, (40, 50))
        self.screen = screen

        #获取矩形框
        self.rect = self.image_car.get_rect()
        self.rect.width *= 0.8
        self.rect.height *= 0.8
        self.screen_rect = self.screen.get_rect()

        #对位
        self.rect.centerx = self.screen_rect.centerx + choice([-85, -45, -5, 35, 75])
        self.rect.y = position

        #开关
        self.enemy_active = True

    def enemycar_move(self, speed):
        '''单个汽车运动'''
        if self.enemy_active == True:
            self.rect = self.rect.move(0, speed)
            if self.rect.y > 600:
                self.rect.y = 0
                self.rect.centerx = self.screen_rect.centerx + \
                                    choice([-85, -45, -5, 35, 75])
        sleep(0.004)

