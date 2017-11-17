def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
		
def getPlayerMove(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		from PySetup import isSpaceFree
		print('What is your next move? (1-9)')
		move = input()
	return int(move)