import pygame

pygame.init()

platform_1 = pygame.image.load("../Roboto/images/Platform1.png")
platform_1 = pygame.transform.scale(platform_1, (400, 250))

class Platform(pygame.sprite.Sprite):
    def __init__(self, platform_1):
        super().__init__()
        self.image = platform_1
        self.rect = self.image.get_rect()

        
