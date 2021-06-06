# gomoku board
# 12x12

# player wins if they get 5 or more in a row

# players take turns placing an X or an O piece
# -*- coding: utf-8 -*-
# on an empty board

# game class: manages the gameplay

# player class: one player object for each player
# get_move

# board class: responsible for making a move on the board\
# makes the board
# gets all the available moves on the board (empty spaces)
# checks if a player has won

# PIECES O X

class Game:
  def __init__(self):
    self.board = Board()
  
  @staticmethod
  def print_intro(): print("Gomoku Game")

  def start_game(self):
    self.print_intro()
    players, choices, turn = [Player(), Player()], ["X", "O"], False
    player_won = self.board.has_player_won()
    while not player_won:
      self.board.print_board()
      print(
        f"It is {choices[int(turn)]}"
        f" ({['Player 1', 'Player 2'][int(turn)]})'s turn."
      )
      while True:
        row, col = players[int(turn)].get_move()
        if self.board.board[row - 1][col - 1] == " ": break
        print("Invalid Input")
      self.board.board[row - 1][col - 1] = choices[int(turn)]
      turn = not turn
      player_won = self.board.has_player_won()
    print(player_won)

class Player:
  def get_move(self):
    try:
      row, column = int(input("Row: ")), int(input("Column: "))
      if 0 < row < 13 and 0 < column < 13: return (row,column)
    except: pass

    print("Invalid input")
    return self.get_move()
      
      

class Board:
  def __init__(self):
    self.board = [[" " for i in range(12)] for _ in range(12)]

  def has_player_won(self):
    """Return the player if one won"""
    for i in range(5):
      if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] == self.board[i][4] and self.board[i][0] != " ": return self.board[i][0]
    # if any([True for i in range(5) if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] and board[i][0] != " "]):
    # return (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ") or (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ") or any([True for i in range(5) if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " "]) or any([True for i in range(3) if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " "])
    return False

  @staticmethod
  def format_board(board): return "\n--+---+---+---+---+---+---+---+---+---+---+--\n".join(" | ".join(i) for i in board)

  def print_board(self):
    print(self.format_board(self.board))

# i for in ["".join([str(row) for row in self.board])]



g = Game()
g.start_game()