import random
from classes import Board

if __name__ == '__main__':
    board = Board(15, 15)
    board.place_start(0, 0)
    board.place_finish(14, 14)
    board.draw()