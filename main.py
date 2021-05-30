# gomoku board
# 12x12

# player wins if they get 5 or more in a row

# players take turns placing an X or an O piece
# on an empty board

# game class: manages the gameplay

# player class: one player object for each player
# get_move

# board class: responsible for making a move on the board\
# makes the board
# gets all the available moves on the board (empty spaces)
# checks if a player has won

# PIECES Ø X

class Game:
  def __init__(self):
    self.print_intro()
  
  @staticmethod
  def print_intro():
    print("Gomoku Game")

class Player(Game):
  def __init__(self):
    print("Player class")

class Board(Game):
  def __init__(self):
    print("Board class")

if __name__ == "___main__":
  g = Game()
  g.start_game()