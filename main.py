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

# PIECES Ø X

class Game:
  def __init__(self):
    self.start_game()
  
  @staticmethod
  def print_intro():
    print("Gomoku Game")

  def start_game(self):
    self.print_intro()
    players, choices, board, turn = [Player(), Player()], ("X", "O"), Board(), False
    player_won = board.player_won()
    while not player_won:
      board.print_board()
      print(f"It is {choices[int(turn)]} ({['Player 1', 'Player 2'][choices[int(turn)]]})'s turn'")
      while True:
        row, col = players[int(turn)].get_move()
        if board.board[row - 1][col - 1] == " ": break
        print("Invalid Input")
      board.board[row - 1][col - 1] = choices[int(turn)]
      turn = not turn

class Player:
  def get_move(self):
		row = int(input("Row:"))  
		column = int(input("Column:"))
		if 0 < row < 13 and 0 < column < 13: 
			return (row,column)
      
		return self.get_move()

class Board:
  def __init__(self):
    self.board = [[0 for i in range(12)] for _ in range(12)]

  def has_player_won(self):
    """Return the player if one won"""
    return "FUNCTION has_player_won"

  def get_valid_moves(self):
    return "FUNCTION get_valid_moves"

  def place_move(self):
    return "FUNCTION place_move"

  def print_board(self):
    pass

if __name__ == "___main__":
  g = Game()
  g.start_game()