import os
import pygame
import time
import pickle

from Roboto import Player, Button, SquareIcon, EnemyRobot

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Color Definitions
white = (255, 255, 255)
black = (0, 0, 0)
ground = (26, 20, 17)
red = (255, 0, 0)
lightRed = (244, 66, 66)
grey = (73, 73, 73)
darkYellow = (255, 204, 0)
yellow = (255, 255, 0)
darkGrey = (51, 51, 51)

displayWidth = 800
displayHeight = 600
centerDisplayWidth = displayWidth / 2
centerDisplayHeight = displayHeight / 2
buttonWidth = 150
buttonHeight = 50
groundHeight = displayHeight - 150
FPS = 60

titleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 35)
subTitleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 25)
subSubTitleFont = pygame.font.Font("../Roboto/Krona_One/KronaOne-Regular.ttf", 15)
defaultFont = pygame.font.SysFont("comicsansms", 20)
pauseFont = pygame.font.Font("../Roboto/Passion_One/PassionOne-Bold.ttf", 20)

pygame.mixer.init()
startScreenMusic = "../Roboto/music/Roboto.mp3"
mainMusic = "../Roboto/music/Blackout.mp3"

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Roboto")
clock = pygame.time.Clock()

# icon = pygame.image.load("../Roboto/images/projectiles/EnemyBullet1.png")
# pygame.display.set_icon(icon)

caveBackgroundHome = pygame.transform.scale(pygame.image.load("../Roboto/images/Cave.jpg"),
                                            (displayWidth, displayHeight))
caveBackground = pygame.transform.scale(pygame.image.load("../Roboto/images/Cave.jpg"),
                                        (displayWidth, displayHeight - 100))
leftKey = pygame.transform.scale(pygame.image.load("../Roboto/images/LeftKey.png"), (50, 50))
rightKey = pygame.transform.scale(pygame.image.load("../Roboto/images/RightKey.png"), (50, 50))
upKey = pygame.transform.scale(pygame.image.load("../Roboto/images/UpKey.png"), (50, 50))
spaceBar = pygame.transform.scale(pygame.image.load("../Roboto/images/Space.png"), (180, 60))

roboto = Player.player(20, displayHeight - 155 - (130 / 2), gameDisplay)
enemy = EnemyRobot.enemy(displayWidth - 150, displayHeight - 155 - (130 / 2), gameDisplay)

startScreenRobot = Player.player(displayWidth - 30, 55, gameDisplay)
startScreenRobot.velocity = 3

showHit = False
addScore = False
musicStart = False
justReset = False
score = 0
highScore = 0
hitTimer = 0

try:
    with open('score.dat', 'rb') as file:
        # highScore = 0
        highScore = pickle.load(file)
except:
    highScore = 0
    with open('score.dat', 'wb') as file:
        pickle.dump(highScore, file)

startButton = Button.Button(grey, black, gameDisplay, "START", centerDisplayWidth - (buttonWidth / 2),
                            centerDisplayHeight - 30, buttonWidth, buttonHeight, white, -30, centerDisplayWidth,
                            centerDisplayHeight, defaultFont)

helpButton = Button.Button(grey, black, gameDisplay, "HELP", centerDisplayWidth - (buttonWidth / 2),
                           centerDisplayHeight + 50, buttonWidth, buttonHeight, white, 50, centerDisplayWidth,
                           centerDisplayHeight, defaultFont)

quitButton = Button.Button(grey, black, gameDisplay, "QUIT", centerDisplayWidth - (buttonWidth / 2),
                           centerDisplayHeight + 130, buttonWidth, buttonHeight, white, 130, centerDisplayWidth,
                           centerDisplayHeight, defaultFont)

resumeButton = Button.Button(grey, black, gameDisplay, "RESUME", centerDisplayWidth - (buttonWidth / 2),
                             centerDisplayHeight - 30, buttonWidth, buttonHeight, white, -30, centerDisplayWidth,
                             centerDisplayHeight, defaultFont)

homeButton = Button.Button(grey, black, gameDisplay, "HOME", centerDisplayWidth - (buttonWidth / 2),
                           centerDisplayHeight - 30, buttonWidth, buttonHeight, white, -30, centerDisplayWidth,
                           centerDisplayHeight, defaultFont)


def music(soundtrack):
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def startScreen():
    global justReset
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        gameDisplay.blit(caveBackgroundHome, (0, 0))
        startScreenRobot.movingAnimation("right")

        screen_text = titleFont.render("Roboto", True, white)
        gameDisplay.blit(screen_text, [(displayWidth / 2) - (screen_text.get_rect().width / 2),
                                       (displayHeight / 2) - (screen_text.get_rect().height / 2) - 100])

        startButton.showButton()
        helpButton.showButton()
        quitButton.showButton()

        if not justReset:
            if startButton.isHovered(getCursorPos()):
                if isLeftMouseClicked():
                    gameLoop()
            elif helpButton.isHovered(getCursorPos()):
                if isLeftMouseClicked():
                    helpScreen("start")
            elif quitButton.isHovered(getCursorPos()):
                if isLeftMouseClicked():
                    quitProgram()
        elif justReset and not isLeftMouseClicked():
            justReset = False

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


def helpScreen(lastScreen):
    xMargin = 100
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (50, 50, displayWidth - 100, displayHeight - 100))

        titleText = titleFont.render("Help", True, white)
        helpText1 = defaultFont.render("You play as Roboto, the robot. Roboto has been created to test the ", True,
                                       white)
        helpText2 = defaultFont.render("strength of Dark Roboto. Survive as long as you can, and earn", True,
                                       white)
        helpText3 = defaultFont.render("points by returning shots to Dark Roboto!", True, white)
        helpText4 = subTitleFont.render("Controls", True, white)
        helpText5 = defaultFont.render("Left and Right Arrow Keys to Move", True, white)
        helpText6 = defaultFont.render("Up Arrow Key to Jump", True, white)
        helpText7 = defaultFont.render("Space Bar to Shoot", True, white)

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

        xButton = SquareIcon.SquareIcon(red, lightRed, gameDisplay, "X", displayWidth - 100, 70, 30, black, defaultFont)

        if xButton.left < getCursorPos()[0] < xButton.left + xButton.size and xButton.top < getCursorPos()[1] < \
                xButton.top + xButton.size:
            xButton.hover()
            if isLeftMouseClicked():
                if lastScreen == "start":
                    startScreen()
                elif lastScreen == "pause":
                    pause()

        pygame.display.update()


def gameLoop():
    global musicStart
    global score
    global highScore
    global addScore
    global showHit
    global hitTimer
    while True:
        roboto.hasRestarted = False
        gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (0, displayHeight - 100, displayWidth, 100))

        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        if keys[pygame.K_SPACE]:
            roboto.keepShooting = True
            roboto.isShooting = True

        if not keys[pygame.K_SPACE]:
            roboto.keepShooting = False

        if (roboto.isShooting and roboto.shootPos < roboto.shootRange or not roboto.finishedShot) or \
                roboto.keepShooting:
            if int(round(time.time() * 1000)) - roboto.lastShot >= 200 or not roboto.keepShooting:
                if roboto.shootPos == 0:
                    addScore = True
                roboto.shoot()
        else:
            roboto.isShooting = False

        if not roboto.gotShot:
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
                    roboto.lastJump = 0
                    roboto.jumping = True
            else:
                roboto.jump()

            if int(round(time.time() * 1000)) - enemy.lastShot >= enemy.randomInterval:
                enemy.shoot()
                enemy.isShooting = True
            else:
                enemy.isShooting = False

        if not musicStart:
            music(mainMusic)
            musicStart = True

        pauseButton = SquareIcon.SquareIcon(darkYellow, yellow, gameDisplay, "| |", displayWidth - 50, 20, 30, darkGrey,
                                            pauseFont)

        if pauseButton.left < getCursorPos()[0] < pauseButton.left + pauseButton.size and \
                pauseButton.top < getCursorPos()[1] < pauseButton.top + pauseButton.size:
            pauseButton.hover()
            if isLeftMouseClicked():
                pause()

        if checkCollision(roboto.playerBounds[0], roboto.playerBounds[1], roboto.playerBounds[2],
                          roboto.playerBounds[3], enemy.bulletBounds[0], enemy.bulletBounds[1], enemy.bulletBounds[2],
                          enemy.bulletBounds[3]):
            roboto.gotShot = True
            roboto.resetShooting()

        if roboto.gotShot:
            roboto.ripRoboto(roboto.hasRestarted)

        while roboto.isDead:
            if highScore < score:
                with open('score.dat', 'rb') as fileName:
                    highScore = pickle.load(fileName)
                with open('score.dat', 'wb') as fileName:
                    pickle.dump(score, fileName)
            gameOver()

        if checkCollision(enemy.playerBounds[0], enemy.playerBounds[1], enemy.playerBounds[2], enemy.playerBounds[3],
                          roboto.bulletBounds[0], roboto.bulletBounds[1], roboto.bulletBounds[2],
                          roboto.bulletBounds[3]) and addScore:
            roboto.endShot()
            showHit = True
            hitTimer = int(round(time.time() * 1000))
            score += 1
            addScore = False

        if showHit and int(round(time.time() * 1000)) - hitTimer <= 400:
            screen_text = defaultFont.render("HIT", True, red)
            gameDisplay.blit(screen_text, (enemy.x, enemy.y))

        enemy.idleAnimation()
        gameDisplay.blit(enemy.currentEnemy, (enemy.x, enemy.y))
        gameDisplay.blit(roboto.currentPlayer, (roboto.x, roboto.y))
        showScores(score > highScore)
        pygame.display.update()
        clock.tick(FPS)


def pause():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (50, 50, displayWidth - 100, displayHeight - 100))

        pauseText1 = titleFont.render("Game Paused", True, white)
        gameDisplay.blit(pauseText1, [centerDisplayWidth - (pauseText1.get_rect().width / 2),
                                      centerDisplayHeight - (pauseText1.get_rect().height / 2) - 100])

        resumeButton.showButton()
        helpButton.showButton()
        quitButton.showButton()

        if resumeButton.isHovered(getCursorPos()):
            if isLeftMouseClicked():
                gameLoop()
        elif helpButton.isHovered(getCursorPos()):
            if isLeftMouseClicked():
                helpScreen("pause")
        elif quitButton.isHovered(getCursorPos()):
            if isLeftMouseClicked():
                quitProgram()

        pygame.display.update()


def gameOver():
    global justReset
    justReset = True
    gameDisplay.blit(caveBackground, (0, 0))
    showScores(score > highScore)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quitProgram()
        if event.type == pygame.MOUSEBUTTONDOWN:
            roboto.hasRestarted = True
            roboto.resetRoboto()
            enemy.resetShooting()
            resetGame()
            startScreen()

    gameOverText = titleFont.render("Game Over", True, white)
    gameDisplay.blit(gameOverText, [centerDisplayWidth - (gameOverText.get_rect().width / 2),
                                    centerDisplayHeight - (gameOverText.get_rect().height / 2)])

    clickText = titleFont.render("Click anywhere to restart.", True, white)
    gameDisplay.blit(clickText, [centerDisplayWidth - (clickText.get_rect().width / 2),
                                 centerDisplayHeight - (clickText.get_rect().height / 2) + 50])

    pygame.display.update()


def quitProgram():
    pygame.quit()
    exit()


def getCursorPos():
    return pygame.mouse.get_pos()


def isLeftMouseClicked():
    return pygame.mouse.get_pressed()[0]


def checkCollision(minX1, maxX1, minY1, maxY1, minX2, maxX2, minY2, maxY2):
    return (minX2 <= minX1 <= maxX2 or minX2 <= maxX1 <= maxX2) and (minY1 <= minY2 <= maxY1 or minY1 <= maxY2 <= maxY1)


def resetGame():
    global roboto
    global score
    roboto = Player.player(20, displayHeight - 155 - (130 / 2), gameDisplay)
    score = 0


def showScores(new):
    screen_text = pygame.font.SysFont("comicsansms", 20).render("Score: " + str(score), True, white)
    gameDisplay.blit(screen_text, (20, 20))

    high_score = pygame.font.SysFont("comicsansms", 20).render("High Score: " + str(highScore), True, white)

    if new:
        high_score = pygame.font.SysFont("comicsansms", 20).render("New High Score!", True, red)

    gameDisplay.blit(high_score, (20, 50))


music(startScreenMusic)
startScreen()
