import random
from classes import Board
from operator import attrgetter
import math


def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def algo(board):
    start_tile = board.tiles[board.start[0]][board.start[1]]
    finish_tile = board.tiles[board.finish[0]][board.finish[1]]
    open_set = [start_tile]
    start_tile.add_neighbors(board)
    start_tile.f = calc_dist(start_tile.i, start_tile.j, finish_tile.i, finish_tile.j)

    while open_set:
        current_tile = min(open_set, key=attrgetter('f'))

        if current_tile == finish_tile:
            while current_tile != start_tile:
                current_tile.is_route = True
                current_tile = current_tile.previous
            return True

        open_set.remove(current_tile)

        current_tile.is_closed = True
        for neighbor in current_tile.neighbors:
            if not neighbor.is_closed:
                neighbor.add_neighbors(board)

                if current_tile.g + 1 < neighbor.g:
                    neighbor.previous = current_tile
                    neighbor.g = current_tile.g + 1
                    neighbor.f = neighbor.g + calc_dist(neighbor.i, neighbor.j, finish_tile.i, finish_tile.j)

                if neighbor not in open_set:
                    open_set.append(neighbor)


if __name__ == '__main__':
    board = Board(15, 15)
    board.place_start(0, 0)
    board.place_finish(14, 14)
    algo(board)
    board.draw()
