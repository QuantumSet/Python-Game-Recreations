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


def gridDisplay(grid):
    for k in range(len(grid)):
        str1 = ""
        for j in range(len(grid[k])):
            str1 = str1 + str(grid[k][j]) + " "

        print(str1)


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


def simulateInf(grid):
    file = open("PathZ.txt", "w")
    morb = random.randint(1, 2)
    if morb:
        x1 = True
    else:
        x1 = False

    obj = Morbius(x1, grid, [0, 1])
    for i in range(7):
        randomMove(obj)
        file.write(str(obj.pos[0]) + " " + str(obj.pos[1]) + "\n")
        #print(obj.pos)

    #print("----")
    file.close()
    return obj


def simulate(grid, rep):
    for i in range(rep):
        morb = random.randint(1, 2)
        if morb:
            x1 = True
        else:
            x1 = False

        obj = Morbius(x1, grid, [0, 1])
        for k in range(5):
            randomMove(obj)
            print(obj.pos)

        print(obj.points)


print("Bro...💀")
print("--------")
arr = [1, 0, 1, 0]
alr = [0, 1, 0, 1]
mapo = [arr, alr, arr, alr]

gridDisplay(mapo)
print("--------")

# simulate(mapo, 5)

s = simulateInf(mapo)
x = s.points
while x != 4:
    s = simulateInf(mapo)
    x = s.points

print(s.pos)
print(x)
