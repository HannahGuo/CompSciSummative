import pygame
import time

imageWidth = 130
imageHeight = 130

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


def leftImageMode(player):
    return pygame.transform.flip(player, True, False)


# Player Images/Assignments
rightPlayer = pygame.transform.scale(idleImages[0], (imageWidth, imageHeight))
leftPlayer = leftImageMode(rightPlayer)


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = imageWidth
        self.height = imageHeight
        self.velocity = 10
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

    def idleAnimation(self):
        self.idleCycleCount += 1
        if self.idleCycleCount > ((len(idleImages) - 1) * 3) - 1:
            self.idleCycleCount = 0
        if self.goingLeft:
            self.currentPlayer = leftImageMode(
                pygame.transform.scale(idleImages[self.idleCycleCount // 3], (imageWidth, imageHeight)))
        else:
            self.currentPlayer = pygame.transform.scale(idleImages[self.idleCycleCount // 3],
                                                          (imageWidth, imageHeight))

    def movingAnimation(self, direction):
        if direction == "left":
            self.x -= self.velocity
            self.runCycleCount += 1
            self.goingRight = False
            self.goingLeft = True
            self.firstMove = False
            if self.runCycleCount > ((len(runImages) - 1) * 3) - 1:
                self.runCycleCount = 0
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
            self.runCycleCount += 1
            self.goingRight = True
            self.goingLeft = False
            self.firstMove = False
            if self.runCycleCount > ((len(runImages) - 1) * 3) - 1:
                self.runCycleCount = 0
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
