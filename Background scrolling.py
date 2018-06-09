import pygame

pygame.init()


# Color Definitions
white = (255, 255, 255)
black = (0, 0, 0)
ground = (26, 20, 17)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)
lightBlue = (59, 59, 198)
grey = (73, 73, 73)

displayWidth = 800
displayHeight = 600
centerDisplayWidth = (displayWidth / 2)
centerDisplayHeight = (displayHeight / 2)
buttonWidth = 150
buttonHeight = 50
groundHeight = displayHeight - 150
FPS = 60

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Roboto")
clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("../Roboto/images/Cave.jpg"), (displayWidth, displayHeight))

bgX = 0

bgX2 = bg.get_width()

run = True

speed = 30

def redraw_window():
    gameDisplay.blit(bg, (bgX,0))
    gameDisplay.blit(bg, (bgX2,0))
    pygame.display.update()

while run:
    redraw_window()
    clock.tick(speed)
    bgX -= 1.4
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:
        bgX =  bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 =  bg.get_width()
    
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


