import pygame
from pygame import key

battle32 = pygame.image.load("battleship32.png")
battle64 = pygame.image.load("battleship64.png")
battle64 = pygame.transform. scale(battle64, (50, 50))
bullet64 = pygame.image.load("bullet.png")
bullet64 = pygame.transform. scale(bullet64, (30, 40))

enemy64 = pygame.image.load("skull.png")
enemy64 = pygame.transform. scale(enemy64, (50, 50))
pygame.init()
font16 = pygame.font.Font('freesansbold.ttf', 16)
screen = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Space Invaders(!)")
pygame.display.set_icon(battle32)
PlayerX = 600
PlayerY = 600

EnemyX = 120
EnemyY = 40


def conBut(points):
    button = pygame.Surface((100, 40))  # Create a Surface to draw on.
    button.fill((255, 255, 255))
    pygame.draw.rect(button, (138, 43, 226), button.get_rect())  # Draw on it.
    screen.blit(button, (570, 650))

    text = font16.render("Points: " + str(points), True, (127, 255, 212), (138, 43, 226))
    screen.blit(text, (582, 663))


def conBut2(lives):
    button = pygame.Surface((100, 40))  # Create a Surface to draw on.
    button.fill((255, 255, 255))
    pygame.draw.rect(button, (138, 43, 226), button.get_rect())  # Draw on it.
    screen.blit(button, (40, 650))

    text = font16.render("Lives: " + str(lives), True, (127, 255, 212), (138, 43, 226))
    screen.blit(text, (60, 663))


def conBut3():
    button = pygame.Surface((100, 40))  # Create a Surface to draw on.
    button.fill((255, 255, 255))
    pygame.draw.rect(button, (138, 43, 226), button.get_rect())  # Draw on it.
    screen.blit(button, (300, 300))

    text = font16.render("Game Over!", True, (127, 255, 212), (138, 43, 226))
    screen.blit(text, (305, 315))


def conBut4():
    button = pygame.Surface((100, 40))  # Create a Surface to draw on.
    button.fill((255, 255, 255))
    pygame.draw.rect(button, (138, 43, 226), button.get_rect())  # Draw on it.
    screen.blit(button, (300, 350))

    text = font16.render("Try Again?", True, (127, 255, 212), (138, 43, 226))
    screen.blit(text, (305, 365))


class Player(pygame.sprite.Sprite):
    def __init__(self, PlayerX, PlayerY):
        super().__init__()
        self.image = battle64
        self.PlayerX = PlayerX
        self.PlayerY = PlayerY
        self.rect = self.image.get_rect(center=(self.PlayerX+30, self.PlayerY+20))

    def update(self):
        self.PlayerX = PlayerX
        self.PlayerY = PlayerY
        self.rect.center = (self.PlayerX, self.PlayerY)

    def shoot(self):
        return Bullet(self.rect[0], self.rect[1])


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = bullet64
        self.rect = self.image.get_rect(center=(pos_x+30, pos_y+20))

    def update(self):
        self.rect.y -= 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self, EnemyX, EnemyY):
        super().__init__()
        self.switch = False
        self.image = enemy64
        self.EnemyX = EnemyX
        self.EnemyY = EnemyY
        self.rect = self.image.get_rect(center=(self.EnemyX, self.EnemyY))

    def update(self):
        if self.EnemyX > 600:
            self.EnemyY += 40
            self.switch = True
        elif self.EnemyX < 80:
            self.EnemyY += 40
            self.switch = False

        if self.switch:
            self.EnemyX = self.EnemyX - 0.3
        else:
            self.EnemyX = self.EnemyX + 0.3

        self.rect.center = (self.EnemyX, self.EnemyY)


enemy = Enemy(EnemyX, EnemyY)
playerGroup = pygame.sprite.Group()

enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
enemyGroup.add(enemy)


flagL, flagR, flagU, flagD = [False, False, False, False]
counter = 0
done = True
sClick = False
speed = 0.7
shotActive = False
points = 0
spawnCounter = 0
lives = 3
gameStart = True
gameOver = False
while done:
    mouseX, mouseY = pygame.mouse.get_pos()
    if gameStart and lives > 0:
        PlayerX = 600
        PlayerY = 600
        player = Player(PlayerX, PlayerY)
        playerGroup.add(player)
        gameStart = False

    counter += 1
    spawnCounter += 1
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 <= mouseX <= 400 and 350 <= mouseY <= 390 and gameOver:
                lives = 3
                gameStart = True
                points = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            flagL = True
        else:
            flagL = False

        if keys[pygame.K_RIGHT]:
            flagR = True
        else:
            flagR = False

        if keys[pygame.K_UP]:
            flagU = True
        else:
            flagU = False

        if keys[pygame.K_DOWN]:
            flagD = True
        else:
            flagD = False

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            sClick = True
        else:
            sClick = False

        if keys[pygame.K_z]:
            shotActive = True
        else:
            shotActive = False

        if event.type == pygame.QUIT:
            done = False

    if sClick:
        speed = 0.3
    else:
        speed = 0.8

    if counter > 100 and shotActive:
        bulletGroup.add(player.shoot())
        counter = 0

    if spawnCounter % 200 == 0 and lives > 0:
        enemyGroup.add(Enemy(EnemyX, EnemyY))

    if flagL:
        if PlayerX < 40:
            PlayerX = 41
        else:
            PlayerX -= speed

    if flagR:
        if PlayerX > 600:
            PlayerX = 599
        else:
            PlayerX += speed

    if flagU:
        if PlayerY < 0:
            PlayerY = 1
        else:
            PlayerY -= speed

    if flagD:
        if PlayerY > 631:
            PlayerY = 630
        else:
            PlayerY += speed

    conBut(points)
    conBut2(lives)
    if pygame.sprite.groupcollide(bulletGroup, enemyGroup, True, True):
        points += 1
    if pygame.sprite.groupcollide(playerGroup, enemyGroup, True, False):
        enemyGroup.empty()
        lives -= 1
        gameStart = True
        pygame.time.delay(1000)
    enemyGroup.draw(screen)
    playerGroup.draw(screen)
    bulletGroup.draw(screen)
    playerGroup.update()
    bulletGroup.update()
    enemyGroup.update()
    if lives == 0:
        gameOver = True
        conBut3()
        conBut4()

    pygame.display.flip()
    pygame.display.update()
