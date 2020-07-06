import random
import Enum

"""

"""
class Direction(Enum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3


class Coordinates:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Entrails:

    def __init__(self):
        self.grid = [0 for i in range(4) for i in range(4)]
        self.dirLine = [1, 0, -1, 0]
        self.dirColumn = [0, 1, 0, -1]

    def get_unnocuppied_position(self) -> Coordinates:
        isOccupied = True
        while isOccupied:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.grid[x][y] == 0:
                isOccupied = False
        return Coordinates(x, y)

    def add_piece(self):
        cellForTwo: Coordinates = self.getUnoccupiedPosition()
        if random.randint(0, 1000) % 3 == 0:
            self.grid[cellForTwo.x][cellForTwo.y] = 2
        else:
            self.grid[cellForTwo.x][cellForTwo.y] = 4

    def cell_in_grid(self, nextLine: int, nextColumn: int):
        if nextLine < 0 or nextColumn < 0 or nextLine >= 4 or nextColumn >= 4:
            return False
        return True

    def same_cell(self, line: int, column: int, nextLine: int, nextColumn: int):
        if self.grid[line][column] != self.grid[nextLine][nextColumn]:
            return False
        return True

    def move_is_possible(self, line: int, column: int, nextLine: int, nextColumn: int):
        if not self.cell_in_grid(nextLine, nextColumn):
            if self.grid[line][column] != self.grid[nextLine][nextColumn] and self.grid[nextLine][nextColumn] != 0:
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
                for j in range(startColumn, endColumn, columnStep):
                    nextLine = i + self.dirLine[direction]
                    nextColumn = j + self.dirColumn[direction]
                    if (self.grid[i][j] != 0 and self.moveIsPossible(i, j, nextLine, nextColumn)):
                        self.grid[nextLine][nextColumn] += self.grid[i][j]
                        self.grid[i][j] = 0
                        moveWasMade = True
                        canAddPiece = True
        if canAddPiece:
            self.add_piece()

    def show(self):
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

    def restart(self):
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = 0
        self.add_piece()
        self.add_piece()

    def start(self):
        commands = {'s': Direction.DOWN, 'd': Direction.RIGHT, 'w': Direction.UP, 'a': Direction.LEFT}
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
