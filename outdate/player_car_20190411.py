import pygame


class Car:
    def __init__(self, screen):
        super(Car, self).__init__()
        self.image_old = pygame.image.load("赛车.png")
        self.image_car = pygame.transform.scale(self.image_old, (40, 50))
        self.screen = screen

        self.rect = self.image_car.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx - 20
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def bliteme(self):
        self.screen.blit(self.image_car, self.rect)

    def car_move(self):
        if self.moving_right and self.rect.centerx < self.screen_rect.right * 0.5:
            self.rect.centerx += 40
        elif self.moving_left and self.rect.centerx > self.screen_rect.right * 0.5:
            self.rect.centerx -= 40

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        if event.key == pygame.K_LEFT:
            self.moving_left = True

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        if event.key == pygame.K_LEFT:
            self.moving_left = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)