import xo_board
import xo_board_evaluator
import random

class XOPlayerSmart:
	# player is either "X" or "O" representing which character this 
	# player is
	def __init__(self, player):
		self.evaluator = xo_board_evaluator.XOBoardEvaluator()
		self.player = player
		if (self.player == "X"):
			self.op_player = "O"
		else:
			self.op_player = "X"
		
	def get_move(self, board):
		moves = list(board.available_moves)
		# If this player gets the first move, the best move is in the middle
		# because it has the most possibilities for winning the game
		if (len(moves) >= 8 and moves.count([1, 1]) == 1):
			return [1, 1]
		scores = []
		for i in range(len(moves)):
			board.exec_move(moves[i], self.player)
			score = -1 * self.get_board_score(board, self.op_player, 1)
			scores.append(score)
			board.undo_move(moves[i])
		
		best_score = -11
		for i in range(len(scores)):
			if (scores[i] > best_score):
				best_score = scores[i]
		
		best_moves = []
		for i in range(len(scores)):
			if (scores[i] == best_score):
				best_moves.append(moves[i])

		choice = random.randint(0, len(best_moves) - 1)
		return best_moves[choice]
				
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
		
		
				