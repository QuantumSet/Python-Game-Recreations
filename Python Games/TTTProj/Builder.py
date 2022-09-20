import random


class GameBuilder:
    def __init__(self):
        self.map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.active = True

    def move(self, x, y, player=True):
        if self.active:
            if x > 3 or y > 3 or x < 1 or y < 1:
                print("Those numbers are outside the range!")
            elif self.map[y-1][x-1] > 0:
                print("Someone has already used that location!")
            elif player:
                self.map[y-1][x-1] = 1
                self.view()
            else:
                self.map[y-1][x-1] = 2
                self.view()
            if self.checkOutcome():
                self.active = False

    def AImove(self):
        rX = random.randint(1, 3)
        rY = random.randint(1, 3)
        while self.map[rY-1][rX-1] != 0:
            rX = random.randint(1, 3)
            rY = random.randint(1, 3)
        self.move(rX, rY, player=False)

    def view(self):
        for i in self.map:
            for j in i:
                j = str(j)
                if j == "0":
                    print("-", end=" ")
                elif j == "1":
                    print("O", end=" ")
                elif j == "2":
                    print("X", end=" ")
            print("")
        print("======")

    def checkOutcome(self):
        count = 0
        for i in range(len(self.map)):
            if self.map[0][i] == self.map[1][i] == self.map[2][i] == 1:
                print("You won!")
                return True
            elif self.map[0][i] == self.map[1][i] == self.map[2][i] == 2:
                print("The computer won!")
                return True
        for i in range(len(self.map[0])):
            if self.map[i][0] == self.map[i][1] == self.map[i][2] == 1:
                print("You won!")
                return True
            elif self.map[i][0] == self.map[i][1] == self.map[i][2] == 2:
                print("The computer won!")
                return True

        for i in range(len(self.map)):
            if self.map[0][0] == self.map[1][1] == self.map[2][2] == 1:
                print("You won!")
                return True
            elif self.map[2][0] == self.map[1][1] == self.map[0][2] == 1:
                print("You won!")
                return True
            if self.map[0][0] == self.map[1][1] == self.map[2][2] == 2:
                print("The computer won!")
                return True
            elif self.map[2][0] == self.map[1][1] == self.map[0][2] == 2:
                print("The computer won!")
                return True

        for i in self.map:
            for j in i:
                if j > 0:
                    count += 1
        if count == 9:
            print("There are no more additional spaces! It's a draw!")
            return True

        return False


TTT = GameBuilder()
TTT.move(1, 1)
TTT.move(1, 2)
TTT.move(1, 3, player=False)
TTT.AImove()



