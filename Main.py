import pygame
import time

pygame.init()

# Color Definitions
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)
lightBlue = (59, 59, 198)

displayWidth = 800
displayHeight = 600
centerWidth = (displayWidth / 2)
centerHeight = (displayHeight / 2)
imageWidth = 130
imageHeight = 130
buttonWidth = 150
buttonHeight = 50
groundHeight = displayHeight - 150
FPS = 60

# Jumping Variables
jumping = False
jumpCounter = 12
jumpBound = jumpCounter
lastJump = 0

# Moving Variables
goingLeft = False
goingRight = True
velocity = 5

# Player Location
x = imageWidth
y = displayHeight - 155 - (imageHeight / 2)

# Shooting Variables
isShooting = False

bodyFont = pygame.font.SysFont("comicsansms", 50)
buttonFont = pygame.font.SysFont("comicsansms", 20)
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Roboto")
clock = pygame.time.Clock()

# WIP Icon Variables
# icon = pygame.image.load("../Roboto/images/Idle.png")
# pygame.display.set_icon(icon)


def leftImageMode(player):
    return pygame.transform.flip(player, True, False)


# Image Assignments
idleImages = [pygame.image.load("../Roboto/images/Idle1.png"),
              pygame.image.load("../Roboto/images/Idle2.png"),
              pygame.image.load("../Roboto/images/Idle3.png"),
              pygame.image.load("../Roboto/images/Idle4.png"),
              pygame.image.load("../Roboto/images/Idle5.png"),
              pygame.image.load("../Roboto/images/Idle6.png"),
              pygame.image.load("../Roboto/images/Idle7.png"),
              pygame.image.load("../Roboto/images/Idle8.png"),
              pygame.image.load("../Roboto/images/Idle9.png"),
              pygame.image.load("../Roboto/images/Idle10.png")]

runImages = [pygame.image.load("../Roboto/images/Run1.png"),
              pygame.image.load("../Roboto/images/Run2.png"),
              pygame.image.load("../Roboto/images/Run3.png"),
              pygame.image.load("../Roboto/images/Run4.png"),
              pygame.image.load("../Roboto/images/Run5.png"),
              pygame.image.load("../Roboto/images/Run6.png"),
              pygame.image.load("../Roboto/images/Run7.png"),
              pygame.image.load("../Roboto/images/Run8.png")]

jumpImages = [pygame.image.load("../Roboto/images/Jump1.png"),
              pygame.image.load("../Roboto/images/Jump2.png"),
              pygame.image.load("../Roboto/images/Jump3.png"),
              pygame.image.load("../Roboto/images/Jump4.png"),
              pygame.image.load("../Roboto/images/Jump5.png"),
              pygame.image.load("../Roboto/images/Jump6.png"),
              pygame.image.load("../Roboto/images/Jump7.png"),
              pygame.image.load("../Roboto/images/Jump8.png")]

runShootImages = [pygame.image.load("../Roboto/images/RunShoot1.png"),
                  pygame.image.load("../Roboto/images/RunShoot2.png"),
                  pygame.image.load("../Roboto/images/RunShoot3.png"),
                  pygame.image.load("../Roboto/images/RunShoot4.png"),
                  pygame.image.load("../Roboto/images/RunShoot5.png"),
                  pygame.image.load("../Roboto/images/RunShoot6.png"),
                  pygame.image.load("../Roboto/images/RunShoot7.png"),
                  pygame.image.load("../Roboto/images/RunShoot8.png"),
                  pygame.image.load("../Roboto/images/RunShoot9.png")]

jumpShootImages = [pygame.image.load("../Roboto/images/JumpShoot1.png"),
                  pygame.image.load("../Roboto/images/JumpShoot2.png"),
                  pygame.image.load("../Roboto/images/JumpShoot3.png"),
                  pygame.image.load("../Roboto/images/JumpShoot4.png"),
                  pygame.image.load("../Roboto/images/JumpShoot5.png")]


# Player Images/Assignments
rightPlayer = pygame.transform.scale(idleImages[0], (imageWidth, imageHeight))
leftPlayer = leftImageMode(rightPlayer)
currentPlayer = rightPlayer

# Image Cycle Counters
idleCycleCount = 0
runCycleCount = 0
runShootCycleCount = 0
jumpShootCycleCount = 0


def startScreen():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        gameDisplay.fill(white)

        screen_text = bodyFont.render("Roboto", True, blue)
        gameDisplay.blit(screen_text, [(displayWidth / 2) - (screen_text.get_rect().width / 2),
                                       (displayHeight / 2) - (screen_text.get_rect().height / 2) - 100])

        gameDisplay.fill(blue, (centerWidth - (buttonWidth / 2), centerHeight - 30, buttonWidth, buttonHeight))
        gameDisplay.fill(blue, (centerWidth - (buttonWidth / 2), centerHeight + 50, buttonWidth, buttonHeight))

        cursorPos = pygame.mouse.get_pos()
        leftButtonState = pygame.mouse.get_pressed()[0]

        if (centerWidth - (buttonWidth / 2)) < cursorPos[0] < centerWidth + (buttonWidth / 2) and \
                (centerHeight - (buttonHeight / 2)) < cursorPos[1] < centerHeight + (buttonHeight / 2):
            gameDisplay.fill(lightBlue, (centerWidth - (buttonWidth / 2), centerHeight - 30, buttonWidth, buttonHeight))
            if leftButtonState:
                return

        elif (centerWidth - (buttonWidth / 2)) < cursorPos[0] < centerWidth + (buttonWidth / 2) and \
                (centerHeight + 50 - (buttonHeight / 2)) < cursorPos[1] < centerHeight + 50 + buttonHeight:
            gameDisplay.fill(lightBlue, (centerWidth - (buttonWidth / 2), centerHeight + 50, buttonWidth, buttonHeight))
            if leftButtonState:
                pygame.quit()
                exit()

        drawButtonText("START", white, -30)
        drawButtonText("QUIT", white, 50)

        pygame.display.update()


def drawButtonText(text, colour, yOffset):
    displayText = buttonFont.render(text, True, colour)

    gameDisplay.blit(displayText, [centerWidth - (displayText.get_rect().width / 2),
                                   centerHeight + (buttonHeight / 2) - (displayText.get_rect().height / 2) + yOffset])


def gameLoop():
    global idleCycleCount
    global runCycleCount
    global runShootCycleCount
    global jumpShootCycleCount
    global x
    global y
    global goingLeft
    global goingRight
    global jumping
    global jumpCounter
    global lastJump
    global currentPlayer

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            isShooting = True
        else:
            isShooting = False

        if keys[pygame.K_LEFT] and (x > -30) and not keys[pygame.K_RIGHT]:
            x -= velocity
            runCycleCount += 1
            goingRight = False
            goingLeft = True
            if runCycleCount > ((len(runImages) - 1) * 3) - 1:
                runCycleCount = 0
            if isShooting:
                runShootCycleCount += 1
                if runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                    runShootCycleCount = 0
                currentPlayer = leftImageMode(
                    pygame.transform.scale(runShootImages[runShootCycleCount // 3], (imageWidth, imageHeight)))
            else:
                currentPlayer = leftImageMode(
                    pygame.transform.scale(runImages[runCycleCount // 3], (imageWidth, imageHeight)))

        elif keys[pygame.K_RIGHT] and (x < 695) and not keys[pygame.K_LEFT]:
            x += velocity
            runCycleCount += 1
            goingRight = True
            goingLeft = False
            if runCycleCount > ((len(runImages) - 1) * 3) - 1:
                runCycleCount = 0
            if isShooting:
                runShootCycleCount += 1
                if runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                    runShootCycleCount = 0
                currentPlayer = pygame.transform.scale(runShootImages[runShootCycleCount // 3], (imageWidth, imageHeight))
            else:
                currentPlayer = pygame.transform.scale(runImages[runCycleCount // 3], (imageWidth, imageHeight))
        else:
            idleCycleCount += 1
            if idleCycleCount > ((len(idleImages) - 1) * 3) - 1:
                idleCycleCount = 0
            if goingLeft:
                currentPlayer = leftImageMode(
                    pygame.transform.scale(idleImages[idleCycleCount // 3], (imageWidth, imageHeight)))
            else:
                currentPlayer = pygame.transform.scale(idleImages[idleCycleCount // 3], (imageWidth, imageHeight))

        if not jumping:
            if keys[pygame.K_UP] and int(round(time.time() * 1000)) - lastJump >= 350:
                lastJump = 0
                jumping = True
        else:
            if jumpCounter >= -jumpBound:
                y -= (jumpCounter * 2)
                jumpCounter -= 1
                if goingRight:
                    if isShooting:
                        jumpShootCycleCount += 1
                        if jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                            jumpShootCycleCount = 0
                        currentPlayer = pygame.transform.scale(runShootImages[jumpShootCycleCount // 3],
                                                               (imageWidth, imageHeight))
                    else:
                        currentPlayer = pygame.transform.scale(jumpImages[jumpCounter // 3], (imageWidth, imageHeight))
                else:
                    if isShooting:
                        jumpShootCycleCount += 1
                        if jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                            jumpShootCycleCount = 0
                        currentPlayer = leftImageMode(
                            pygame.transform.scale(runShootImages[jumpShootCycleCount // 3], (imageWidth, imageHeight)))
                    currentPlayer = leftImageMode(
                        pygame.transform.scale(jumpImages[jumpCounter // 3], (imageWidth, imageHeight)))
            else:
                jumpCounter = jumpBound
                jumping = False
                lastJump = int(round(time.time() * 1000))

        gameDisplay.fill(white)
        gameDisplay.fill(black, (0, displayHeight - 100, displayWidth, 100))
        gameDisplay.blit(currentPlayer, (x, y))

        pygame.display.update()
        clock.tick(FPS)


while True:
    startScreen()
    gameLoop()
