import pygame
import random


class Morbius:
    def __init__(self, morb, grid, pos):
        if morb:
            self.morbin = "It's morbin time"
        else:
            self.morbin = "To bats it's deadly..."

        self.grid = grid
        self.pos = pos
        self.location = self.grid[self.pos[0]][self.pos[1]]
        self.points = 0

    def moveV(self, amt):
        if amt:
            self.pos[0] += 1
        else:
            self.pos[0] -= 1
        if self.pos[0] < 0:
            self.pos[0] = len(self.grid) + self.pos[0]
        elif self.pos[0] >= len(self.grid):
            self.pos[0] = self.pos[0] - len(self.grid)

        self.location = self.grid[self.pos[0]][self.pos[1]]
        if self.location == 1:
            self.points += self.location

    def moveH(self, amt):
        if amt:
            self.pos[1] += 1
        else:
            self.pos[1] -= 1
        if self.pos[1] < 0:
            self.pos[1] = len(self.grid[0]) + self.pos[1]
        elif self.pos[1] >= len(self.grid[0]):
            self.pos[1] = self.pos[1] - len(self.grid[0])

        self.location = self.grid[self.pos[0]][self.pos[1]]
        if self.location == 1:
            self.points += self.location


pygame.init()
screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("#MORBIUSSWEEP")
icon = pygame.image.load("bro.png")
pygame.display.set_icon(icon)
playerImg = pygame.image.load("aya.png")
playerX = 10
playerY = 460

bgColor = pygame.Color(123, 234, 111)
arr = [0, 1, 0, 1]
alr = [1, 0, 1, 0]
fin = [arr, alr, arr]

font32 = pygame.font.Font('freesansbold.ttf', 32)
font16 = pygame.font.Font('freesansbold.ttf', 16)
move_txt = ''
point_txt = ''


def player(X, Y):
    screen.blit(playerImg, (X, Y))


def randomMove(object1):
    move = random.randint(0, 3)
    if move == 0:
        object1.moveV(True)
    elif move == 1:
        object1.moveV(False)
    elif move == 2:
        object1.moveH(True)
    elif move == 3:
        object1.moveH(False)
    else:
        print("It was lethal...")


size = (500, 500)


def drawBorder():
    rect_border = pygame.Surface(size)  # Create a Surface to draw on.
    rect_border.fill(bgColor)
    pygame.draw.rect(rect_border, (127, 255, 212), rect_border.get_rect(), 10)  # Draw on it.
    screen.blit(rect_border, (0, 0))


def drawGrid(array):
    s = (10, 500)
    p = (500, 10)
    x, y = size
    n = len(array[0])
    m = len(array)

    v = x / n
    w = x / n

    r = y / m
    z = y / m

    rect_line = pygame.Surface(s)
    pygame.draw.rect(rect_line, (127, 255, 212), rect_line.get_rect())
    rect_hor = pygame.Surface(p)
    pygame.draw.rect(rect_hor, (127, 255, 212), rect_hor.get_rect())

    tempX = v/2
    tempY = r/2

    for i in range(n-1):
        screen.blit(rect_line, (v, 0))
        v += w

    for j in range(m-1):
        screen.blit(rect_hor, (0, r))
        r += z

    for k in array:
        for item in k:
            text = font32.render(str(item), True, (0, 0, 128), bgColor)
            screen.blit(text, (tempX, tempY))
            tempX += w
        tempY += z
        tempX = (x/n)/2


def calculate(array, start):

    arr = []

    activateSim(int(point_txt), array, int(move_txt), start)

    f = open("PathZ.txt", "r")
    f1 = f.readlines()
    for i in f1:
        temp = [int(i[0]), int(i[2])]
        arr.append(temp)
    print(arr)

    f.close()
    return arr


def simulateInf(grid, moves, start):
    file = open("PathZ.txt", "w")
    morb = random.randint(1, 2)
    if morb:
        x1 = True
    else:
        x1 = False

    obj = Morbius(x1, grid, start)
    for i in range(moves):
        randomMove(obj)
        file.write(str(obj.pos[1]) + " " + str(obj.pos[0]) + "\n")
        #print(obj.pos)

    #print("----")
    file.close()
    return obj


def activateSim(points, grid, moves, start):
    s = simulateInf(grid, moves, start)
    x = s.points
    while x != points:
        s = simulateInf(grid, moves, start)
        x = s.points


def conBut():
    button = pygame.Surface((100, 40))  # Create a Surface to draw on.
    button.fill(bgColor)
    pygame.draw.rect(button, (138, 43, 226), button.get_rect())  # Draw on it.
    screen.blit(button, (550, 350))

    text = font16.render("Calculate", True, (127, 255, 212), (138, 43, 226))
    screen.blit(text, (562, 363))


def moveBut():
    text = font16.render("Moves:", True, (138, 43, 226), bgColor)
    screen.blit(text, (550, 100))


def pointBut():
    text = font16.render("Points:", True, (138, 43, 226), bgColor)
    screen.blit(text, (550, 200))


input_move = pygame.Rect(610, 95, 20, 25)
input_point = pygame.Rect(610, 195, 20, 25)

color_active = pygame.Color('lightskyblue3')

color_passive = pygame.Color('chartreuse4')
color = color_passive
color1 = color_passive

active = False
active1 = False
done = True
switch = True
while done:
    n = len(fin[0])
    m = len(fin)
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill(bgColor)
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_move.collidepoint(event.pos):
                active = True
            else:
                active = False

            if input_point.collidepoint(event.pos):
                active1 = True
            else:
                active1 = False
            if 550 <= mouseX <= 650 and 350 <= mouseY <= 390:
                start = [0, 0]
                s = [0, 0]
                arr = calculate(fin, start)

                arr.insert(0, s)
                print(arr)

                for i in arr:
                    drawBorder()
                    drawGrid(fin)
                    playerX = ((i[0] + 1) * (500 / n)) - 40
                    playerY = (i[1] + 1) * (500 / m) - 40
                    player(playerX, playerY)
                    pygame.display.update()
                    pygame.time.delay(1000)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and active:
                move_txt = move_txt[:-1]
            elif active:
                move_txt += event.unicode

            if event.key == pygame.K_BACKSPACE and active1:
                point_txt = point_txt[:-1]
            elif active1:
                point_txt += event.unicode
        if event.type == pygame.QUIT:
            done = False

    if active:
        color = color_active
    else:
        color = color_passive
    if active1:
        color1 = color_active
    else:
        color1 = color_passive

    # Background Information
    drawBorder()
    drawGrid(fin)
    conBut()
    moveBut()
    pointBut()

    pygame.draw.rect(screen, color, input_move)
    pygame.draw.rect(screen, color1, input_point)

    text_surface = font16.render(move_txt, True, (255, 255, 255))
    text_point = font16.render(point_txt, True, (255, 255, 255))

    screen.blit(text_surface, (input_move.x + 5, input_move.y + 5))
    screen.blit(text_point, (input_point.x + 5, input_point.y + 5))

    input_move.w = max(20, text_surface.get_width() + 10)
    input_point.w = max(20, text_point.get_width() + 10)

    # Just a pass time

    player(playerX, playerY)
    # if switch:
    #     playerX += 0.1
    # else:
    #     playerX -= 0.1
    # if playerX >= 460:
    #     switch = False
    # elif playerX <= 10:
    #     switch = True

    # Finishing touches
    pygame.display.flip()
    pygame.display.update()


