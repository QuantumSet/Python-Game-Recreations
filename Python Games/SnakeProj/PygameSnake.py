import random
import pygame

pygame.init()
screen = pygame.display.set_mode((700, 510))
pygame.display.set_caption("Snake")
pyLogo = pygame.image.load("python.png")
pygame.display.set_icon(pyLogo)
bgColor = pygame.Color(255, 182, 193)
s = 5
snHead = pygame.image.load("boxing.png")
snHeadF = pygame.image.load("boxing.png")
snBody = pygame.image.load("latency.png")
appleImg = pygame.image.load("coin.png")
font32 = pygame.font.Font('freesansbold.ttf', 32)
font16 = pygame.font.Font('freesansbold.ttf', 16)

inc = 100

currentDir = ""

sn = [[0, 0]]
body = sn[1:]


def drawBorder():
    rect_border = pygame.Surface((510, 510))  # Create a Surface to draw on.
    rect_border.fill(bgColor)
    pygame.draw.rect(rect_border, (127, 255, 212), rect_border.get_rect(), 10)  # Draw on it.
    screen.blit(rect_border, (0, 0))


def grid():
    s = (10, 500)
    p = (500, 10)
    x, y = (500, 500)
    n = 5
    m = 5

    v = x / n
    w = x / n

    r = y / m
    z = y / m

    rect_line = pygame.Surface(s)
    pygame.draw.rect(rect_line, (127, 255, 212), rect_line.get_rect())
    rect_hor = pygame.Surface(p)
    pygame.draw.rect(rect_hor, (127, 255, 212), rect_hor.get_rect())

    for i in range(n-1):
        screen.blit(rect_line, (v, 0))
        v += w

    for j in range(m-1):
        screen.blit(rect_hor, (0, r))
        r += z


def spawnApple():
    randX = random.randint(0, s - 1)
    randY = random.randint(0, s - 1)
    apple = [randY, randX]
    while apple in sn:
        randX = random.randint(0, s - 1)
        randY = random.randint(0, s - 1)
        apple = [randY, randX]
    return apple


def conBut():
    button = pygame.Surface((100, 40))  # Create a Surface to draw on.
    button.fill(bgColor)
    pygame.draw.rect(button, (138, 43, 226), button.get_rect())  # Draw on it.
    screen.blit(button, (550, 350))

    text = font16.render("Try Again?", True, (127, 255, 212), (138, 43, 226))
    screen.blit(text, (562, 363))


def moveS(dir, list, apple=False):
    gameOver = False
    cl = []
    if not apple:
        for i in range(1, len(list)):
            cl.append(list[i])
    else:
        for i in range(len(list)):
            cl.append(list[i])

    x, y = list[-1]

    if dir == "u":
        x -= 1
    elif dir == "d":
        x += 1
    elif dir == "r":
        y += 1
    elif dir == "l":
        y -= 1

    cl.append([x, y])

    for i in cl:
        count = 0
        x, y = i
        if x < 0 or x > s-1 or y < 0 or y > s-1:
            print("That was outside the parameters!")
            gameOver = True
            return list, gameOver
        for j in cl:
            if i == j:
                count += 1

        if count == 2:
            print("You crashed into yourself!")
            gameOver = True
            return list, gameOver
    return cl, gameOver


apple = spawnApple()
apTest = False
tick = 0
done = True
gameOver = False
while done:
    body = sn[1:]
    tick += 1
    screen.fill(bgColor)
    mouseX, mouseY = pygame.mouse.get_pos()
    move = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 550 <= mouseX <= 650 and 350 <= mouseY <= 390 and gameOver:
                sn = [[0, 0]]
                currentDir = ""
                gameOver = False

        if event.type == pygame.KEYDOWN and not gameOver:
            if event.key == pygame.K_RIGHT:
                snHeadF = snHead
                
                currentDir = "r"
                move = True
                sn, gameOver = moveS(currentDir, sn, apple=apTest)
            elif event.key == pygame.K_LEFT:
                snHeadF = pygame.transform.rotate(snHead, 180)
                
                currentDir = "l"
                move = True
                sn, gameOver = moveS(currentDir, sn, apple=apTest)
            if event.key == pygame.K_UP:
                snHeadF = pygame.transform.rotate(snHead, 90)
                
                currentDir = "u"
                move = True
                sn, gameOver = moveS(currentDir, sn, apple=apTest)
            elif event.key == pygame.K_DOWN:
                snHeadF = pygame.transform.rotate(snHead, 270)
                
                currentDir = "d"
                move = True
                sn, gameOver = moveS(currentDir, sn, apple=apTest)
            tick = 0
            apTest = False

        if event.type == pygame.QUIT:
            done = False

    if not move and tick == 300 and not gameOver:
        tick = 0
        if currentDir == "r":
            snHeadF = snHead
            
            sn, gameOver = moveS(currentDir, sn, apple=apTest)
        elif currentDir == "l":
            snHeadF = pygame.transform.rotate(snHead, 180)
            
            sn, gameOver = moveS(currentDir, sn, apple=apTest)
        elif currentDir == "u":
            snHeadF = pygame.transform.rotate(snHead, 90)
            sn, gameOver = moveS(currentDir, sn, apple=apTest)
        elif currentDir == "d":
            snHeadF = pygame.transform.rotate(snHead, 270)
            sn, gameOver = moveS(currentDir, sn, apple=apTest)
        apTest = False

    drawBorder()
    grid()
    x, y = apple
    if apple in sn:
        apple = spawnApple()
        apTest = True
        print(body)
    screen.blit(appleImg, (y * 100 + 25, x * 100+25))
    for i in sn:
        x = ((i[0]) * (500 / 5)) + 25
        y = ((i[1]) * (500 / 5)) + 25
        if i == sn[-1]:
            screen.blit(snHeadF, (y, x))
        else:
            screen.blit(snBody, (y, x))

    if gameOver:
        text = font16.render("Game Over!", True, (0, 0, 128), bgColor)
        screen.blit(text, (562, 83))
        text2 = font16.render("You won " + str(len(sn[1:])) + " points!", True, (0, 0, 128), bgColor)
        screen.blit(text2, (542, 123))

        conBut()

    pygame.display.flip()
    pygame.display.update()
