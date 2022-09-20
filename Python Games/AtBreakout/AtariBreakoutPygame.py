import pygame
import random

pygame.init()

screen = pygame.display.set_mode((700, 700))
font16 = pygame.font.Font('freesansbold.ttf', 16)

playerX = 250

ballX = 200
ballY = 200

brickX = 70
brickY = 40

speedP = 0.7
speedBH = 0.5
speedBV = 0.5
flagH = 1
flagV = 1
factor = 1
counter = 0

gameLoad = True
gameEnd = False
gameEndL = False
restart = True
start = True
row = 1
sets = 0
points = 0

flagL = False
flagR = False

lives = 3


def pointsButton(points):
    surf = pygame.Surface((100, 40))
    surf.fill((100, 149, 237))
    pygame.draw.rect(surf, (100, 149, 237), surf.get_rect())  # Draw on it.
    screen.blit(surf, (570, 650))

    text = font16.render("Points: " + str(points), True, (255, 255, 255))
    screen.blit(text, (582, 663))


def livesButton(lives):
    surf = pygame.Surface((100, 40))
    surf.fill((100, 149, 237))
    pygame.draw.rect(surf, (100, 149, 237), surf.get_rect())  # Draw on it.
    screen.blit(surf, (30, 650))

    text = font16.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(text, (42, 663))


def winButton(points):
    surf = pygame.Surface((200, 40))
    pygame.draw.rect(surf, (100, 149, 237), surf.get_rect())  # Draw on it.
    screen.blit(surf, (270, 300))

    text = font16.render("You won with " + str(points) + " points!", True, (255, 255, 255))
    screen.blit(text, (282, 313))


def tryAgainButton():
    surf = pygame.Surface((100, 40))
    pygame.draw.rect(surf, (100, 149, 237), surf.get_rect())  # Draw on it.
    screen.blit(surf, (320, 360))

    text = font16.render("Try Again?", True, (255, 255, 255))
    screen.blit(text, (332, 373))


def loseButton(points):
    surf = pygame.Surface((200, 40))
    pygame.draw.rect(surf, (100, 149, 237), surf.get_rect())  # Draw on it.
    screen.blit(surf, (270, 300))

    text = font16.render("You lost with " + str(points) + " points!", True, (255, 255, 255))
    screen.blit(text, (282, 313))


class Paddle(pygame.sprite.Sprite):
    def __init__(self, playerX):
        super().__init__()
        self.playerX = playerX
        self.image = pygame.Surface((80, 10))
        self.image.fill((127, 255, 212))
        self.rect = self.image.get_rect(center=(self.playerX, 650))

    def update(self):
        self.playerX = playerX
        self.rect.center = (self.playerX, 650)


class Ball(pygame.sprite.Sprite):
    def __init__(self, ballX, ballY):
        super().__init__()
        self.ballX = ballX
        self.ballY = ballY
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 182, 193))
        self.rect = self.image.get_rect(center=(self.ballX, self.ballY))
        
    def update(self):
        self.ballX = ballX
        self.ballY = ballY
        self.rect.center = (self.ballX, self.ballY)


class Brick(pygame.sprite.Sprite):
    def __init__(self, brickX, brickY, sets):
        super().__init__()
        self.health = 3 - sets
        self.brickX = brickX
        self.brickY = brickY
        self.image = pygame.Surface((80, 20))
        self.rect = self.image.get_rect(center=(self.brickX, self.brickY))
        self.count = 0
        self.supcount = 0

    def update(self):
        self.count += 1

        if self.count > 2:
            self.hit()
        if self.health == 3:
            self.image.fill((0, 0, 139))
        elif self.health == 2:
            self.image.fill((95, 158, 160))
        elif self.health == 1:
            self.image.fill((127, 255, 0))
        else:
            self.supcount += 1
            if self.supcount > 10:
                brickGroup.remove(self)

    def hit(self):
        if pygame.sprite.collide_rect(self, ball):
            self.health -= 1
            self.count = 0


paddle = Paddle(playerX)

paddleGroup = pygame.sprite.Group()
paddleGroup.add(paddle)

ball = Ball(ballX, ballY)

ballGroup = pygame.sprite.Group()
ballGroup.add(ball)

brickGroup = pygame.sprite.Group()

done = True

while done:
    counter += 1
    screen.fill((0, 0, 0))
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            flagR = True
        else:
            flagR = False

        if keys[pygame.K_LEFT]:
            flagL = True
        else:
            flagL = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 320 <= mouseX <= 420 and 360 <= mouseY <= 400 and (gameEnd or gameEndL):
                restart = True

        if event.type == pygame.QUIT:
            done = False

    if restart:
        ballX = 200
        ballY = 200
        gameEnd = False
        gameEndL = False
        gameLoad = True
        lives = 3
        sets = 0
        brickX = 70
        brickY = 40
        brickGroup.empty()
        if start:
            brick = Brick(brickX, brickY, sets)
            brickGroup.add(brick)
            brickX += 90
            start = False
        restart = False

    if flagL:
        if playerX < 40:
            playerX = 41
        else:
            playerX -= speedP

    if flagR:
        if playerX > 660:
            playerX = 659
        else:
            playerX += speedP

    if not gameLoad and not gameEnd and not gameEndL:
        ballX += (flagH * speedBH * factor)
        ballY += (flagV * speedBV)
    elif not gameEnd and not gameEndL:
        if counter > 50 and row < 6:
            x = Brick(brickX, brickY, sets)
            brickGroup.add(x)
            brickX += 90
            row += 1
            counter = 0
        elif counter > 50 and row == 6:
            x = Brick(brickX, brickY, sets)
            brickGroup.add(x)
            row = 0
            brickX = 70
            brickY += 30
            # print("New Row!")
            counter = 0
            sets += 1

        if sets == 3:
            points = 0
            gameLoad = False

    if ballX < 10 or ballX > 690:
        flagH = flagH * -1

    if ballY < 10:
        flagV = flagV * -1

    if pygame.sprite.collide_rect(ball, paddle) and counter > 50:
        factor = random.randint(-10, 10) * 0.1
        if factor < 0:
            flagH *= -1
        flagV = flagV * -1
        counter = 0

    collisions = pygame.sprite.groupcollide(brickGroup, ballGroup, False, False)

    if collisions and counter > 50:
        points += 1
        flagV = flagV * -1
        counter = 0

    if ballY > 690:
        lives -= 1
        ballX = 200
        ballY = 200

    if len(brickGroup.sprites()) == 0 and not start:
        gameEnd = True
        brickX = 70
        brickY = 40

    if lives == 0:
        gameEndL = True

    if gameEnd:
        winButton(points)
        tryAgainButton()

    if gameEndL:
        loseButton(points)
        tryAgainButton()

    pointsButton(points)
    livesButton(lives)

    paddleGroup.draw(screen)
    ballGroup.draw(screen)
    brickGroup.draw(screen)
    paddleGroup.update()
    ballGroup.update()
    brickGroup.update()

    pygame.display.flip()
    pygame.display.update()
