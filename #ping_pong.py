#ping_pong.py

import pygame
import os
import time
import random
pygame.init()

PATH = os.path.dirname(__file__) + os.sep


COLOR_WHITE = (255, 255, 255)
FPS = 30

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imageS ,w, h,  x, y, speed):
        super().__init__()
        self.image = pygame.image.load(imageS)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
      
        self.speed = speed
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

        #def create(self):
        #self.image = pygame.transform.scale(self.image, (self.w, self.h))
    def show(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))
        

class Hero(GameSprite):
    #def __init__(self, image, w, h, x, y, speed):
        #super(). __init__(image, w, h, x, y, speed)
    def control(self):
        keys = pygame.key.get_pressed()
        #events = pygame.event.ge()
        if keys [pygame.K_w] == True:
            self.y -= 15

        if keys [pygame.K_s] == True:
            self.y += 15

        self.rect.x = self.x
        self.rect.y = self.y


class Hero2(GameSprite):
    #def __init__(self, image, w, h, x, y, speed):
        #super(). __init__(image, w, h, x, y, speed)
    def m_control(self):
        keys = pygame.key.get_pressed()
        #events = pygame.event.ge()
        if keys [pygame.K_UP] == True:
            self.y -= 15

        if keys [pygame.K_DOWN] == True:
            self.y += 15

        self.rect.x = self.x
        self.rect.y = self.y


class Ball(GameSprite):
    def __init__(self, image, w, h, x, y, speed):
        super(). __init__(image, w, h, x, y, speed)
        self.directX = 1
        self.directY = 1

    def move(self):
        
        self.rect.x += self.speed * self.directX
        self.rect.y += self.speed * self.directY

        if self.rect.y > 550 or self.rect.y < 0:
            self.directY *= - 1
        if pygame.sprite.collide_rect(self, platforme1) or  pygame.sprite.collide_rect(self, platforme2):
            self.directX *= -1
        
            


    
wind = pygame.display.set_mode((1000, 600))
beg = GameSprite(PATH+'seryj_odnotonnyj_fon_138531_1280x720.jpg',  1000,600, 0,0,0)
platforme1 = Hero(PATH+'platforme.png', 40, 180,80,200 , 0 )
platforme2 = Hero2(PATH+'platforme.png', 40, 180, 850, 200, 0)
ball = Ball(PATH+'ball.png', 50, 50,450, 250, 7)

font = pygame.font.SysFont('Arial', 40)



game = True



clock = pygame.time.Clock()

while game:

    beg.show()
    platforme1.control()
    platforme1.show()
    platforme2.m_control()
    platforme2.show()
    ball.move()
    ball.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    wind.blit(text1, (10,10))

    clock.tick(FPS)
    pygame.display.update()