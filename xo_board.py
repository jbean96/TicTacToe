class XOBoard:
	def __init__(self):
		self.new_board()
	
	def new_board(self):
		self.moves = []
		self.available_moves = []
		for row in range(3):
			self.moves.append([" ", " ", " "])
			for col in range(3):
				self.available_moves.append([row, col])
		
	# Draws the tic-tac-toe game board
	def draw_board(self):
		print("    0   1   2 ")
		print("   ___________")
		print("  |   |   |   |")
		self.draw_row(0)
		print("  |___|___|___|")
		print("  |   |   |   |")
		self.draw_row(1)
		print("  |___|___|___|")
		print("  |   |   |   |")
		self.draw_row(2)
		print("  |___|___|___|")

	# Draws the given row of the board
	def draw_row(self, row):
		print(row, "|", end=" ")
		print(self.moves[row][0], end="")
		print(" | ", end="")
		print(self.moves[row][1], end="")
		print(" | ", end="")
		print(self.moves[row][2], end="")
		print(" |")
	
	# Executes the given move and puts the correct player symbol at the position
	# where the move is made
	def exec_move(self, move, player):
		try:
			self.available_moves.remove(move)
			row = move[0]
			col = move[1]
			self.moves[row][col] = player
			return 0
		except ValueError:
			print("Move", move, "cannot be executed...")
			return 1
	
	def undo_move(self, move):
		self.available_moves.append(move)
		row = move[0]
		col = move[1]
		self.moves[row][col] = " "