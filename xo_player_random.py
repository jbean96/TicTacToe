from xo_board import XOBoard
import random

# This class is an opposing player for tic-tac-toe who makes moves
# completely at random
class XOPlayerRandom:
	def __init__(self):
		None
	
	def get_move(self, board):
		index = random.randint(0, len(board.available_moves) - 1)
		return board.available_moves[index]