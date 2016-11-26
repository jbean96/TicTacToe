import xo_board
import xo_board_evaluator
import sys
import random
import xo_player_random
import xo_player_smart
from methods import print_typing

class XOGame:
	def __init__(self):
		self.board = xo_board.XOBoard()
		self.eval = xo_board_evaluator.XOBoardEvaluator()
		self.op_player = xo_player_smart.XOPlayerSmart()
		self.winner = None
	
	# Gets the next move and returns it an array of two ints [row, col]
	def get_move(self):
		while True:
			print_typing("What is your move? (row col): ", "", 0.0)
			try:
				user_in = input()
				row, col = user_in.split(" ")
				move = [int(row), int(col)]
				if (self.board.available_moves.count(move) == 1):
					break;
				print_typing("Invalid move", base_delay=0.0)
			except ValueError:
				if (user_in == "exit"):
					sys.exit()
				print_typing("Please enter your move in the form: row col", base_delay=0.0)
			print_typing("Try again", base_delay=0.0)
		return move
	
	# The main game loop, plays until the game is won
	def play_game(self):
		game_won = False
		x_move = random.randint(0, 1)
		if (x_move):
			print("X", end=" ")
		else:
			print("O", end=" ")
		print_typing("moves first.")
		
		while (not(game_won)):
			if x_move:
				self.board.draw_board()
				move = self.get_move()
			else:
				move = self.op_player.get_move(self.board)
			if (x_move):
				self.board.exec_move(move, "X")
			else:
				self.board.exec_move(move, "O")
			x_move = not(x_move)
			game_won, self.winner = self.eval.is_won(self.board)
		
		self.board.draw_board()
	
	def reset(self):
		self.board.new_board()
		self.winner = None

