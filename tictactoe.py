from IPython.display import clear_output
import random

def board_display(board):
	''' Print the board. '''

	clear_output(wait=True)
	print('   |   |')
	print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('-----------')
	print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('-----------')
	print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def player_input():
	''' Assigns 'X' or 'O' to player one or two. '''
	marker = ''
	while not(marker == 'X' or marker == 'O'):
		print('Player two will play the unchosen marker.')
		marker = input("Type 'X' or 'O' for the player one: ").upper()
		

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def place_marker(board, marker, position):
	''' Print a marker in the desired position. '''
	board[position] = marker

def win_check(board, marker):
	''' Verifies if the last person to play won. '''
	return ((board[1] == marker and board[2] == marker and board[3] == marker) or
	(board[4] == marker and board[5] == marker and board[6] == marker) or
	(board[7] == marker and board[8] == marker and board[9] == marker) or
	(board[1] == marker and board[4] == marker and board[7] == marker) or
	(board[2] == marker and board[5] == marker and board[8] == marker) or
	(board[3] == marker and board[6] == marker and board[9] == marker) or
	(board[1] == marker and board[5] == marker and board[9] == marker) or
	(board[7] == marker and board[5] == marker and board[3] == marker))

def choose_first():
	''' Randomly chooses the first to play. '''
	if random.randint(1,2) == 1:
		return 'Player one'
	else:
		return 'Player two'

def space_check(board, position):
	''' Verifies if a space on the board is available. '''
	return board[position] == ' '

def full_board_check(board):
	''' Verifies if the board is full. This functions helps to declare a draw. '''
	for i in range(1, 10):
		if space_check(board, i):
			return False
	else:
		return True

def player_choice(board):
	''' Receives a desired position and checks if it's available. '''
	playerchoice_position = 0
	while playerchoice_position not in '1 2 3 4 5 6 7 8 9'.split() and not space_check(board, int(playerchoice_position)):
		playerchoice_position = input('Type a position from 1 to 9: ')

	return int(playerchoice_position)

def replay():
	''' Asks the player for a replay. '''
	return input('For replay type "YES", to leave type anything: ').upper().startswith('YES')

print('Welcome to tic tac toe!')

while True:
	# Reset the board
	theBoard = [' '] * 10
	theBoard[0] = '*'
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print('{} plays first!'.format(turn))
	game_on = True

	while game_on:
		# Player one's turn
		if turn == 'Player one':
			board_display(theBoard)
			print('Player 1')
			position = player_choice(theBoard)
			place_marker(theBoard, player1_marker, position)
			if win_check(theBoard, player1_marker):
				board_display(theBoard)
				print('Player one wins!')
				game_on = False
			else:
				if full_board_check(theBoard):
					board_display(theBoard)
					print('Draw!')
					game_on = False
				else:
					turn = 'Player two'
		# Player two's turn
		else:
			board_display(theBoard)
			print('Player 2')
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker, position)
			if win_check(theBoard, player2_marker):
				board_display(theBoard)
				print('Player two wins!')
				game_on = False
			else:
				if full_board_check(theBoard):
					board_display(theBoard)
					print('Draw!')
					game_on = False
				else:
					turn = 'Player one'

	if not replay():
		break
