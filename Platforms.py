import pygame
import time
import random

pygame.init()

platform_1 = pygame.image.load("../Roboto/images/Platform1.png")
platform_1 = pygame.transform.scale(platform_1, (400, 250))
'''
class Platform(pygame.sprite.Sprite):
    def __init__(self, platform_1):
        super().__init__()
        self.image = platform_1
        self.rect = self.image.get_rect()



        
'''

objects = []
pygame.time.set_timer(USEREVENT+2,random.randrange(3000,5000))

class saw(object):
    img = [pygame.image.load("../Roboto/images/SAW0.png"),pygame.image.load("../Roboto/images/SAW1.png"),
           pygame.image.load("../Roboto/images/SAW2.png"),pygame.image.load("../Roboto/images/SAW3.png")]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)
        self.count = 0

    def draw(self,gameDisplay):
        self.hitbox = (self.x +5,self.y+5,self.width-10,self.height)
        if self.count >= 8:
            self.count = 0
        gameDisplay.blit(self.img,[self.count//2],(self.x,self.y))
        self.count += 1
        pygame.draw.rect(gameDisplay, (255,0,255),self.hitbox,2)

class spike(saw):
    img = platform_1
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)
        self.count = 0

    def draw(self,gameDisplay):
        self.hitbox = (self.x+10,self.y,28,315)
        gameDisplay.blit(self.img,(self.x,self.y))
        pygame.draw.rect(gameDisplay, (255,100,255),self.hitbox,2)

def redraw_window():
    for objectt in objects:
        objectt.draw(gameDisplay)
    pygame.display.update()


