import pygame
import time
import random

# Image Assignments
idleImages = [pygame.image.load("../Roboto/images/darkrobot/Idle1.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle2.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle3.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle4.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle5.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle6.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle7.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle8.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle9.png"),
              pygame.image.load("../Roboto/images/darkrobot/Idle10.png")]

idleShootImages = [pygame.image.load("../Roboto/images/darkrobot/Shoot1.png"),
                   pygame.image.load("../Roboto/images/darkrobot/Shoot2.png"),
                   pygame.image.load("../Roboto/images/darkrobot/Shoot3.png"),
                   pygame.image.load("../Roboto/images/darkrobot/Shoot4.png")]

bulletImages = [pygame.image.load("../Roboto/images/projectiles/EnemyBullet1.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyBullet2.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyBullet3.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyBullet4.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyBullet5.png")]

muzzleImages = [pygame.image.load("../Roboto/images/projectiles/EnemyMuzzle1.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyMuzzle2.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyMuzzle3.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyMuzzle4.png"),
                pygame.image.load("../Roboto/images/projectiles/EnemyMuzzle5.png")]

deadImages = [pygame.image.load("../Roboto/images/darkrobot/Dead1.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead2.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead3.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead4.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead5.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead6.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead7.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead8.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead9.png"),
              pygame.image.load("../Roboto/images/darkrobot/Dead10.png")]

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


def leftImageMode(image):
    return pygame.transform.flip(image, True, False)


# Player Images/Assignments
rightPlayer = pygame.transform.scale(idleImages[0], (130, 130))
leftPlayer = leftImageMode(rightPlayer)

class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y, display):
        # Core Variables
        self.x = x
        self.y = y
        self.width = 130
        self.height = 130
        self.velocity = 5
        self.currentPlayer = rightPlayer
        self.display = display
        self.playerBounds = [self.x + 30, self.x + 90, self.y + 15, self.y + 120]
        self.hasRestarted = False

        # Player States
        self.jumping = False
        self.isShooting = False
        self.direction = "right"
        self.firstMove = True
        self.isDead = False
        self.gotShot = False

        # Image Cycle Counters
        self.idleCycleCount = 0
        self.idleShootCount = 0
        self.runCycleCount = 0
        self.runShootCycleCount = 0
        self.jumpShootCycleCount = 0
        self.bulletCycleCount = 0
        self.deadCycleCount = 0

        # Jumping Variables
        self.jumpCounter = 12
        self.jumpBound = self.jumpCounter
        self.lastJump = 0

        # Shooting Variables
        self.shootRange = 140
        self.shootPos = self.shootRange
        self.currentBullet = bulletImages[0]
        self.lastShot = int(round(time.time() * 1000))
        self.keepShooting = False
        self.firstShot = False
        self.currentX = 0
        self.currentY = 0
        self.currentDirection = self.direction
        self.muzzleImagesCount = 0
        self.muzzle = muzzleImages[0]
        self.hasShot = False
        self.finishedShot = True
        self.bulletX = 0
        self.bulletY = 0
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
        self.firstMove = False
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
                self.currentPlayer = leftImageMode(pygame.transform.scale(runImages[self.runCycleCount // 3],
                                                            (self.width, self.height)))
        

        elif direction == "right" and self.x < 600:
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

    @staticmethod
    def playShotSound():
        shootingSound = "../Roboto/music/Blaster.wav"
        shootingSoundEffect = pygame.mixer.Sound(shootingSound)
        shootingSoundEffect.set_volume(0.2)
        shootingSoundEffect.play()

    def shoot(self):
        if self.shootPos == 0:
            self.currentX = self.x
            self.currentY = self.y
            self.currentDirection = self.direction
            self.finishedShot = False
            self.playShotSound()
        if self.shootPos < self.shootRange:
            if 30 < self.bulletX < 750:
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
                self.updateBulletBounds()
            else:
                self.endShot()
                self.bulletBounds = [0, 0, 0, 0]
        else:
            self.endShot()
            self.bulletBounds = [0, 0, 0, 0]

    def endShot(self):
        if self.muzzleImagesCount < ((len(muzzleImages) - 1) * 3) - 1 and not self.finishedShot:
            self.muzzleImagesCount += 1
            self.shootPos += 5
            if self.currentDirection == "right":
                self.muzzle = pygame.transform.scale(muzzleImages[self.muzzleImagesCount // 3], (19, 50))
                self.bulletX = self.currentX + self.shootPos + (self.width / 2) + 20
            else:
                self.muzzle = leftImageMode(pygame.transform.scale(muzzleImages[self.muzzleImagesCount // 3], (19, 50)))
                self.bulletX = self.currentX - self.shootPos
            self.bulletY = self.currentY + (self.height / 2) - 20
            self.display.blit(self.muzzle, (self.bulletX, self.bulletY))
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
        self.hasShot = False
        self.isShooting = False
        self.lastShot = int(round(time.time() * 1000))
        self.muzzleImagesCount = 0
        self.shootPos = 0
        self.updateBulletBounds()

    def updateBounds(self):
        if self.direction == "right":
            self.playerBounds = [self.x + 30, self.x + 90, self.y + 15, self.y + 120]
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
                self.currentPlayer = pygame.transform.scale(deadImages[self.deadCycleCount // 8], (self.width, self.height))
            else:
                self.currentPlayer = leftImageMode(pygame.transform.scale(deadImages[self.deadCycleCount // 8], (self.width, self.height)))
        elif not pronounceDead:
            self.isDead = True

    def resetRoboto(self):
        self.isDead = False
        self.gotShot = False
        self.deadCycleCount = 0
        self.hasRestarted = True
        self.updateBounds()
        self.currentDirection = "right"
