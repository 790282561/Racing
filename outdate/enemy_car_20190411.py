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
        self.screen_rect = self.screen.get_rect()
        #对位
        self.rect.centerx = self.screen_rect.centerx + choice([-20, 20])
        self.rect.y = position

    def single_enemycar(self):
        '''单个汽车运动'''
        self.rect.move_ip(0, 10)
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.centerx = self.screen_rect.centerx + choice([-20, 20])
        self.screen.blit(self.image_car, self.rect)
        sleep(0.004)

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



    # locationgroup = ([choice([80, 120]), 0],
    #                  [choice([80, 120]), 110],
    #                  [choice([80, 120]), 220],
    #                  [choice([80, 120]), 330],
    #                  [choice([80, 120]), 440],
    #                 )
    # for lo in locationgroup:
    #     enemygroup.append(Enemy("敌人赛车.png", lo))
    # for enemylist in enemygroup:
    #     enemylist.rect.move_ip(0, 10)
    #     sleep(0.02)
    #     screen.blit(enemylist.image_car, enemylist.rect)
    #     pygame.time.delay(0)
