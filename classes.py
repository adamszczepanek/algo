import random


class Tile:
    def __init__(self, i, j, is_obstacle=False):
        self.i: int = i
        self.j: int = j
        self.is_obstacle: bool = is_obstacle
        self.start: bool = False
        self.finish: bool = False
        self.f: float = float('inf')
        self.g: float = float('inf')
        self.h: float = float('inf')
        self.neighbors = []
        self.previous: Tile
        self.is_closed = False
        self.is_route = False

    def add_neighbors(self, board):
        if self.neighbors:
            return

        if self.j < board.cols - 1 and not board.tiles[self.i][self.j + 1].is_obstacle:
            self.neighbors.append(board.tiles[self.i][self.j + 1])
            print("dupa", board.tiles[self.i][self.j + 1].i, board.tiles[self.i][self.j + 1].j)
        if self.j > 0 and not board.tiles[self.i][self.j - 1].is_obstacle:
            self.neighbors.append(board.tiles[self.i][self.j - 1])
        if self.i < board.rows - 1 and not board.tiles[self.i + 1][self.j].is_obstacle:
            self.neighbors.append(board.tiles[self.i + 1][self.j])
        if self.i > 0 and not board.tiles[self.i - 1][self.j].is_obstacle:
            self.neighbors.append(board.tiles[self.i - 1][self.j])


class Board:
    def __init__(self, rows, cols):
        self.tiles = []
        self.rows = rows
        self.cols = cols
        self.start = []
        self.finish = []
        for i in range(rows):
            self.tiles.append([])
            for j in range(cols):
                if random.random() < 0.2:
                    self.tiles[i].append(Tile(i, j, is_obstacle=True))
                else:
                    self.tiles[i].append(Tile(i, j))

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) == (self.start[0], self.start[1]):
                    print('\033[95mS \033[0m', end='')
                elif (i, j) == (self.finish[0], self.finish[1]):
                    print('\033[95mF \033[0m', end='')
                elif self.tiles[i][j].is_obstacle:
                    print('X ', end='')
                elif self.tiles[i][j].is_route:
                    print('R ', end='')
                else:
                    print('- ', end='')
            print('')

    def place_start(self, row, col):
        self.start = [row, col]
        self.tiles[row][col].g = 0

    def place_finish(self, row, col):
        self.finish = [row, col]
