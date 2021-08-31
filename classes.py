import random


class Tile:
    def __init__(self, x, y, is_obstacle=False):
        self.x = x
        self.y = y
        self.is_obstacle = is_obstacle
        self.start = False
        self.finish = False


class Board:
    def __init__(self, rows, cols):
        self.tiles = []
        self.rows = rows
        self.cols = cols
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
                if self.tiles[i][j].start:
                    print('\033[95mS \033[0m', end='')
                elif self.tiles[i][j].finish:
                    print('\033[95mF \033[0m', end='')
                elif self.tiles[i][j].is_obstacle:
                    print('X ', end='')
                else:
                    print('- ', end='')
            print('')

    def place_start(self, row, col):
        self.tiles[row][col].start = True
        self.tiles[row][col].is_obstacle = False

    def place_finish(self, row, col):
        self.tiles[row][col].finish = True
        self.tiles[row][col].is_obstacle = False