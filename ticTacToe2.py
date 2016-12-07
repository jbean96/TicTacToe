import xo_game
import time
from methods import print_typing

print_typing("Let's play some tic-tac-toe!")
print_typing("Would you like to be 'X' or 'O'?")
player = None
while (player == None):
	user_in = input()
	if (user_in == "X" or user_in == "O"):
		player = user_in
game = xo_game.XOGame(player)
while True:
	game.play_game()
	print_typing(game.winner, end=" ")
	if (game.winner != "Cat's Game"):
		print_typing("wins!")
	else:
		print()
	while True:
		print_typing("Would you like to play again? (yes/no): ", end="")
		user = input()
		if (user == "yes" or user == "no"):
			break
	if (user == "no"):
		break
	game.reset()
print_typing("Thanks for playing!")