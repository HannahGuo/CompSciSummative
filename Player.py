import pygame
import time

imageWidth = 130
imageHeight = 130

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

bulletImages = [pygame.image.load("../Roboto/images/projectiles/Bullet1.png"),
                pygame.image.load("../Roboto/images/projectiles/Bullet2.png"),
                pygame.image.load("../Roboto/images/projectiles/Bullet3.png"),
                pygame.image.load("../Roboto/images/projectiles/Bullet4.png"),
                pygame.image.load("../Roboto/images/projectiles/Bullet5.png")]

muzzleImages = [pygame.image.load("../Roboto/images/projectiles/Muzzle1.png"),
                pygame.image.load("../Roboto/images/projectiles/Muzzle2.png"),
                pygame.image.load("../Roboto/images/projectiles/Muzzle3.png"),
                pygame.image.load("../Roboto/images/projectiles/Muzzle4.png"),
                pygame.image.load("../Roboto/images/projectiles/Muzzle5.png")]


def leftImageMode(player):
    return pygame.transform.flip(player, True, False)


# Player Images/Assignments
rightPlayer = pygame.transform.scale(idleImages[0], (imageWidth, imageHeight))
leftPlayer = leftImageMode(rightPlayer)


class player(object):
    def __init__(self, x, y, display):
        # Core Variables
        self.x = x
        self.y = y
        self.width = imageWidth
        self.height = imageHeight
        self.velocity = 5
        self.currentPlayer = rightPlayer
        self.display = display

        # Player States
        self.jumping = False
        self.isShooting = False
        self.goingLeft = False
        self.goingRight = True
        self.firstMove = True

        # Image Cycle Counters
        self.idleCycleCount = 0
        self.idleShootCount = 0
        self.runCycleCount = 0
        self.runShootCycleCount = 0
        self.jumpShootCycleCount = 0
        self.bulletCycleCount = 0

        # Jumping Variables
        self.jumpCounter = 12
        self.jumpBound = self.jumpCounter
        self.lastJump = 0

        # Shooting Variables
        self.shootRange = 150
        self.shootPos = self.shootRange
        self.currentBullet = bulletImages[0]
        self.lastShot = int(round(time.time() * 1000))
        self.keepShooting = False
        self.firstShot = False
        self.currentX = 0
        self.currentY = 0
        self.currentDirection = "right"
        self.muzzleImagesCount = 0
        self.muzzle = muzzleImages[0]
        self.hasShot = False
        self.finishedShot = True

    def idleAnimation(self):
        if not self.isShooting and not self.keepShooting:
            self.idleCycleCount += 1
            if self.idleCycleCount > ((len(idleImages) - 1) * 3) - 1:
                self.idleCycleCount = 0
            if self.goingLeft:
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(idleImages[self.idleCycleCount // 3], (imageWidth, imageHeight)))
            else:
                self.currentPlayer = pygame.transform.scale(idleImages[self.idleCycleCount // 3],
                                                            (imageWidth, imageHeight))
        else:
            self.idleShootCount += 1
            if self.idleShootCount > ((len(idleShootImages) - 1) * 3) - 1:
                self.idleShootCount = 0
            if self.goingLeft:
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(idleShootImages[self.idleShootCount // 3], (imageWidth, imageHeight)))
            else:
                self.currentPlayer = pygame.transform.scale(idleShootImages[self.idleShootCount // 3],
                                                            (imageWidth, imageHeight))

    def movingAnimation(self, direction):
        self.firstMove = False
        if self.runCycleCount > ((len(runImages) - 1) * 3) - 1:
            self.runCycleCount = 0
        self.runCycleCount += 1

        if direction == "left":
            self.x -= self.velocity
            self.goingRight = False
            self.goingLeft = True
            if self.isShooting:
                self.runShootCycleCount += 1
                if self.runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                    self.runShootCycleCount = 0
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(runShootImages[self.runShootCycleCount // 3], (imageWidth, imageHeight)))
            else:
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(runImages[self.runCycleCount // 3], (imageWidth, imageHeight)))

        elif direction == "right":
            self.x += self.velocity
            self.goingRight = True
            self.goingLeft = False
            if self.isShooting:
                self.runShootCycleCount += 1
                if self.runShootCycleCount > ((len(runShootImages) - 1) * 3) - 1:
                    self.runShootCycleCount = 0
                self.currentPlayer = pygame.transform.scale(runShootImages[self.runShootCycleCount // 3],
                                                            (imageWidth, imageHeight))
            else:
                self.currentPlayer = pygame.transform.scale(runImages[self.runCycleCount // 3],
                                                            (imageWidth, imageHeight))

    def jump(self):
        if self.jumpCounter >= -self.jumpBound:
            self.y -= (self.jumpCounter * 2)
            self.jumpCounter -= 1
            if self.goingRight:
                if self.isShooting:
                    self.jumpShootCycleCount += 1
                    if self.jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                        self.jumpShootCycleCount = 0
                    self.currentPlayer = pygame.transform.scale(runShootImages[self.jumpShootCycleCount // 3],
                                                                (imageWidth, imageHeight))
                else:
                    self.currentPlayer = pygame.transform.scale(jumpImages[self.jumpCounter // 3],
                                                                (imageWidth, imageHeight))
            else:
                if self.isShooting:
                    self.jumpShootCycleCount += 1
                    if self.jumpShootCycleCount > ((len(jumpShootImages) - 1) * 3) - 1:
                        self.jumpShootCycleCount = 0
                    self.currentPlayer = leftImageMode(
                        pygame.transform.scale(runShootImages[self.jumpShootCycleCount // 3],
                                               (imageWidth, imageHeight)))
                self.currentPlayer = leftImageMode(
                    pygame.transform.scale(jumpImages[self.jumpCounter // 3], (imageWidth, imageHeight)))
        else:
            self.jumpCounter = self.jumpBound
            self.jumping = False
            self.lastJump = int(round(time.time() * 1000))

    def shoot(self):
        if self.shootPos == 0:
            self.currentX = self.x
            self.currentY = self.y
            self.currentDirection = "right" if self.goingRight else "left"
            self.finishedShot = False
            shootingSound = "../Roboto/music/Blaster.wav"
            shootingSoundEffect = pygame.mixer.Sound(shootingSound)
            shootingSoundEffect.set_volume(0.2)
            shootingSoundEffect.play()
            pygame.mixer.init()
        if self.shootPos < self.shootRange:
            if self.bulletCycleCount > ((len(bulletImages) - 1) * 5) - 1:
                self.bulletCycleCount = 0
            self.shootPos += 5
            self.bulletCycleCount += 1
            if self.currentDirection == "right":
                self.currentBullet = pygame.transform.scale(bulletImages[self.bulletCycleCount // 5], (40, 40))
                self.display.blit(self.currentBullet, (self.currentX + self.shootPos + (self.width / 2) + 20,
                                                       self.currentY + (imageHeight / 2) - 20))
            else:
                self.currentBullet = leftImageMode(pygame.transform.scale(bulletImages[self.bulletCycleCount // 5], (40, 40)))
                self.display.blit(self.currentBullet, (self.currentX - self.shootPos, self.currentY + (imageHeight / 2) - 20))
        else:
            if self.muzzleImagesCount < ((len(muzzleImages) - 1) * 3) - 1 and not self.finishedShot:
                self.muzzleImagesCount += 1
                self.shootPos += 5
                if self.currentDirection == "right":
                    self.muzzle = pygame.transform.scale(muzzleImages[self.muzzleImagesCount // 3], (19, 50))
                    self.display.blit(self.muzzle, (
                        self.currentX + self.shootPos + (self.width / 2) + 20, self.currentY + (imageHeight / 2) - 20))
                else:
                    self.muzzle = leftImageMode(
                        pygame.transform.scale(muzzleImages[self.muzzleImagesCount // 3], (19, 50)))
                    self.display.blit(self.muzzle,
                                      (self.currentX - self.shootPos, self.currentY + (imageHeight / 2) - 20))
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
