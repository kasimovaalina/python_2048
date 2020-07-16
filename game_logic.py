import random
import enum

"""
Поле игры представляет из себя двумерный массив размерностью 4x4.
Изначально все элементы массива равны нулю. Если ячейка массива равна нулю, значит, она пустая,
и не отобразится на экране. За заполнение нулями главного массива отвечает метод create_newgame,
который так же добавляет два ненулевые элемента в случайные позиции с помощью другого метода add_piece.
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


class Game_core:
    def __init__(self):
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def is_grid_changed(self, copy_grid):
        for i in range(4):
            for j in range(4):
                if copy_grid[i][j] != self.grid[i][j]:
                    return True
        return False

    def make_grid_copy(self):
        copy_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            for j in range(4):
                copy_grid[i][j] = self.grid[i][j]
        return copy_grid

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

    def is_2048_in_grid(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 2048:
                    return True
        return False

    def move_left(self):
        for row in self.grid:
            while 0 in row:
                row.remove(0)
            while len(row) != 4:
                row.append(0)
        for i in range(4):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1] and self.grid[i][j] != 0:
                    self.grid[i][j] *= 2
                    self.grid[i].pop(j + 1)
                    self.grid[i].append(0)

    def move_right(self):
        for row in self.grid:
            while 0 in row:
                row.remove(0)
            while len(row) != 4:
                row.insert(0, 0)
        for i in range(4):
            for j in range(3, 0, -1):
                if self.grid[i][j] == self.grid[i][j - 1] and self.grid[i][j] != 0:
                    self.grid[i][j] *= 2
                    self.grid[i].pop(j - 1)
                    self.grid[i].insert(0, 0)
                    can_add_piece = True

    def move_up(self):
        self.swap_columns_to_rows()
        self.move_left()
        self.swap_columns_to_rows()

    def move_down(self):
        self.swap_columns_to_rows()
        self.move_right()
        self.swap_columns_to_rows()

    def swap_columns_to_rows(self):
        grid_copy = [[], [], [], []]
        for i in range(4):
            for j in range(4):
                grid_copy[i].append(self.grid[j][i])
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = grid_copy[i][j]

    def create_newgame(self):
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = 0
        self.add_piece()
        self.add_piece()
