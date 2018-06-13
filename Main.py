import pygame
import time
from Roboto import Player, Button, SquareIcon

pygame.init()

# Color Definitions
white = (255, 255, 255)
black = (0, 0, 0)
ground = (26, 20, 17)
red = (255, 0, 0)
lightRed = (244, 66, 66)
green = (0, 155, 0)
grey = (73, 73, 73)
darkYellow = (255, 204, 0)
yellow = (255, 255, 0)
darkGrey = (51, 51, 51)

displayWidth = 800
displayHeight = 600
centerDisplayWidth = (displayWidth / 2)
centerDisplayHeight = (displayHeight / 2)
buttonWidth = 150
buttonHeight = 50
groundHeight = displayHeight - 150
FPS = 60

titleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 35)
subTitleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 25)
subSubTitleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 15)
bodyFont = pygame.font.SysFont("comicsansms", 20)
buttonFont = pygame.font.SysFont("comicsansms", 20)
pauseFont = pygame.font.Font("../Roboto/Passion_One/PassionOne-Bold.ttf", 20)

pygame.mixer.init()
startScreenMusic = "../Roboto/music/Roboto.mp3"
mainMusic = "../Roboto/music/Blackout.mp3"

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Roboto")
clock = pygame.time.Clock()

# WIP Icon Variables
# icon = pygame.image.load("../Roboto/images/Idle.png")
# pygame.display.set_icon(icon)

caveBackground = pygame.transform.scale(pygame.image.load("../Roboto/images/Cave.jpg"), (displayWidth, displayHeight))
leftKey = pygame.transform.scale(pygame.image.load("../Roboto/images/LeftKey.png"), (50, 50))
rightKey = pygame.transform.scale(pygame.image.load("../Roboto/images/RightKey.png"), (50, 50))
upKey = pygame.transform.scale(pygame.image.load("../Roboto/images/UpKey.png"), (50, 50))
spaceBar = pygame.transform.scale(pygame.image.load("../Roboto/images/Space.png"), (180, 60))

roboto = Player.player(Player.imageWidth, displayHeight - 155 - (Player.imageHeight / 2), gameDisplay)

startScreenRobot = Player.player(displayWidth - 30, 55, gameDisplay)
startScreenRobot.velocity = 3

resume = False


def music(soundtrack):
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def startScreen():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        gameDisplay.blit(caveBackground, (0, 0))
        startScreenRobot.movingAnimation("right")

        screen_text = titleFont.render("Roboto", True, white)
        gameDisplay.blit(screen_text, [(displayWidth / 2) - (screen_text.get_rect().width / 2),
                                       (displayHeight / 2) - (screen_text.get_rect().height / 2) - 100])

        startButton = Button.Button(grey, black, gameDisplay, "START", centerDisplayWidth - (buttonWidth / 2),
                                    centerDisplayHeight - 30, buttonWidth, buttonHeight, white, -30, centerDisplayWidth,
                                    centerDisplayHeight)

        helpButton = Button.Button(grey, black, gameDisplay, "HELP", centerDisplayWidth - (buttonWidth / 2),
                                   centerDisplayHeight + 50, buttonWidth, buttonHeight, white, 50, centerDisplayWidth,
                                   centerDisplayHeight)

        quitButton = Button.Button(grey, black, gameDisplay, "QUIT", centerDisplayWidth - (buttonWidth / 2),
                                   centerDisplayHeight + 130, buttonWidth, buttonHeight, white, 130, centerDisplayWidth,
                                   centerDisplayHeight)

        if (centerDisplayWidth - (buttonWidth / 2)) < getCursorPos()[0] < centerDisplayWidth + (buttonWidth / 2) and \
                (centerDisplayHeight - (buttonHeight / 2)) < getCursorPos()[1] < \
                centerDisplayHeight + (buttonHeight / 2):
            startButton.hover()
            if isLeftMouseClicked():
                gameLoop()

        elif (centerDisplayWidth - (buttonWidth / 2)) < getCursorPos()[0] < centerDisplayWidth + (buttonWidth / 2) and \
                (centerDisplayHeight + buttonHeight) < getCursorPos()[1] < centerDisplayHeight + 50 + buttonHeight:
            helpButton.hover()
            if isLeftMouseClicked():
                helpScreen()
        elif (centerDisplayWidth - (buttonWidth / 2)) < getCursorPos()[0] < centerDisplayWidth + (buttonWidth / 2) and \
                (centerDisplayHeight + 130) < getCursorPos()[1] < centerDisplayHeight + 130 + buttonHeight:
            quitButton.hover()
            if isLeftMouseClicked():
                quitProgram()

        if startScreenRobot.x > displayWidth + 1400:
            startScreenRobot.x = -(startScreenRobot.width / 2)
        elif 200 <= startScreenRobot.x <= 400:
            startScreenRobot.isShooting = True
        else:
            startScreenRobot.isShooting = False

        gameDisplay.blit(startScreenRobot.currentPlayer, (startScreenRobot.x, startScreenRobot.y))

        creators = subSubTitleFont.render("Created by Hannah Guo & Manav Shardha", True, white)
        gameDisplay.blit(creators, [(displayWidth / 2) - (creators.get_rect().width / 2), displayHeight - 50])

        pygame.display.update()


def helpScreen():
    global resume
    xMargin = 100
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (50, 50, displayWidth - 100, displayHeight - 100))

        titleText = titleFont.render("Help", True, white)
        helpText1 = bodyFont.render("You play as Roboto, the robot. Roboto has been created to test the ", True, white)
        helpText2 = bodyFont.render("mettle of the Cavern. Survive as long as you can, and earn the most", True, white)
        helpText3 = bodyFont.render("points by shooting monsters and dodging obstacles!", True, white)
        helpText4 = subTitleFont.render("Controls", True, white)
        helpText5 = bodyFont.render("Left and Right Arrow Keys to Move", True, white)
        helpText6 = bodyFont.render("Up Arrow Key to Jump", True, white)
        helpText7 = bodyFont.render("Space Bar to Shoot", True, white)

        gameDisplay.blit(titleText, [xMargin, 100])
        gameDisplay.blit(helpText1, [xMargin, 150])
        gameDisplay.blit(helpText2, [xMargin, 180])
        gameDisplay.blit(helpText3, [xMargin, 210])
        gameDisplay.blit(helpText4, [xMargin, 260])
        gameDisplay.blit(helpText5, [300, displayHeight - 280])
        gameDisplay.blit(helpText6, [300, displayHeight - 215])
        gameDisplay.blit(helpText7, [300, displayHeight - 140])

        gameDisplay.blit(leftKey, [120, displayHeight - 290])
        gameDisplay.blit(rightKey, [180, displayHeight - 290])
        gameDisplay.blit(upKey, [150, displayHeight - 220])
        gameDisplay.blit(spaceBar, [90, displayHeight - 150])

        xButton = SquareIcon.SquareIcon(red, lightRed, gameDisplay, "X", displayWidth - 100, 70, 30, black, buttonFont)

        if xButton.left < getCursorPos()[0] < xButton.left + xButton.size and xButton.top < getCursorPos()[1] < \
                xButton.top + xButton.size:
            xButton.hover()
            if isLeftMouseClicked():
                startScreen()

        pygame.display.update()


def gameLoop():
    global resume
    while True:
        gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (0, displayHeight - 100, displayWidth, 100))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            roboto.keepShooting = True
            roboto.isShooting = True

        if not keys[pygame.K_SPACE]:
            roboto.keepShooting = False

        if (roboto.isShooting and roboto.shootPos < roboto.shootRange or not roboto.finishedShot) or \
                roboto.keepShooting:
            if int(round(time.time() * 1000)) - roboto.lastShot >= 200 or not roboto.keepShooting:
                roboto.shoot()
        else:
            roboto.isShooting = False

        if (roboto.direction == "right" and keys[pygame.K_LEFT]) or \
                (roboto.direction == "left" and keys[pygame.K_RIGHT]):
            roboto.keepShooting = False

        if keys[pygame.K_LEFT] and (roboto.x > -30) and not keys[pygame.K_RIGHT]:
            roboto.movingAnimation("left")
        elif keys[pygame.K_RIGHT] and (roboto.x < 695) and not keys[pygame.K_LEFT]:
            roboto.movingAnimation("right")
        else:
            roboto.idleAnimation()

        if not roboto.jumping:
            if keys[pygame.K_UP] and int(round(time.time() * 1000)) - roboto.lastJump >= 350:
                roboto.firstMove = False
                roboto.lastJump = 0
                roboto.jumping = True
        else:
            roboto.jump()

        if roboto.firstMove:
            music(mainMusic)

        # if keys[pygame.K_p]:
        #     roboto.ripRoboto()
        # else:
        #     roboto.deadCycleCount = 0

        gameDisplay.blit(roboto.currentPlayer, (roboto.x, roboto.y))

        pauseButton = SquareIcon.SquareIcon(darkYellow, yellow, gameDisplay, "| |", displayWidth - 50, 20, 30, darkGrey,
                                            pauseFont)

        if pauseButton.left < getCursorPos()[0] < pauseButton.left + pauseButton.size and \
                pauseButton.top < getCursorPos()[1] < pauseButton.top + pauseButton.size:
            pauseButton.hover()
            if isLeftMouseClicked():
                if not resume:
                    pause()
                else:
                    resume = True
            else:
                resume = False

        pygame.display.update()
        clock.tick(FPS)


def pause():
    global resume
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        pauseText1 = titleFont.render("Game Paused", True, white)
        gameDisplay.blit(pauseText1, [centerDisplayWidth - (pauseText1.get_rect().width / 2),
                                      centerDisplayHeight - (pauseText1.get_rect().height / 2)])

        pauseText2 = subTitleFont.render("Click anywhere to resume", True, white)
        gameDisplay.blit(pauseText2, [centerDisplayWidth - (pauseText2.get_rect().width / 2),
                                      centerDisplayHeight - (pauseText2.get_rect().height / 2) + 40])
        resume = True
        pygame.display.update()


def quitProgram():
    pygame.quit()
    exit()


def getCursorPos():
    return pygame.mouse.get_pos()


def isLeftMouseClicked():
    return pygame.mouse.get_pressed()[0]


music(startScreenMusic)
startScreen()
