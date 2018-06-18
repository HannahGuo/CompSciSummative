import pygame
import time

# Image Assignments
idleImages = [pygame.image.load("../Roboto/images/robot/Idle1.png"),
              pygame.image.load("../Roboto/images/robot/Idle2.png"),
              pygame.image.load("../Roboto/images/robot/Idle3.png"),
              pygame.image.load("../Roboto/images/robot/Idle4.png"),
              pygame.image.load("../Roboto/images/robot/Idle5.png"),
              pygame.image.load("../Roboto/images/robot/Idle6.png"),
              pygame.image.load("../Roboto/images/robot/Idle7.png"),
              pygame.image.load("../Roboto/images/robot/Idle8.png"),
              pygame.image.load("../Roboto/images/robot/Idle9.png"),
              pygame.image.load("../Roboto/images/robot/Idle10.png")]

runImages = [pygame.image.load("../Roboto/images/robot/Run1.png"),
             pygame.image.load("../Roboto/images/robot/Run2.png"),
             pygame.image.load("../Roboto/images/robot/Run3.png"),
             pygame.image.load("../Roboto/images/robot/Run4.png"),
             pygame.image.load("../Roboto/images/robot/Run5.png"),
             pygame.image.load("../Roboto/images/robot/Run6.png"),
             pygame.image.load("../Roboto/images/robot/Run7.png"),
             pygame.image.load("../Roboto/images/robot/Run8.png")]

jumpImages = [pygame.image.load("../Roboto/images/robot/Jump1.png"),
              pygame.image.load("../Roboto/images/robot/Jump2.png"),
              pygame.image.load("../Roboto/images/robot/Jump3.png"),
              pygame.image.load("../Roboto/images/robot/Jump4.png"),
              pygame.image.load("../Roboto/images/robot/Jump5.png"),
              pygame.image.load("../Roboto/images/robot/Jump6.png"),
              pygame.image.load("../Roboto/images/robot/Jump7.png"),
              pygame.image.load("../Roboto/images/robot/Jump8.png")]

idleShootImages = [pygame.image.load("../Roboto/images/robot/Shoot1.png"),
                   pygame.image.load("../Roboto/images/robot/Shoot2.png"),
                   pygame.image.load("../Roboto/images/robot/Shoot3.png"),
                   pygame.image.load("../Roboto/images/robot/Shoot4.png")]

runShootImages = [pygame.image.load("../Roboto/images/robot/RunShoot1.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot2.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot3.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot4.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot5.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot6.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot7.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot8.png"),
                  pygame.image.load("../Roboto/images/robot/RunShoot9.png")]

jumpShootImages = [pygame.image.load("../Roboto/images/robot/JumpShoot1.png"),
                   pygame.image.load("../Roboto/images/robot/JumpShoot2.png"),
                   pygame.image.load("../Roboto/images/robot/JumpShoot3.png"),
                   pygame.image.load("../Roboto/images/robot/JumpShoot4.png"),
                   pygame.image.load("../Roboto/images/robot/JumpShoot5.png")]

bulletImages = [pygame.image.load("../Roboto/images/projectiles/PlayerBullet1.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerBullet2.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerBullet3.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerBullet4.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerBullet5.png")]

muzzleImages = [pygame.image.load("../Roboto/images/projectiles/PlayerMuzzle1.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerMuzzle2.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerMuzzle3.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerMuzzle4.png"),
                pygame.image.load("../Roboto/images/projectiles/PlayerMuzzle5.png")]

deadImages = [pygame.image.load("../Roboto/images/robot/Dead1.png"),
              pygame.image.load("../Roboto/images/robot/Dead2.png"),
              pygame.image.load("../Roboto/images/robot/Dead3.png"),
              pygame.image.load("../Roboto/images/robot/Dead4.png"),
              pygame.image.load("../Roboto/images/robot/Dead5.png"),
              pygame.image.load("../Roboto/images/robot/Dead6.png"),
              pygame.image.load("../Roboto/images/robot/Dead7.png"),
              pygame.image.load("../Roboto/images/robot/Dead8.png"),
              pygame.image.load("../Roboto/images/robot/Dead9.png"),
              pygame.image.load("../Roboto/images/robot/Dead10.png")]


def leftImageMode(image):
    return pygame.transform.flip(image, True, False)


# Player Images/Assignments
rightPlayer = pygame.transform.scale(idleImages[0], (130, 130))
leftPlayer = leftImageMode(rightPlayer)


class player:
    def __init__(self, x, y, display):
        # Core Variables
        self.x = x  # this control's the player's x position on the display, and is initially assigned to the x
                    # parameter when an instance of this class is created
        self.y = y  # this control's the player's y position, and is initially assigned to the y parameter when an
                    # instance of this class is created
        self.width = 130  # this is the integer width of the player's image and is used for calculations of the player's
                          # position as well as scaling
        self.height = 130  # this is the integer height of the player's image and is used for calculations of the
                           # player's position as well as scaling
        self.velocity = 6  # this is the player's velocity, which is how many pixels they move every time they move.
                           # It's currently set to 6, however if it were to be tuned lower/higher, the player would move
                           # slower/faster.
        self.currentPlayer = rightPlayer  # this stores the current player image that is to be displayed. It's used for
                                          # all the sprite animations and player states. It's initial value is the
                                          # idle image for the right player.
        self.display = display  # this is the pygame display that the player/shots will be blit to. It's
                                # assigned to the display parameter that is passed into this class.
        self.playerBounds = [self.x + 30, self.x + 85, self.y + 15, self.y + 120]  # the playerBounds is a list of the
                                                                                   # player's minimum x, maximum x,
                                                                                   # minimum y and maximum y values.
                                                                                   # This is used to calculate hit boxes
                                                                                   # and updates whenever the robot
                                                                                   # moves.
        # Player States
        self.jumping = False  # this stores a boolean value of if the robot is jumping. It's used to run the jump
                              # function. It's initially set to False because the player starts in an idle position. It
                              # changes to True when the user presses the UP arrow key.
        self.isShooting = False  # this stores a boolean value of if the robot is shooting. It's used to run the shoot
                                 # function and to display the player's shooting sprites based on their current
                                 # movement (idle, running or jumping). It's initially set to False because the player
                                 # hasn't shot yet. It changes to True when the user presses the space bar.
        self.gotShot = False  # this stores the boolean value of if this player has collided with another bullet. It
                              # turns to True when the player collides with the enemy's bullet. This allows the program
                              # to cycle through the player's death animation.
        self.keepShooting = False  # this is a boolean that checks if the player should keep shooting. This turns to
                                   # True when the space bar is held.
        self.finishedShot = True  # this variable holds the boolean value of if the user has finished shooting, which
                                  # happens after the endShot() functions finishes running. It's initially set to True
                                  # because otherwise a shot would generate on the screen initially.
        self.isDead = False  # this stores a boolean value of if the player is dead or not. This turns to True when the
                             # player's death animation finishes running. The death animation starts running after the
                             # player has collided with the enemy's bullet.
        self.hasRestarted = False  # this boolean holds the value of if the game has restarted. It's set to true when
                                   # the game restarts.
        self.direction = "right"  # this string value stores the direction that the player is moving. It has two
                                  # possible values; "left" when the player presses the left arrow key and "right" when
                                  # the user presses the right arrow key. The default value is "right" since we want the
                                  # player to be facing right. This variable controls the direction of the sprites
                                  # that are blit to the screen.

        # Image Cycle Counters -- These counters allow the program to cycle through the sprites to animate them. They
        # are reset to 0 when the animation resets.
        self.idleCycleCount = 0  # image cycle counter for the idle animation.
        self.idleShootCount = 0  # image cycle counter for the idle and shooting animation.
        self.runCycleCount = 0   # image cycle counter for the running animation.
        self.runShootCycleCount = 0   # image cycle counter for the running and shooting animation.
        self.jumpShootCycleCount = 0  # image cycle counter for the jumping and shooting animation.
        self.bulletCycleCount = 0   # image cycle counter for the bullet animation.
        self.muzzleImagesCount = 0  # image cycle counter for the muzzle animation.
        self.deadCycleCount = 0     # image cycle counter for the death animation.

        # Jumping Variables
        self.jumpCounter = 13  # this integer controls how high the player's jump will be. It changes during a jump.
        self.jumpBound = self.jumpCounter  # this variable is the jump's boundaries that can be referenced to reset the
                                           # jumpCounter. jumpBound's value doesn't change.
        self.lastJump = 0  # this acts as a timer for when the player last jumped. It's initially set to 0, but is
                           # later assigned to the system's current time in milliseconds. This makes sure that the
                           # user doesn't jump repeatedly if the up arrow key is held.

        # Shooting Variables
        self.shootRange = 140  # this integer value controls how many pixels the shot will travel.
        self.shootPos = self.shootRange  # shootPos is the shot's current position. It's initially set to the shootRange
                                         # but changes based on where the shot is.
        self.currentBullet = bulletImages[0]  # this stores the current bullet image that is to be displayed. It's used
                                              # for all the bullet animations. It's initial value is first
                                              # bullet image.
        self.currentMuzzle = muzzleImages[0]  # this stores the muzzle image that is to be displayed. It's used
                                              # for all the muzzle animations. It's initial value is first
                                              # bullet image.
        self.lastShot = 0  # this acts as a timer for when the player last shot. It's initially set to 0, but is later
                           # assigned to the system's current time in milliseconds. This makes sure that the user
                           # doesn't shoot non-stop when they hold the space bar.
        self.currentX = 0  # this is the player's current x value when they shoot. It's used at the beginning of the
                           # shot to make sure that the shot doesn't move when the player does (i.e. not relative to
                           # wherever the player moves as the shot is traveling, but rather their position when they
                           # shoot.) It's used to calculate the x value of the bullet and reset whenever the player
                           # shoots.
        self.currentY = 0  # this is the player's current Y value when they shoot. It's used at the beginning of the
                           # shot to make sure that the shot doesn't move when the player does (i.e. not relative to
                           # wherever the player moves as the shot is traveling, but rather their position when they
                           # shoot.) It's used to calculate the y value of the bullet. It's used to calculate the x
                           # value of the bullet and reset whenever the player shoots.
        self.currentDirection = self.direction  # this is the player's current direction when they shoot. It works the
                                                # same as the direction variable. It's used at the beginning of the shot
                                                # to make sure that the bullet doesn't switch directions when the player
                                                # does. This also makes sure that the bullet's image is facing the
                                                # direction it is traveling.
        self.bulletX = 0  # this holds the value of the bullet's current X position. It's similar to shootPos, but also
                          # accounts for the bullet's width.
        self.bulletY = 0  # this holds the value of the bullet's current Y position. It's similar to shootPos, but also
                          # accounts for the bullet's height.
        # bulletBounds is a list of the bullet's minimum x, maximum x, minimum y and maximum y values. This is used to
        # calculate hit boxes and updates whenever the bullet moves.
        self.bulletBounds = [self.bulletX, self.bulletX + 35, self.bulletY + 40, self.bulletY]

    def idleAnimation(self):
        if not self.isShooting and not self.keepShooting:
            self.idleCycleCount += 1
            if self.idleCycleCount > ((len(idleImages) - 1) * 3) - 1:
                self.idleCycleCount = 0
            if self.direction == "left":
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(idleImages[self.idleCycleCount // 3], (self.width, self.height)))
            else:
                self.currentPlayer = pygame.transform.scale(idleImages[self.idleCycleCount // 3],
                                                            (self.width, self.height))
        else:
            self.idleShootCount += 1
            if self.idleShootCount > ((len(idleShootImages) - 1) * 3) - 1:
                self.idleShootCount = 0
            if self.direction == "left":
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(idleShootImages[self.idleShootCount // 3], (self.width, self.height)))
            else:
                self.currentPlayer = pygame.transform.scale(idleShootImages[self.idleShootCount // 3],
                                                            (self.width, self.height))

    def movingAnimation(self, direction):
        if self.runCycleCount > ((len(runImages) - 1) * 3) - 1:
            self.runCycleCount = 0
        self.runCycleCount += 1

        if direction == "left":
            self.x -= self.velocity
            self.direction = direction
            if self.isShooting:
                self.runShootCycleCount += 1
                if self.runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                    self.runShootCycleCount = 0
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(runShootImages[self.runShootCycleCount // 3], (self.width, self.height)))
            else:
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(runImages[self.runCycleCount // 3], (self.width, self.height)))

        elif direction == "right":
            if self.x < 580:
                self.x += self.velocity
                self.direction = direction
                if self.isShooting:
                    self.runShootCycleCount += 1
                    if self.runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                        self.runShootCycleCount = 0
                    self.currentPlayer = pygame.transform.scale(runShootImages[self.runShootCycleCount // 3],
                                                                (self.width, self.height))
                else:
                    self.currentPlayer = pygame.transform.scale(runImages[self.runCycleCount // 3],
                                                                (self.width, self.height))
            else:
                self.idleAnimation()
        self.updateBounds()

    def jump(self):
        if self.jumpCounter >= -self.jumpBound:
            self.y -= (self.jumpCounter * 2)
            self.jumpCounter -= 1
            if self.direction == "right":
                if self.isShooting:
                    self.jumpShootCycleCount += 1
                    if self.jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                        self.jumpShootCycleCount = 0
                    self.currentPlayer = pygame.transform.scale(runShootImages[self.jumpShootCycleCount // 3],
                                                                (self.width, self.height))
                else:
                    self.currentPlayer = pygame.transform.scale(jumpImages[self.jumpCounter // 3],
                                                                (self.width, self.height))
                    self.updateBounds()
            else:
                if self.isShooting:
                    self.jumpShootCycleCount += 1
                    if self.jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                        self.jumpShootCycleCount = 0
                    self.currentPlayer = leftImageMode(
                        pygame.transform.scale(runShootImages[self.jumpShootCycleCount // 3],
                                               (self.width, self.height)))
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(jumpImages[self.jumpCounter // 3], (self.width, self.height)))
        else:
            self.jumpCounter = self.jumpBound
            self.jumping = False
            self.lastJump = int(round(time.time() * 1000))

    def shoot(self):
        if self.shootPos == 0:
            self.currentX = self.x
            self.currentY = self.y
            self.currentDirection = self.direction
            self.finishedShot = False
            self.playShotSound()
            self.resetBulletBounds()
        else:
            self.updateBulletBounds()
        if self.shootPos < self.shootRange:
            if 30 < self.bulletX < 700:
                if self.bulletCycleCount > ((len(bulletImages) - 1) * 5) - 1:
                    self.bulletCycleCount = 0
                self.shootPos += 7
                self.bulletCycleCount += 1
                if self.currentDirection == "right":
                    self.currentBullet = pygame.transform.scale(bulletImages[self.bulletCycleCount // 5], (40, 40))
                    self.bulletX = self.currentX + self.shootPos + (self.width / 2) + 20
                else:
                    self.currentBullet = leftImageMode(pygame.transform.scale(bulletImages[self.bulletCycleCount // 5],
                                                                              (40, 40)))
                    self.bulletX = self.currentX - self.shootPos
                self.bulletY = self.currentY + (self.height / 2) - 20
                self.display.blit(self.currentBullet, (self.bulletX, self.bulletY))
            else:
                self.endShot()
        else:
            self.endShot()

    def endShot(self):
        if self.muzzleImagesCount < ((len(muzzleImages) - 1) * 3) - 1 and not self.finishedShot:
            self.muzzleImagesCount += 1
            if self.currentDirection == "right":
                self.currentMuzzle = pygame.transform.scale(muzzleImages[self.muzzleImagesCount // 3], (19, 50))
                self.bulletX = self.currentX + self.shootPos + (self.width / 2) + 20
            else:
                self.currentMuzzle = leftImageMode(pygame.transform.scale(muzzleImages[self.muzzleImagesCount // 3],
                                                                          (19, 50)))
                self.bulletX = self.currentX - self.shootPos
            self.bulletY = self.currentY + (self.height / 2) - 20
            self.display.blit(self.currentMuzzle, (self.bulletX, self.bulletY))
        else:
            self.restartShot()

    def resetShooting(self):
        self.bulletCycleCount = 0
        self.finishedShot = True
        self.isShooting = False
        self.lastShot = int(round(time.time() * 1000))
        self.muzzleImagesCount = 0
        self.shootPos = self.shootRange

    def restartShot(self):
        self.bulletCycleCount = 0
        self.finishedShot = True
        self.isShooting = False
        self.lastShot = int(round(time.time() * 1000))
        self.muzzleImagesCount = 0
        self.shootPos = 0
        self.updateBulletBounds()

    def updateBounds(self):
        if self.direction == "right":
            self.playerBounds = [self.x + 30, self.x + 85, self.y + 15, self.y + 120]
        else:
            self.playerBounds = [self.x + 100, self.x + 40, self.y + 15, self.y + 120]

    def updateBulletBounds(self):
        if self.direction == "right":
            self.bulletBounds = [self.bulletX, self.bulletX + 35, self.bulletY + 40, self.bulletY]
        else:
            self.bulletBounds = [self.bulletX, self.bulletX + 35, self.bulletY + 40, self.bulletY]

    def resetBulletBounds(self):
        self.bulletBounds = [0, 0, 0, 0]

    def ripRoboto(self, pronounceDead):
        if self.deadCycleCount < ((len(deadImages) - 1) * 8) - 1 and self.gotShot:
            self.deadCycleCount += 1
            self.y = 600 - 155 - (130 / 2)

            if self.direction == "right":
                self.currentPlayer = pygame.transform.scale(deadImages[self.deadCycleCount // 8],
                                                            (self.width, self.height))
            else:
                self.currentPlayer = leftImageMode(pygame.transform.scale(deadImages[self.deadCycleCount // 8],
                                                                          (self.width, self.height)))
        elif not pronounceDead:
            self.isDead = True

    def resetRoboto(self):
        self.isDead = False
        self.gotShot = False
        self.deadCycleCount = 0
        self.hasRestarted = True
        self.updateBounds()
        self.currentDirection = "right"
