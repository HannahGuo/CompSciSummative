import pygame
import time
import Player, Button
#import platforms

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

titleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 40)
bodyFont = pygame.font.SysFont("comicsansms", 50)
buttonFont = pygame.font.SysFont("comicsansms", 20)

pygame.mixer.init()
startScreenMusic = "../Roboto/Roboto.mp3"
mainMusic = "../Roboto/Blackout.mp3"


gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Roboto")
clock = pygame.time.Clock()

# WIP Icon Variables
# icon = pygame.image.load("../Roboto/images/Idle.png")
# pygame.display.set_icon(icon)

caveBackground = pygame.transform.scale(pygame.image.load("../Roboto/images/Cave.jpg"), (displayWidth, displayHeight))
roboto = Player.player(Player.imageWidth, displayHeight - 155 - (Player.imageHeight / 2),gameDisplay)

platform_1 = pygame.image.load("../Roboto/images/Platform1.png")
platform_1 = pygame.transform.scale(platform_1, (400, 150))


#add backgroundrunning
caveBackground1 = -30

caveBackground2 = caveBackground.get_width() - 30

startScreenRobot = Player.player(displayWidth - 30, 55,gameDisplay)
startScreenRobot.velocity = 3


def redraw_window():
    gameDisplay.blit(caveBackground, (caveBackground1,0))
    gameDisplay.blit(caveBackground, (caveBackground2,0))


def music(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    
def running_window():
    gameDisplay = pygame.display.set_mode((displayWidth+695, displayHeight))
    

def startScreen():
    music(startScreenMusic)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        gameDisplay.blit(caveBackground, (0, 0))
        startScreenRobot.movingAnimation("right")

        screen_text = titleFont.render("Roboto", True, white)
        gameDisplay.blit(screen_text, [(displayWidth / 2) - (screen_text.get_rect().width / 2),
                                       (displayHeight / 2) - (screen_text.get_rect().height / 2) - 100])

        startButton = Button.Button(grey, black, gameDisplay, "START", centerDisplayWidth - (buttonWidth / 2),
                                    centerDisplayHeight - 30, buttonWidth, buttonHeight, white, -30, centerDisplayWidth,
                                    centerDisplayHeight)

        quitButton = Button.Button(grey, black, gameDisplay, "QUIT", centerDisplayWidth - (buttonWidth / 2),
                                   centerDisplayHeight + 50, buttonWidth, buttonHeight, white, 50, centerDisplayWidth,
                                   centerDisplayHeight)

        cursorPos = pygame.mouse.get_pos()
        leftButtonState = pygame.mouse.get_pressed()[0]

        if (centerDisplayWidth - (buttonWidth / 2)) < cursorPos[0] < centerDisplayWidth + (buttonWidth / 2) and \
                (centerDisplayHeight - (buttonHeight / 2)) < cursorPos[1] < centerDisplayHeight + (buttonHeight / 2):
            startButton.hover()
            if leftButtonState:
                return

        elif (centerDisplayWidth - (buttonWidth / 2)) < cursorPos[0] < centerDisplayWidth + (buttonWidth / 2) and \
                (centerDisplayHeight + buttonHeight) < cursorPos[1] < centerDisplayHeight + 50 + buttonHeight:
            quitButton.hover()
            if leftButtonState:
                pygame.quit()
                exit()

        if startScreenRobot.x > displayWidth + 1400:
            startScreenRobot.x = -(startScreenRobot.width / 2)
        elif 200 <= startScreenRobot.x <= 400:
            startScreenRobot.isShooting = True
        else:
            startScreenRobot.isShooting = False

        gameDisplay.blit(startScreenRobot.currentPlayer, (startScreenRobot.x, startScreenRobot.y))

        pygame.display.update()


def gameLoop():
    global caveBackground1
    global caveBackground2
    while True:
        redraw_window()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        if caveBackground1 < caveBackground.get_width() * -1:
            caveBackground1 = caveBackground.get_width() - 30
        if caveBackground2 < caveBackground.get_width() * -1:
            caveBackground2 = caveBackground.get_width() - 30

        if keys[pygame.K_SPACE]:
            roboto.isShooting = True
        else:
            roboto.isShooting = False

        if keys[pygame.K_LEFT] and (roboto.x > -30) and not keys[pygame.K_RIGHT]:
            caveBackground1 += 1.4
            caveBackground2 += 1.4
            roboto.movingAnimation("left")
        elif keys[pygame.K_RIGHT] and (roboto.x < 695) and not keys[pygame.K_LEFT]:
        #elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            caveBackground1 -= 1.4
            caveBackground2 -= 1.4
            roboto.movingAnimation("right")
            #if roboto.x < 695:
                #running_window()
        else:
            roboto.idleAnimation()

        if not roboto.jumping:
            if keys[pygame.K_UP] and int(round(time.time() * 1000)) - roboto.lastJump >= 350:
                roboto.firstMove = False
                roboto.lastJump = 0
                roboto.jumping = True
        else:
            roboto.jump()

        #gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (0, displayHeight - 100, displayWidth, 100))
        gameDisplay.blit(roboto.currentPlayer, (roboto.x, roboto.y))
        gameDisplay.blit(platform_1, (450,displayHeight-150))

        if roboto.firstMove:
            music(mainMusic)

        pygame.display.update()
        clock.tick(FPS)

def level_one():
    pass    


while True:
    startScreen()
    gameLoop()