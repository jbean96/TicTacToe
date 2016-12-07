import xo_board
import xo_board_evaluator
import sys
import random
import xo_player_random
import xo_player_smart
from methods import print_typing

class XOGameRandom:
	def __init__(self, opposing_player):
		self.board = xo_board.XOBoard()
		self.eval = xo_board_evaluator.XOBoardEvaluator()
		self.op_player = opposing_player
		self.player = xo_player_smart.XOPlayerSmart("X");
		self.winner = None
		
	def play_game(self):
		game_won = False
		x_move = random.randint(0, 1)
		
		while (not(game_won)):
			if x_move:
				move = self.player.get_move(self.board)
				self.board.exec_move(move, "X")
			else:
				move = self.op_player.get_move(self.board)
				self.board.exec_move(move, "O")
			x_move = not(x_move)
			game_won, self.winner = self.eval.is_won(self.board)
		
		return self.winner
		
	def reset(self):
		self.board.new_board()
		self.winner = None
