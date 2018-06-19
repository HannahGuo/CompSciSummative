# Hannah Guo and Manav Shardha
# June 18th 2018
# ICS3UR
# This is the main file for our game. It contains each game state (start screen, pause, game loop, game over) as a
# function. It also contains the display's features (colours, background, and buttons).

import os
import pygame
import time
import pickle

from Roboto import Player, Button, SquareIcon, EnemyRobot

pygame.init()  # this initializes pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'  # this centers the window to the center of the user's screen

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

displayWidth = 800   # this defines the display width to be 800 pixels. This is later used when creating the window.
displayHeight = 600  # this defines the display height to 600 pixels. This is later used when creating the window.
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

# this try/except block handles accessing a high score
try:  # this attempts to open a file
    with open('score.dat', 'rb') as file:  # opens score.dat to read
        highScore = pickle.load(file)  # set highScore to the loaded file
except:  # if there is no score.dat file, then this creates one. Without this except, the program would crash.
    with open('score.dat', 'wb') as file:  # opens score.dat to write
        pickle.dump(highScore, file)  # put the highScore (which is 0 if this runs) in the pickle file

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
            if startButton.isHovered(getCursorPos()) and isLeftMouseClicked():
                gameLoop()
            elif helpButton.isHovered(getCursorPos()) and isLeftMouseClicked():
                helpScreen("start")
            elif quitButton.isHovered(getCursorPos()) and isLeftMouseClicked():
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
    """
    This function displays the help screen for the user. It shows the goal of the game, and the controls.
    :param lastScreen:
    :return:
    """
    while True:
        xMargin = 100  # sets the value of the xMargin for the text

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        gameDisplay.blit(caveBackgroundHome, (0, 0))  # displays the cave background at (0, 0), meaning it will take up
                                                      # the whole screen
        gameDisplay.fill(ground, (50, 50, displayWidth - 100, displayHeight - 100))  # displays a backdrop the colour
                                                                                     # of the ground for the text
                                                                                     # so that it's easier to see
        titleText = titleFont.render("Help", True, white)  # renders the title of the screen "Help" in a white font.

        # Each helpText block is a rendered line of text. Pygame doesn't have paragraph support, so each line was
        # adjusted to have the right number of words to fit on the screen. The font is always white since that is the
        # clearest on the backdrop. The font most frequently used is the defaultFont, although the controls subtitle
        # uses the subtitle font.
        helpText1 = defaultFont.render("You play as Roboto, the robot. Roboto has been created to test the ", True,
                                       white)
        helpText2 = defaultFont.render("strength of Dark Roboto. Survive as long as you can, and earn", True,
                                       white)
        helpText3 = defaultFont.render("points by returning shots to Dark Roboto!", True, white)
        helpText4 = subTitleFont.render("Controls", True, white)
        helpText5 = defaultFont.render("Left and Right Arrow Keys to Move", True, white)
        helpText6 = defaultFont.render("Up Arrow Key to Jump", True, white)
        helpText7 = defaultFont.render("Space Bar to Shoot", True, white)

        # display all the help texts to the screen at the specified x and y coordinates. This is where xMargin is used
        # to keep the x margin consistent. The y value was then adjusted by a constant in order for it to display
        # in neat lines below each other.
        gameDisplay.blit(titleText, [xMargin, 100])
        gameDisplay.blit(helpText1, [xMargin, 150])
        gameDisplay.blit(helpText2, [xMargin, 180])
        gameDisplay.blit(helpText3, [xMargin, 210])
        gameDisplay.blit(helpText4, [xMargin, 260])
        gameDisplay.blit(helpText5, [300, displayHeight - 280])
        gameDisplay.blit(helpText6, [300, displayHeight - 215])
        gameDisplay.blit(helpText7, [300, displayHeight - 140])

        # These lines display keyboard visuals for the left, right, up keys and the space bar. Each image's x and y
        # values were tuned to line up with their corresponding text.
        gameDisplay.blit(leftKey, [120, displayHeight - 290])
        gameDisplay.blit(rightKey, [180, displayHeight - 290])
        gameDisplay.blit(upKey, [150, displayHeight - 220])
        gameDisplay.blit(spaceBar, [90, displayHeight - 150])

        # This creates a red X icon in the top right corner. This is for the user to return to their previous screen.
        xButton = SquareIcon.SquareIcon(red, lightRed, gameDisplay, "X", displayWidth - 100, 70, 30, black, defaultFont)
        xButton.showIcon()  # puts the x button on the screen

        # This makes the X button more responsive by changing the colour when it is hovered (done in the isHovered
        # function). The if statement checks if the button was hovered and the mouse was clicked.
        if xButton.isHovered(getCursorPos()) and isLeftMouseClicked():
            if lastScreen == "start":  # if the last screen was the start screen, go back to the start screen.
                startScreen()          # call the start screen function
            elif lastScreen == "pause":   # if the last screen was the pause screen, go back to the pause screen.
                pause()                   # call the pause function to show its screen

        pygame.display.update()  # update the display to see the changes


def gameLoop():
    global musicStart
    global score
    global highScore
    global addScore
    global showHit
    global hitTimer
    while True:  # this loop continues running until another function is called, or if the program quits. It contains
                 # all of the game loop code.
        events = pygame.event.get()  # this gets a list of pygame's events and assigns it to the events variable.
        for event in events:         # this for loop loop through the events list defined above. This essentially gets
                                     # all of pygame's events, like mouse button presses. However, for this program the
                                     # only event we handle is the QUIT event (when the application's X button is
                                     # clicked).
            if event.type == pygame.QUIT:  # if the user wants to quit
                quitProgram()              # quit the program; this function is defined later on in the main file.

        roboto.hasRestarted = False
        gameDisplay.blit(caveBackground, (0, 0))
        gameDisplay.fill(ground, (0, displayHeight - 100, displayWidth, 100))

        keys = pygame.key.get_pressed()  # receives the values of each key button in a dictionary. If a key is pressed,
                                         # its boolean value will be True and if it's not, it will be False. This is
                                         # used to access the user's keyboard input.

        if keys[pygame.K_SPACE]:  # this handles if the user pressed the space bar, which triggers the shoot function.
            roboto.keepShooting = True  # since the space bar is still pressed, the robot should keep shooting
            roboto.isShooting = True    # since the user pressed the space bar, the robot is shooting. This variable
                                        # controls the shooting, which is shown later on in the code.
        else:                           # otherwise, space isn't being pressed
            roboto.keepShooting = False  # this means that the robot is not still shooting, so set keepShooting to false

        # The following if condition handles shooting. Note that roboto.keepShooting and roboto.isShooting are
        # conditions in the statement, and at least one of them must be true in order for robot to shoot (although they
        # are not the only conditions that must be met). Therefore, the user's input of a space bar press that set these
        # variables to true controls the shoot function.
        if (roboto.isShooting and roboto.shootPos < roboto.shootRange or not roboto.finishedShot) or \
                roboto.keepShooting:
            if int(round(time.time() * 1000)) - roboto.lastShot >= 200 or not roboto.keepShooting:
                if roboto.shootPos == 0:
                    addScore = True
                roboto.shoot()  # this function is the shot itself.
        else:
            roboto.isShooting = False

        if not roboto.gotShot:  # this only runs if the robot hasn't been shot (i.e. hasn't died yet). This is to make
                                # sure that the player's x and y positions don't change during a dying animation.
            # This if statement will stop the robot's continuous shooting if the user switches directions. This means
            # that the current direction is not the same as they keyboard input. (i.e. robot going right then left
            # arrow key is preesed or robot going left then right arrow key is pressed).
            if (roboto.direction == "right" and keys[pygame.K_LEFT]) or \
                    (roboto.direction == "left" and keys[pygame.K_RIGHT]):
                roboto.keepShooting = False  # set keepShooting to false

            # This if statement checks if the user wants the player to move left. The conditions for this are that
            # the left arrow key is pressed, the robot's x value is within the minimum boundary (-30) and the right
            # arrow key is not pressed.
            if keys[pygame.K_LEFT] and (roboto.x > -30) and not keys[pygame.K_RIGHT]:
                roboto.movingAnimation("left")  # make the robot move left.
            # This elif statement checks if the user wants the player to move left. The conditions for this are that
            # the right arrow key is pressed, the robot's x value is within the maximum boundary (695) and the left
            # arrow key is not pressed.
            elif keys[pygame.K_RIGHT] and (roboto.x < 695) and not keys[pygame.K_LEFT]:
                roboto.movingAnimation("right")  # make the robot move right
            else:  # if neither of these conditions are met, then the robot will not move and run its idle animation
                roboto.idleAnimation()  # run the idle animation

            if not roboto.jumping:  # condition checking if the robot is currently jumping. We don't want the robot to
                                    # jump again before its previous jump was finished.
                # The following if statement checks if the up arrow key was pressed, and if the robot's last jump was
                # 350 milliseconds ago. The 350ms delay is to make sure the robot doesn't quickly jump consecutively.
                if keys[pygame.K_UP] and int(round(time.time() * 1000)) - roboto.lastJump >= 350:
                    roboto.lastJump = 0    # reset the robot's last jump timer to 0
                    roboto.jumping = True  # sets jumping to true, meaning the robot can now jump
            else:  # otherwise, the robot can jump
                roboto.jump()  # make the robot jump

            # This if statement is for the enemy's shot. It checks if the random interval between the enemy's shots has
            # passed or not. It's in this if condition because we don't want the enemy to keep shooting after the player
            #  has died.
            if int(round(time.time() * 1000)) - enemy.lastShot >= enemy.randomInterval:
                enemy.shoot()  # make the enemy shoot
                enemy.isShooting = True  # set the enemy's shooting status to True
            else:  # otherwise, the interval hasn't been met
                enemy.isShooting = False  # set the enemy's shooting status to False

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
                    pickle.dump(highScore, fileName)
            gameOver()

        if checkCollision(enemy.playerBounds[0], enemy.playerBounds[1], enemy.playerBounds[2], enemy.playerBounds[3],
                          roboto.bulletBounds[0], roboto.bulletBounds[1], roboto.bulletBounds[2],
                          roboto.bulletBounds[3]) and addScore:
            roboto.playShotSound()
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

        if not musicStart:
            music(mainMusic)
            musicStart = True

        pauseButton = SquareIcon.SquareIcon(darkYellow, yellow, gameDisplay, "| |", displayWidth - 50, 20, 30, darkGrey,
                                            pauseFont)
        pauseButton.showIcon()

        if pauseButton.isHovered(getCursorPos()) and isLeftMouseClicked():
            pause()

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

        if resumeButton.isHovered(getCursorPos()) and isLeftMouseClicked():
            gameLoop()
        elif helpButton.isHovered(getCursorPos()) and isLeftMouseClicked():
            helpScreen("pause")
        elif quitButton.isHovered(getCursorPos()) and isLeftMouseClicked():
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
    """
    This function checks if two objects collide. Every parameter with a 1 is for the first object, and every parameter
    with a 2 is for the second object. The minimum X value (minX) is for the lowest X value of the object. The maximum
    X value (maxX) is for the highest X value of the object. The minimum Y value (minY) is for the lowest Y value of
    the object. The maximum Y value (maxY) is for the highest Y value of the object.

    The function checks if the minimum or maximum X value of object 1 is within the minimum and maximum X value of
    object 2, and also if the minimum or maximum Y value of object 2 is within the minimum and maximum Y value of
    object 1. It returns a boolean of whether or not the objects have collided (basically if the conditions above are
    true or false).
    :param minX1:
    :param maxX1:
    :param minY1:
    :param maxY1:
    :param minX2:
    :param maxX2:
    :param minY2:
    :param maxY2:
    :return:
    """
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
