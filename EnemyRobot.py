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


def leftImageMode(image):
    return pygame.transform.flip(image, True, False)


# Player Images/Assignments
leftPlayer = leftImageMode(pygame.transform.scale(idleImages[0], (130, 130)))


class enemy:
    def __init__(self, x, y, display):
        # Core Variables
        self.x = x
        self.y = y
        self.width = 130
        self.height = 130
        self.currentEnemy = leftPlayer
        self.display = display
        self.playerBounds = [self.x + 30, self.x + 90, self.y + 15, self.y + 120]

        # Player States
        self.isShooting = False

        # Image Cycle Counters
        self.idleCycleCount = 0
        self.idleShootCount = 0
        self.bulletCycleCount = 0

        # Shooting Variables
        self.shootRange = random.randint(150, 350)
        self.shotVelocity = random.randint(6, 16)
        self.shootPos = 0
        self.currentBullet = bulletImages[0]
        self.lastShot = int(round(time.time() * 1000))
        self.firstShot = False
        self.muzzleImagesCount = 0
        self.muzzle = muzzleImages[0]
        self.hasShot = False
        self.finishedShot = True
        self.bulletX = 0
        self.bulletY = self.y + (self.height / 2) - 20
        self.randomInterval = random.randint(200, 800)
        self.bulletBounds = [self.bulletX, self.bulletX + 35, self.bulletY + 40, self.bulletY + 8]

    def idleAnimation(self):
        if not self.isShooting:
            self.idleCycleCount += 1
            if self.idleCycleCount > ((len(idleImages) - 1) * 3) - 1:
                self.idleCycleCount = 0
            self.currentEnemy = leftImageMode(pygame.transform.scale(idleImages[self.idleCycleCount // 3],
                                                                     (self.width, self.height)))
        else:
            self.idleShootCount += 1
            if self.idleShootCount > ((len(idleShootImages) - 1) * 3) - 1:
                self.idleShootCount = 0
            self.currentEnemy = leftImageMode(pygame.transform.scale(idleShootImages[self.idleShootCount // 3],
                                                                     (self.width, self.height)))

    def shoot(self):
        self.isShooting = True
        self.updateBulletBounds()
        if self.shootPos == 0:
            self.resetBulletBounds()
            self.finishedShot = False
        if self.shootPos < self.shootRange and 30 < self.bulletX < 750:
            if self.bulletCycleCount > ((len(bulletImages) - 1) * 5) - 1:
                self.bulletCycleCount = 0
            self.shootPos += self.shotVelocity
            self.bulletCycleCount += 1
            self.currentBullet = leftImageMode(pygame.transform.scale(bulletImages[self.bulletCycleCount // 5],
                                                                      (40, 40)))
            self.bulletX = self.x - self.shootPos
            self.display.blit(self.currentBullet, (self.bulletX, self.bulletY))
        else:
            self.resetBulletBounds()
            self.endShot()

    def endShot(self):
        if self.muzzleImagesCount < ((len(muzzleImages) - 1) * 3) - 1 and not self.finishedShot:
            self.muzzleImagesCount += 1
            self.muzzle = leftImageMode(pygame.transform.scale(muzzleImages[self.muzzleImagesCount // 3], (19, 50)))
            self.bulletX = self.x - self.shootPos
            self.display.blit(self.muzzle, (self.bulletX, self.bulletY))
        else:
            self.resetShooting()

    def resetShooting(self):
        self.bulletCycleCount = 0
        self.finishedShot = True
        self.hasShot = False
        self.lastShot = int(round(time.time() * 1000))
        self.muzzleImagesCount = 0
        self.randomInterval = random.randint(100, 2500)
        self.shootPos = 0
        self.shootRange = random.randint(150, 350)
        self.shotVelocity = random.randint(6, 16)
        self.resetBulletBounds()

    def updateBulletBounds(self):
        self.bulletBounds = [self.bulletX, self.bulletX + 35, self.bulletY + 40, self.bulletY + 3]

    def resetBulletBounds(self):
        self.bulletBounds = [0, 0, 0, 0]
