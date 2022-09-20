import random

import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Tic-Tac-Toe")
size = (500, 500)
arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
bgColor = pygame.Color(245, 244, 116)
img1 = pygame.image.load("radiation.png")
pygame.display.set_icon(img1)
imgOS = img1
img1 = pygame.transform.scale(img1, (100, 100))

img2 = pygame.image.load("cross.png")
imgXS = img2
img2 = pygame.transform.scale(img2, (100, 100))

font16 = pygame.font.Font('freesansbold.ttf', 16)
turn = 0
counter = 0

def grid(array):
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

    for i in range(n-1):
        screen.blit(rect_line, (v, 0))
        v += w

    for j in range(m-1):
        screen.blit(rect_hor, (0, r))
        r += z


def placeO(PosX, PosY):
    screen.blit(img1, (PosX, PosY))


def placeX(PosX, PosY):
    screen.blit(img2, (PosX, PosY))


def checkOutcome(orig):
    count = 0
    for i in range(len(arr)):
        if arr[0][i] == arr[1][i] == arr[2][i] == 1:
            return 2
        elif arr[0][i] == arr[1][i] == arr[2][i] == 2:
            return 3
    for i in range(len(arr[0])):
        if arr[i][0] == arr[i][1] == arr[i][2] == 1:
            return 2
        elif arr[i][0] == arr[i][1] == arr[i][2] == 2:
            return 3
    for i in range(len(arr)):
        if arr[0][0] == arr[1][1] == arr[2][2] == 1:
            return 2
        elif arr[2][0] == arr[1][1] == arr[0][2] == 1:
            return 2
        if arr[0][0] == arr[1][1] == arr[2][2] == 2:
            return 3
        elif arr[2][0] == arr[1][1] == arr[0][2] == 2:
            return 3

    for n in arr:
        for m in n:
            if m > 0:
                count += 1
    if count == 9:
        return 4
    else:
        return orig


def resetBut():
    button = pygame.Surface((120, 40))  # Create a Surface to draw on.
    button.fill(bgColor)
    pygame.draw.rect(button, (138, 43, 226), button.get_rect())  # Draw on it.
    screen.blit(button, (550, 350))

    text1 = font16.render("Reset Game", True, (127, 255, 212), (138, 43, 226))
    screen.blit(text1, (562, 363))


def Com(counter):
    if counter == 0:
        xrand = random.randint(0, 1) * 2
        yrand = random.randint(0, 1) * 2
        arr[xrand][yrand] = 1


done = True
while done:
    screen.fill(bgColor)
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 550 <= mouseX <= 670 and 350 <= mouseY <= 390:
                arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                turn = 0
                Com(counter)

            if 0 <= mouseX <= 160 and 0 <= mouseY <= 160 and arr[0][0] == 0 and turn < 2:
                if turn == 0:
                    arr[0][0] = 1
                    turn = 1
                else:
                    arr[0][0] = 2
                    turn = 0
            elif 170 <= mouseX <= 330 and 0 <= mouseY <= 160 and arr[1][0] == 0 and turn < 2:
                if turn == 0:
                    arr[1][0] = 1
                    turn = 1
                else:
                    arr[1][0] = 2
                    turn = 0
            elif 340 <= mouseX <= 490 and 0 <= mouseY <= 160 and arr[2][0] == 0 and turn < 2:
                if turn == 0:
                    arr[2][0] = 1
                    turn = 1
                else:
                    arr[2][0] = 2
                    turn = 0
            elif 0 <= mouseX <= 160 and 170 <= mouseY <= 330 and arr[0][1] == 0 and turn < 2:
                if turn == 0:
                    arr[0][1] = 1
                    turn = 1
                else:
                    arr[0][1] = 2
                    turn = 0
            elif 170 <= mouseX <= 330 and 170 <= mouseY <= 330 and arr[1][1] == 0 and turn < 2:
                if turn == 0:
                    arr[1][1] = 1
                    turn = 1
                else:
                    arr[1][1] = 2
                    turn = 0
            elif 340 <= mouseX <= 490 and 170 <= mouseY <= 330 and arr[2][1] == 0 and turn < 2:
                if turn == 0:
                    arr[2][1] = 1
                    turn = 1
                else:
                    arr[2][1] = 2
                    turn = 0
            elif 0 <= mouseX <= 160 and 340 <= mouseY <= 490 and arr[0][2] == 0 and turn < 2:
                if turn == 0:
                    arr[0][2] = 1
                    turn = 1
                else:
                    arr[0][2] = 2
                    turn = 0
            elif 170 <= mouseX <= 330 and 340 <= mouseY <= 490 and arr[1][2] == 0 and turn < 2:
                if turn == 0:
                    arr[1][2] = 1
                    turn = 1
                else:
                    arr[1][2] = 2
                    turn = 0
            elif 340 <= mouseX <= 490 and 340 <= mouseY <= 490 and arr[2][2] == 0 and turn < 2:
                if turn == 0:
                    arr[2][2] = 1
                    turn = 1
                else:
                    arr[2][2] = 2
                    turn = 0

        if event.type == pygame.QUIT:
            done = False

    grid(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            pointX = i * (500 / 3) + 40
            pointY = j * (500 / 3) + 40
            if arr[i][j] == 0:
                continue
            elif arr[i][j] == 1:
                placeO(pointX, pointY)
            elif arr[i][j] == 2:
                placeX(pointX, pointY)

    turn = checkOutcome(turn)

    if turn == 0:
        text = font16.render("Player 2 Turn!", True, (127, 255, 212), (138, 43, 226))
        screen.blit(text, (562, 83))
        screen.blit(imgOS, (520, 75))
    elif turn == 1:
        text = font16.render("Player 1 Turn!", True, (138, 43, 226), (127, 255, 212))
        screen.blit(text, (562, 83))
        screen.blit(imgXS, (520, 75))
    elif turn == 2:
        text = font16.render("Player 2 WIN!", True, (127, 255, 212), (138, 43, 226))
        screen.blit(text, (562, 83))
        screen.blit(imgOS, (520, 75))
    elif turn == 3:
        text = font16.render("Player 1 WIN!", True, (138, 43, 226), (127, 255, 212))
        screen.blit(text, (562, 83))
        screen.blit(imgXS, (520, 75))
    elif turn == 4:
        text = font16.render("It's a draw!", True, (138, 43, 226), (127, 255, 212))
        screen.blit(text, (562, 83))



    resetBut()
    pygame.display.flip()
    pygame.display.update()
