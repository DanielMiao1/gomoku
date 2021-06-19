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
    self.board.print_board()
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
    # check for horizontal wins
    for x in self.board:
      for y in range(len(x) - 4):
        if x[y] == x[y + 1] == x[y + 2] == x[y + 3] == x[y + 4] and x[y] != " ": return x[y]
    for x in range(len(x) - 4):
      for y in range(12):
        if self.board[x][y] == self.board[x + 1][y] == self.board[x + 2][y] == self.board[x + 3][y] == self.board[x + 4][y] and self.board[x][y] != " ": return self.board[x][y]
    for x in range(len(self.board) - 4):
      for y in range(8):
        if self.board[x + 4][y + 4] == self.board[x + 3][y + 3] == self.board[x + 2][y + 2] == self.board[x + 1][y + 1] == self.board[x][y] and self.board[x][y] != " ": return self.board[x][y]
    return False

  def format_board(self, board): return self.add_numbers("\n--+---+---+---+---+---+---+---+---+---+---+--\n".join(" | ".join(i) for i in board))

  @staticmethod
  def add_numbers(board):
    new_board = ""
    for x, y in zip(board.splitlines(), range(1, 26)):
      if y % 2 == 0: new_board += "\n     " + x
      else: new_board += f"\n{str((y // 2) + 1).ljust(3)} {x}"
    return new_board
  def print_board(self):
    print(self.format_board(self.board))


g = Game()
g.start_game()


# check if there are 5 pieces in a row horizontally
# check if there are 5 pieces in a row vertically

# check all the diagonals for 5 in a row

# refactor
# if any(True for y in range(len([x for x in self.board]) - 4) if x[y] == x[y + 1] == x[y + 2] == x[y + 3] == x[y + 4] and x[y] != " ") or any()
# if all(self.board[x][y=]  for y in )