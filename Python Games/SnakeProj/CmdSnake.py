import random

sn = [[0, 0], [0, 1], [0, 2]]
s = 5
arr = []


def spawnApple():
    randX = random.randint(0, s-1)
    randY = random.randint(0, s-1)
    apple = [randY, randX]
    while apple in sn:
        randX = random.randint(0, s - 1)
        randY = random.randint(0, s - 1)
        apple = [randY, randX]
    return apple


apple = spawnApple()


def move(dir, list, apple=False):
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
            return list
        for j in cl:
            if i == j:
                count += 1

        if count == 2:
            print("You crashed into yourself!")
            return list
    return cl

"""
for i in range(s):
    temp = []
    for j in range(s):
        temp.append(0)
    arr.append(temp)
"""


def gridView(snake, apple):
    for i in range(s):
        for j in range(s):
            if [i, j] in snake:
                if [i, j] == snake[-1]:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            elif [i, j] == apple:
                print("X", end=" ")
            else:
                print("-", end=" ")
        print()
    return arr


def action(dir, sn, apple):
    test = False
    [x, y] = apple
    while apple in sn:
        apple = spawnApple()
        test = True
    print("+++++")
    sn = move(dir, sn, apple=test)
    gridView(sn, apple)
    # print(sn)
    return sn, apple


gridView(sn, apple)

cancel = False
while not cancel:
    dir = input("Direction: ")
    if dir == "e":
        cancel = True
    else:
        sn, apple = action(dir, sn, apple)
