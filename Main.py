import pygame
import time

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
imageWidth = 130
imageHeight = 130
buttonWidth = 150
buttonHeight = 50
groundHeight = displayHeight - 150
FPS = 60

titleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 40)
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

caveBackground = pygame.transform.scale(pygame.image.load("../Roboto/images/Cave.jpg"), (displayWidth, displayHeight))

# Player Images/Assignments
rightPlayer = pygame.transform.scale(idleImages[0], (imageWidth, imageHeight))
leftPlayer = leftImageMode(rightPlayer)


def music():
    pygame.mixer.init()
    pygame.mixer.music.load("../Roboto/Roboto.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = imageWidth
        self.height = imageHeight
        self.velocity = 5
        self.jumping = False
        self.isShooting = False
        self.goingLeft = False
        self.goingRight = True
        self.firstMove = True
        self.idleCycleCount = 0
        self.runCycleCount = 0
        self.runShootCycleCount = 0
        self.jumpShootCycleCount = 0
        self.goingLeft = False
        self.goingRight = True
        self.firstMove = True
        self.jumpCounter = 12
        self.jumpBound = self.jumpCounter
        self.lastJump = 0
        self.currentPlayer = rightPlayer


roboto = player(imageWidth, displayHeight - 155 - (imageHeight / 2))


def startScreen():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        gameDisplay.blit(caveBackground, (0, 0))

        screen_text = titleFont.render("Roboto", True, white)
        gameDisplay.blit(screen_text, [(displayWidth / 2) - (screen_text.get_rect().width / 2),
                                       (displayHeight / 2) - (screen_text.get_rect().height / 2) - 100])

        gameDisplay.fill(grey,
                         (centerDisplayWidth - (buttonWidth / 2), centerDisplayHeight - 30, buttonWidth, buttonHeight))
        gameDisplay.fill(grey,
                         (centerDisplayWidth - (buttonWidth / 2), centerDisplayHeight + 50, buttonWidth, buttonHeight))

        cursorPos = pygame.mouse.get_pos()
        leftButtonState = pygame.mouse.get_pressed()[0]

        if (centerDisplayWidth - (buttonWidth / 2)) < cursorPos[0] < centerDisplayWidth + (buttonWidth / 2) and \
                (centerDisplayHeight - (buttonHeight / 2)) < cursorPos[1] < centerDisplayHeight + (buttonHeight / 2):
            gameDisplay.fill(black, (
                centerDisplayWidth - (buttonWidth / 2), centerDisplayHeight - 30, buttonWidth, buttonHeight))
            if leftButtonState:
                return

        elif (centerDisplayWidth - (buttonWidth / 2)) < cursorPos[0] < centerDisplayWidth + (buttonWidth / 2) and \
                (centerDisplayHeight + buttonHeight) < cursorPos[1] < centerDisplayHeight + 50 + buttonHeight:
            gameDisplay.fill(black, (
                centerDisplayWidth - (buttonWidth / 2), centerDisplayHeight + 50, buttonWidth, buttonHeight))
            if leftButtonState:
                pygame.quit()
                exit()
        drawButtonText("START", white, -30)
        drawButtonText("QUIT", white, 50)

        pygame.display.update()


def drawButtonText(text, colour, yOffset):
    displayText = buttonFont.render(text, True, colour)

    gameDisplay.blit(displayText, [centerDisplayWidth - (displayText.get_rect().width / 2),
                                   centerDisplayHeight + (buttonHeight / 2) - (
                                           displayText.get_rect().height / 2) + yOffset])


def gameLoop():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            roboto.isShooting = True
        else:
            roboto.isShooting = False

        if keys[pygame.K_LEFT] and (roboto.x > -30) and not keys[pygame.K_RIGHT]:
            roboto.x -= roboto.velocity
            roboto.runCycleCount += 1
            roboto.goingRight = False
            roboto.goingLeft = True
            roboto.firstMove = False
            if roboto.runCycleCount > ((len(runImages) - 1) * 3) - 1:
                roboto.runCycleCount = 0
            if roboto.isShooting:
                roboto.runShootCycleCount += 1
                if roboto.runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                    roboto.runShootCycleCount = 0
                roboto.currentPlayer = leftImageMode(
                    pygame.transform.scale(runShootImages[roboto.runShootCycleCount // 3], (imageWidth, imageHeight)))
            else:
                roboto.currentPlayer = leftImageMode(
                    pygame.transform.scale(runImages[roboto.runCycleCount // 3], (imageWidth, imageHeight)))

        elif keys[pygame.K_RIGHT] and (roboto.x < 695) and not keys[pygame.K_LEFT]:
            roboto.x += roboto.velocity
            roboto.runCycleCount += 1
            roboto.goingRight = True
            roboto.goingLeft = False
            roboto.firstMove = False
            if roboto.runCycleCount > ((len(runImages) - 1) * 3) - 1:
                roboto.runCycleCount = 0
            if roboto.isShooting:
                roboto.runShootCycleCount += 1
                if roboto.runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                    roboto.runShootCycleCount = 0
                roboto.currentPlayer = pygame.transform.scale(runShootImages[roboto.runShootCycleCount // 3],
                                                              (imageWidth, imageHeight))
            else:
                roboto.currentPlayer = pygame.transform.scale(runImages[roboto.runCycleCount // 3],
                                                              (imageWidth, imageHeight))
        else:
            roboto.idleCycleCount += 1
            if roboto.idleCycleCount > ((len(idleImages) - 1) * 3) - 1:
                roboto.idleCycleCount = 0
            if roboto.goingLeft:
                roboto.currentPlayer = leftImageMode(
                    pygame.transform.scale(idleImages[roboto.idleCycleCount // 3], (imageWidth, imageHeight)))
            else:
                roboto.currentPlayer = pygame.transform.scale(idleImages[roboto.idleCycleCount // 3],
                                                              (imageWidth, imageHeight))

        if not roboto.jumping:
            if keys[pygame.K_UP] and int(round(time.time() * 1000)) - roboto.lastJump >= 350:
                roboto.firstMove = False
                roboto.lastJump = 0
                roboto.jumping = True
        else:
            if roboto.jumpCounter >= -roboto.jumpBound:
                roboto.y -= (roboto.jumpCounter * 2)
                roboto.jumpCounter -= 1
                if roboto.goingRight:
                    if roboto.isShooting:
                        roboto.jumpShootCycleCount += 1
                        if roboto.jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                            roboto.jumpShootCycleCount = 0
                        roboto.currentPlayer = pygame.transform.scale(runShootImages[roboto.jumpShootCycleCount // 3],
                                                                      (imageWidth, imageHeight))
                    else:
                        roboto.currentPlayer = pygame.transform.scale(jumpImages[roboto.jumpCounter // 3],
                                                                      (imageWidth, imageHeight))
                else:
                    if roboto.isShooting:
                        roboto.jumpShootCycleCount += 1
                        if roboto.jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                            roboto.jumpShootCycleCount = 0
                        roboto.currentPlayer = leftImageMode(
                            pygame.transform.scale(runShootImages[roboto.jumpShootCycleCount // 3],
                                                   (imageWidth, imageHeight)))
                    roboto.currentPlayer = leftImageMode(
                        pygame.transform.scale(jumpImages[roboto.jumpCounter // 3], (imageWidth, imageHeight)))
            else:
                roboto.jumpCounter = roboto.jumpBound
                roboto.jumping = False
                roboto.lastJump = int(round(time.time() * 1000))

        gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (0, displayHeight - 100, displayWidth, 100))
        gameDisplay.blit(roboto.currentPlayer, (roboto.x, roboto.y))

        if roboto.firstMove:
            music()

        pygame.display.update()
        clock.tick(FPS)


while True:
    startScreen()
    gameLoop()
