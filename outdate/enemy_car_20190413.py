import pygame
from time import sleep
from pygame.sprite import Sprite
from random import choice

class Enemy(Sprite):
    def __init__(self, screen, position, speed):
        super(Enemy, self).__init__()

        #载入图像
        self.image_old = pygame.image.load("敌人赛车.png")
        self.image_car = pygame.transform.scale(self.image_old, (40, 50))
        self.screen = screen
        #获取矩形框
        self.rect = self.image_car.get_rect()
        self.screen_rect = self.screen.get_rect()
        #对位
        self.rect.centerx = self.screen_rect.centerx + choice([-80, -40, 0, 40, 80])
        self.rect.y = position
        #速度
        self.speed = speed

    def enemycar_move(self):
        '''单个汽车运动'''
        self.rect = self.rect.move(0, self.speed)
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.centerx = self.screen_rect.centerx + \
                                choice([-80, -40, 0, 40, 80])
        sleep(0.004)

