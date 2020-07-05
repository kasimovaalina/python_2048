import random

class Coordinates:

    def Coordinates(self, x_, y_):
        self.x = x_
        self.y = y_


class Entrails:

    def Entrails(self):
        self.gamePole = [[0]*4]*4
        self.dirLine = [1, 0, -1, 0]
        self.dirColumn = [0, 1, 0, -1]
    def getUnnocuppiedPosition(self)
        bool isOccupied = True
        while isOccupied:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.gamePole[x][y] == 0:
                isOccupied = False
        return Coordinates(x,y)


    def addAnotherPiece(self)
        Coordinates cellForTwo = self.getUnoccupiedPosition()
        randomNumber = random.randint(0, 1000)
        if randomNumber % 3 != 0: 
            self.gamePole[cellForTwo.x][cellForTwo.y] = 2
        else 
            self.gamePole[cellForTwo.x][cellForTwo.y] = 4

    def moveIsPossible(self, line, column, nextLine, nextColumn)
        if (nextLine < 0) or (nextColumn < 0) or (nextLine >= 4) or (nextColumn >= 4) or (gamePole[line][column] != gamePole[nextLine][nextColumn] and gamePole[nextLine][nextColumn] != 0):
            return false
        else 
            return true
    

    def move(self, int direction):
        startLine = 0
        startColumn = 0
        endLine = 3
        endColumn = 3  
        lineStep = 1
        columnStep = 1
        if (direction == 0):
            startLine = 3
            endLine = 0
            lineStep = -1
        if (direction == 1):
            startColumn = 3
            endLine = 0
            columnStep = -1
        bool moveWasMade = True
        bool canAddPiece
        while (moveWasMade):
            moveWasMade = False
            for i in range(startLine, endLine, lineStep):
                for j in range(startColumnn, endColumn, columnStep):
                    nextLine = i + dirLine[direction]
                    nextColumn = j + dirColumn[direction]
                    if (self.gamePole[i][j] != 0 and moveIsPossible(i,j,nextLine,nextColumn)):
                        self.gamePole[nextLine][nextColumn] += self.gamePole[i][j]
                        self.gamePole[i][j] = 0
                        moveWasMade = true
                        canAddPiece = true
        if (canAddPiece)
        addAnotherPiece()

    def gameInterface(self):
        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                if (self.gamePole[i][j] == 0):
                    print("{     }  ") 
                elif (self.gamePole[i][j] < 10):
                    print("{    ", self.gamePole[i][j], "}  ")
                elif (self.gamePole[i][j] < 100):
                    print("{   " self.gamePole[i][j], "}  ")
                elif (self.gamePole[i][j] < 1000):
                    print("{  ", self.gamePole[i][j], "}  ")
                elif (self.gamePole[i][j] < 10000):
                    print("{ ", self.gamePole[i][j], "}  ")
            print(" ")
  print("n - new game, a - left, w - up, d - right, s - down, q - quit)
}