import pygame
from pygame.sprite import Sprite

class Lives(Sprite):
    def __init__(self, screen):
        super(Lives, self).__init__()

        self.old_image_life = pygame.image.load('lives.png')
        self.image_life = pygame.transform.scale(self.old_image_life, (20, 20))
        self.screen = screen

        self.rect = self.image_life.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.topright = self.screen_rect.topright

    def blit_life(self):
        self.screen.blit(self.image_life, self.rect)