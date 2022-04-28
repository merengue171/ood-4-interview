"""
The system should support two online players to play a game of chess.

All rules of international chess will be followed.

Each player will be randomly assigned a side, black or white.

Both players will play their moves one after the other. The white side plays the first move.
"""

from abc import ABC
from enum import Enum

class GameStatus(Enum):
  ACTIVE, BLACK_WIN, WHITE_WIN, FORFEIT, STALEMATE, RESIGNATION = 1, 2, 3, 4, 5, 6

class Board:
  def __init__(self):
    self.__boxes = [[]]
    self.reset_board()

  def get_box(self, x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
      raise Exception("Index out of bound")
    return self.__boxes[x][y]

  def reset_board(self):
    # initialize white pieces
    boxes[0][0] = Box(Rook(True), 0, 0);
    boxes[0][1] = Box(Knight(True), 0, 1);
    boxes[0][2] = Box(Bishop(True), 0, 2);
    #...
    boxes[1][0] = Box(Pawn(True), 1, 0);
    boxes[1][1] = Box(Pawn(True), 1, 1);
    #...
    
    # initialize black pieces
    boxes[7][0] = Box(Rook(False), 7, 0);
    boxes[7][1] = Box(Knight(False), 7, 1);
    boxes[7][2] = Box(Bishop(False), 7, 2);
    #...
    boxes[6][0] = Box(Pawn(False), 6, 0);
    boxes[6][1] = Box(Pawn(False), 6, 1);
    # ...

    # initialize remaining boxes without any piece
    for i in range(2, 6):
      for j in range(0, 8):
        boxes[i][j] = Box(None, i, j)

class Box:
  def __init__(self, piece, x, y):
    self.__piece = piece
    self.__x = x
    self.__y = y

  def get_piece(self):
    return self.__piece

  def set_piece(self, piece):
    self.__piece = piece

  def get_x(self):
    return self.__x

  def set_x(self, x):
    self.__x = x

  def get_y(self):
    return self.__y

  def set_y(self, y):
    self.__y = y
    
class Piece(ABC):
  def __init__(self, white=False):
    self.__killed = False
    self.__white = white

  def is_white(self):
    return self.__white

  def set_white(self, white):
    self.__white = white

  def is_killed(self):
    return self.__killed

  def set_killed(self, killed):
    self.__killed = killed

  def can_move(self, board, start_box, end_box):
    None

class King(Piece):
    pass

class Knight(Piece):
    pass

class Player():
  def __init__(self, name, white_side=False):
    self.__name = name
    self.__white_side = white_side

  def is_white_side(self):
    return self.__white_side

class Game():
    def __init__(self):
        self.__players = []
        self.__board = Board()
        self.__current_turn = None
        self.__status = GameStatus.ACTIVE
        self.__moves_played = []
    
    def initialize(self, player1, player2):
        self.__players[0] = player1
        self.__players[1] = player2

        self.__board.reset_board()

        if player1.is_white_side():
            self.__current_turn = player1
        else:
            self.__current_turn = player2

        self.__moves_played.clear()

    def is_end(self):
        return self.get_status() != GameStatus.ACTIVE

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def player_move(self, player, start_x, start_y, end_x, end_y):
        start_box = self.__board.get_box(start_x, start_y)
        end_box = self.__board.get_box(end_x, end_y)
        return self.__make_move(player, start_box, end_box)

    def __make_move(self, player, start, end):
        pass

