from IPython.display import clear_output
player1 = ""
player2 = ""

def start_game():
	board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
	validInput = False
	while(validInput == False):
		player1 = input("Please pick a marker 'X' or 'O': ")
		if player1 == 'X':
			player2 = 'O'
			validInput = True
		else:
			player2 = 'X'
			validInput = False
	print(player1)
	display_board(board)
	await_user_input(1,player1, player2, board)

def display_board(items):
	print('\n'*100)
	print(items[7] + "|" + items[8] + "|" + items[9])
	print("-----")
	print(items[4] + "|" + items[5] + "|" + items[6])
	print("-----")
	print(items[1] + "|" + items[2] + "|" + items[3])
	

def await_user_input(player, player1, player2, board):
	chosenSquare = int(input("Please enter a number player {}: ".format(player)))
	if position_available(board, chosenSquare):
		if player == 1:

			board[chosenSquare] = player1
			display_board(board)
			check_for_winner(player1, player, board)
			player = 2
		else:
			board[chosenSquare] = player2
			display_board(board)
			check_for_winner(player2, player, board)		
			player = 1
	else:
		print("Position already chosen, please choose again")
	await_user_input(player, player1, player2, board)

def check_for_winner(marker, player, board):
	if board[7] == board[8] == board[9] == marker:
		#win
		player_wins(player)
	elif board[4] == board[5] == board[6] == marker:
		#win
		player_wins(player)
	elif board[1] == board[2] == board[3] == marker:
		#win
		player_wins(player)
	elif board[1] == board[5] == board[9] == marker:
		#win
		player_wins(player)
	elif board[7] == board[5] == board[3] == marker:
		#win
		player_wins(player)
	elif board[7] == board[4] == board[1] == marker:
		#win
		player_wins(player)
	elif board[8] == board[5] == board[2] == marker:
		#win
		player_wins(player)
	elif board[9] == board[6] == board[3] == marker:
		#win
		player_wins(player)
	elif " " not in board:
		#draw
		player_draws()

def player_wins(player):
	print("Player {} has won the game! Well done!".format(player))
	end_game()
def player_draws():
	print("The game has ended in a draw!")
	end_game()
def end_game():
	response = input("Would you like to play again? (Y/N)")
	if response.upper() == 'Y':
		start_game()
	else:
		quit()

def position_available(board, position):
	return board[position] == " "

start_game()