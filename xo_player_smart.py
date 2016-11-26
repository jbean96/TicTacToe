import xo_board
import xo_board_evaluator
import random

class XOPlayerSmart:
	def __init__(self):
		self.evaluator = xo_board_evaluator.XOBoardEvaluator();
		
	def get_move(self, board):
		moves = list(board.available_moves)
		best_score = -10
		best_move = moves[0]
		for move in moves:
			board.exec_move(move, "O")
			score = -1 * self.get_board_score(board, "X", 1)
			if (score > best_score or (score == best_score and random.randint(0, 1))):
				best_score = score
				best_move = move	
			board.undo_move(move)
		return best_move
				
	def get_board_score(self, board, player, depth):
		is_won, winner = self.evaluator.is_won(board)
		if (is_won):
			if (winner == player):
				return 10 - depth
			elif (winner == "Cat's Game"):
				return 0
			else:
				return depth - 10
		else:
			depth = depth + 1
			moves = list(board.available_moves);
			best_score = -10
			for move in moves:
				if (player == "X"):
					next_player = "O"
				else:
					next_player = "X"
				board.exec_move(move, player)
				score = -1 * self.get_board_score(board, next_player, depth)
				if (score > best_score):
					best_score = score
				board.undo_move(move)
			return best_score
		
		
				