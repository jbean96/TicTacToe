import xo_board

class XOBoardEvaluator:
	def __init__(self):
		None
		
	# Evaluates the status of the given board, returns None if the game is not yet finished,
	# returns "Cat's Game" if the game cannot be won; if the game has been won, the method
	# returns a string representing the winning player
	def is_won(self, board):
		for i in range(3):
			row = self.win_row(board, i)
			if (row != None):
				return True, row
			col = self.win_col(board, i)
			if (col != None):
				return True, col
		diag1 = self.win_diag1(board)
		if (diag1 != None):
			return True, diag1
		diag2 = self.win_diag2(board)
		if (diag2 != None):
			return True, diag2
		if (board.moves[0].count(" ") == 0 and board.moves[1].count(" ") == 0 and board.moves[2].count(" ") == 0):
			return True, "Cat's Game"
		return False, None
	
	def win_row(self, board, row):
		if (board.moves[row].count("X") == 3):
			return "X"
		elif(board.moves[row].count("O") == 3):
			return "O"
	
	def win_col(self, board, col):
		if (board.moves[0][col] != " " and board.moves[0][col] == board.moves[1][col] and board.moves[1][col] == board.moves[2][col]):
			return board.moves[0][col]
	
	def win_diag1(self, board):
		if (board.moves[0][0] != " " and board.moves[0][0] == board.moves[1][1] and board.moves[1][1] == board.moves[2][2]):
			return board.moves[0][0]
	
	def win_diag2(self, board):
		if (board.moves[0][2] != " " and board.moves[0][2] == board.moves[1][1] and board.moves[1][1] == board.moves[2][0]):
			return board.moves[0][2]