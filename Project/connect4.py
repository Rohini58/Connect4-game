#import numpy as numpy

ROW_COUNT=5
COLUMN_COUNT=6
def create_board():
	board=[[0,0,0,0,0,0]]*ROW_COUNT#np.zeros((5,6))
	
	return board
def drop_piece(board,row,col,piece):
	return board[row][col]==piece
def is_valid_location(board,col):
	return board[4][col]==0
def get_next_open_row(board,col):
	for r in range(col):
		if board[r][col]==0:
			return r
def print_board(board):
	print(board)
create_board()
board=create_board()
game_over=False
turn=0
print_board(board)
def board_number(board,col,player):
	r=ROW_COUNT-1
	print(player)
	while (r>=0):
		if(board[r][col]==0):
			board[r][col]=player
			break
		elif(r==0):
			print("Column full")
		r=r-1
			
while not game_over:
	#Ask for player 1 Input
	if turn == 0:
		col=int(input("Player 1 make your(0-5):"))
		if is_valid_location(board,col):
			board_number(board,col,1)
			row=get_next_open_row(board,col)
			#drop_piece(board,row,col,1)
			print_board(board)

 #Ask for player 2 Input
		turn=1
	else:
		col=int(input("Player 2 make your(0-5):"))
		if is_valid_location(board,col):
			board_number(board,col,2)
			row=get_next_open_row(board,col)
			#drop_piece(board,row,col,2)
			print_board(board)
		turn=0
		
				
	
