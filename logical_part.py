import random
import Enum

"""

"""
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Coordinates:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Entrails:

    def __init__(self):
        self.grid = [0 for i in range(4) for i in range(4)]
        self.dirLine = [1, 0, -1, 0]
        self.dirColumn = [0, 1, 0, -1]

    def get_Unnocuppied_Position(self) -> Coordinates:
        isOccupied = True
        while isOccupied:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.grid[x][y] == 0:
                isOccupied = False
        return Coordinates(x, y)

    def addAnotherPiece(self):
        cellForTwo: Coordinates = self.getUnoccupiedPosition()
        if random.randint(0, 1000) % 3 == 0:
            self.grid[cellForTwo.x][cellForTwo.y] = 2
        else:
            self.grid[cellForTwo.x][cellForTwo.y] = 4

    def moveIsPossible(self, line, column, nextLine, nextColumn):
        if nextLine < 0 or nextColumn < 0 or nextLine >= 4 or nextColumn >= 4 or grid[line][column] != grid[nextLine][nextColumn] and grid[nextLine][nextColumn] != 0:
            return False
        else:
            return True

    def move(self, direction: Direction):
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
        moveWasMade = True
        canAddPiece = False
        while (moveWasMade):
            moveWasMade = False
            for i in range(startLine, endLine, lineStep):
                for j in range(startColumnn, endColumn, columnStep):
                    nextLine = i + dirLine[direction]
                    nextColumn = j + dirColumn[direction]
                    if (self.grid[i][j] != 0 and self.moveIsPossible(i, j, nextLine, nextColumn)):
                        self.grid[nextLine][nextColumn] += self.grid[i][j]
                        self.grid[i][j] = 0
                        moveWasMade = True
                        canAddPiece = True
        if canAddPiece:
            addAnotherPiece()

    def gameInterface(self):
        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                if (self.grid[i][j] == 0):
                    print("{     }  ")
                elif (self.grid[i][j] < 10):
                    print("{    ", self.grid[i][j], "}  ")
                elif (self.grid[i][j] < 100):
                    print("{   ", self.grid[i][j], "}  ")
                elif (self.grid[i][j] < 1000):
                    print("{  ", self.grid[i][j], "}  ")
                elif (self.grid[i][j] < 10000):
                    print("{ ", self.grid[i][j], "}  ")
            print(" ")
        print("n - new game, a - left, w - up, d - right, s - down, q - quit")

    def newGame(self):
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = 0
        self.addAnotherPiece()
        self.addAnotherPiece()

    def startGame(self):
        commands = {
            "s": Direction.DOWN
            # ...
        }
        isNotOver = True
        while isNotOver:
            self.gameInterface()
            choice = input()
            if choice == 'n':
                self.newGame()
            else:
                if choice in commands:
                    self.move(direction=commands[choice])
                else:
                    print("Unknown command")
        print("End of the game!")
