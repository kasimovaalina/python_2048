import random
import enum

"""
Поле игры представляет из себя двумерный массив размерностью 4x4.
Массив видоизменяется каждый раз, когда программа обращается к методу move в соответсвии
"""
class Direction(enum.Enum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3

change_vector = {
    Direction.UP: (-1, 0),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1),
    Direction.RIGHT: (0, 1)
}

class Coordinates:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Entrails:
    direct_line = [1, 0, -1, 0]
    direct_column = [0, 1, 0, -1]

    def __init__(self):
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def get_unnocuppied_position(self) -> Coordinates:
        is_occupied = True
        while is_occupied:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.grid[x][y] == 0:
                is_occupied = False
        return Coordinates(x, y)

    def add_piece(self):
        free_cell: Coordinates = self.get_unnocuppied_position()
        if random.randint(0, 1000) % 53 == 0:
            self.grid[free_cell.x][free_cell.y] = 4
        else:
            self.grid[free_cell.x][free_cell.y] = 2

    def is_cell_in_grid(self, next_line: int, next_column: int):
        if next_line >= 0 and next_column >= 0 and next_line < 4 and next_column < 4:
            return True
        return False

    def is_same_cell(self, line: int, column: int, next_line: int, next_column: int):
        if self.grid[line][column] != self.grid[next_line][next_column]:
            return False
        return True

    def is_move_possible(self, line: int, column: int, next_line: int, next_column: int):
        if not self.is_cell_in_grid(next_line, next_column):
            return False
        elif self.grid[line][column] != self.grid[next_line][next_column] and self.grid[next_line][next_column] != 0:
            return False
        else:
            return True

    def is_2048_in_grid(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 2048:
                    return True
        return False

    def move(self, direction):
        start_line = 0
        start_column = 0
        line_step = 1
        column_step = 1
        if direction is Direction.DOWN:
            start_line = 3
            line_step = -1
        if direction is Direction.RIGHT:
            start_column = 3
            column_step = -1
        move_was_made = True
        can_add_piece = False
        while (move_was_made):
            move_was_made = False
            i = start_line
            while i >= 0 and i < 4:
                j = start_column
                while j >= 0 and j < 4:
                    line_offset, column_offset = change_vector[direction]
                    next_line = i + line_offset
                    next_column = j + column_offset
                    if (self.grid[i][j] != 0 and self.is_move_possible(i, j, next_line, next_column)):
                        self.grid[next_line][next_column] += self.grid[i][j]
                        self.grid[i][j] = 0
                        move_was_made = True
                        can_add_piece = True
                    j += column_step
                i += line_step
        if can_add_piece:
            self.add_piece()

    def create_newgame(self):
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = 0
        self.add_piece()
        self.add_piece()
