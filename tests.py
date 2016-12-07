import xo_game_random
import xo_player_random
import xo_player_smart

file = open("results.txt", "w")
op_player = xo_player_random.XOPlayerRandom()
game = xo_game_random.XOGameRandom(op_player)
file.write("Running tests against random player")
results = {"Win" : 0, "Cat's Game" : 0, "Lose" : 0}
for i in range(100):
	winner = game.play_game()
	if (winner == "X"):
		results["Win"] = results["Win"] + 1
	elif (winner == "O"):
		results["Lose"] = results["Lose"] + 1
	else:
		results["Cat's Game"] = results["Cat's Game"] + 1
	
	print(results)
	game.reset()

file.write(str(results))

op_player = xo_player_smart.XOPlayerSmart("O")
game = xo_game_random.XOGameRandom(op_player)
file.write("Running tests against smart player")
results = {"Win" : 0, "Cat's Game" : 0, "Lose" : 0}
for i in range(1000):
	winner = game.play_game()
	if (winner == "X"):
		results["Win"] = results["Win"] + 1
	elif (winner == "O"):
		results["Lose"] = results["Lose"] + 1
	else:
		results["Cat's Game"] = results["Cat's Game"] + 1
	
	print(results)
	game.reset()

file.write(str(results))