#using the lab3 sample code:lab3.py

from UltimateMetaTTT import NumTicTacToe
from UltimateMetaTTT import ClassicTicTacToe
from UltimateMetaTTT import MetaTicTacToe

def getEntry(player, entries):
	global numDescription
	global upperRange
	global lowerRange
	if player % 2 == 0:
		numDescription = 'even'#player2 enter even number
		lowerRange = 2#range
		upperRange = 8		
	else:
		numDescription = 'odd'#player1 enter odd number
		lowerRange = 1#range
		upperRange = 9		 
	prompt = 'Player {}, please enter an {} number ({}-{}): '
	prompt = prompt.format(player, numDescription, lowerRange, upperRange)

	entry =input(prompt)
	
	return int(entry)

def swich_Entry(player, entries):
	global numDescription
	global upperRange
	global lowerRange
	if player % 2 == 0:#player 2 enter odd number after the player switched
		numDescription = 'odd'
		lowerRange = 1
		upperRange = 9		
	else:
		numDescription = 'even'#player1 enter the even number
		lowerRange = 2
		upperRange = 8		 
	prompt_swich = 'Player {}, please enter an {} number ({}-{}): '
	prompt_swich = prompt_swich.format(player, numDescription, lowerRange, upperRange)

	entry =input(prompt_swich)
	
	return int(entry)

def getWrong_Entry(player, entries):
	global numDescription
	if player % 2 == 0:
		numDescription = 'even'
		lowerRange = 2
		upperRange = 8		
	else:
		numDescription = 'odd'
		lowerRange = 1
		upperRange = 9		 
	prompt_again1 = 'Error: entry not {} or out range. Player {} , please enter an {} number ({}-{}): '#if the player enter the wrong number or out of the range
	prompt_again1 = prompt_again1.format(numDescription, player, numDescription, lowerRange, upperRange)

	entry_again1 =input(prompt_again1)
	
	return int(entry_again1)

def getWrong_Entry_swich(player, entries):
	global numDescription
	if player % 2 == 0:
		numDescription = 'odd'#remind players to enter the correct number after swiching
		lowerRange = 1
		upperRange = 9		
	else:
		numDescription = 'even'
		lowerRange = 2
		upperRange = 8		 
	prompt_again1 = 'Error: entry not {} or out range. Player {} , please enter an {} number ({}-{}): '
	prompt_again1 = prompt_again1.format(numDescription, player, numDescription, lowerRange, upperRange)

	entry_again1 =input(prompt_again1)
	
	return int(entry_again1)


def getExist_Entry(player, entries):
	global numDescription
	if player % 2 == 0:
		numDescription = 'even'
		lowerRange = 2
		upperRange = 8		
	else:
		numDescription = 'odd'
		lowerRange = 1
		upperRange = 9		 
	prompt_again2 = 'Error: that number has already been entered . Player {} , please enter an {} number ({}-{}): '#when players enter the number that is choosed already, remind players to enter the correct number. 
	prompt_again2 = prompt_again2.format(player, numDescription, lowerRange, upperRange)

	entry_again2 =input(prompt_again2)
	
	return int(entry_again2)

def getCoord(player, dimension):
	
	LOWER = 0
	UPPER = 2
	index =input('Player ' + str(player) + ', please enter a ' + dimension+': ')#input the row and the column
	return int(index)


def getWrong_Coord(player,dimension):
	LOWER = 0
	UPPER = 2
	index_again =input('Not in correct range.' + 'Player' + str(player) + ', please enter a ' + dimension+': ')#if the input out of range, remind players to enter the correct dimension. 
	return int(index_again)

# def get_sameboard(player)

def getMark(player,entries):
	
	global mark
	if player % 2 == 0:#player2 use "X"
		mark = 'O'	
	else:
		mark = 'X'# player1 use "O"
	return mark
	Class_Index ='Player ' + str(player) + ', please enter a ' + dimension+': '#input the dimension
	enter_Mark = input(Class_Index)
	return int(enter_Mark)

def getMark_swich(player,entries):
	global mark
	if player % 2 == 0:
		mark = 'X'	
	else:
		mark = 'O'
	return mark
	Class_Index ='Player ' + str(player) + ', please enter a ' + dimension+': '#input the dimension after swiching
	enter_Mark = input(Class_Index)
	return int(enter_Mark)


def get_ClassicCoord(player,entries,dimension):
	global enter
	Class_Index ='Player ' + str(player) + ', please enter a ' + dimension+': '#if the player enter the dimension out of range,remind player
	enter = input(Class_Index)
	return int(enter)

def getWrong_ClassicCoord():
	if player % 2 == 0:
		Mark = 'O'	
	else:
		Mark = 'X'
	Class_Index =input('Not in correct range.' + 'Player' + str(player) + ', please enter a ' + dimension+': ')#remind players to enter the correct dimension.
	# localboard.update(row,col,mark)
	return str(Class_Index)

def isGameOver(myBoard, player):#critical result of the local board
	
	if myBoard.isWinner():
		myBoard.drawBoard()
		print ('Player', player ,"wins. Congrats!")		   
		return True
	elif myBoard.boardFull():
		myBoard.drawBoard()
		print ("It's a tie.")#think about draw			 
		return True  
	return False


def who_is_winner(myBoard,player):#critical result of the global board
	if myBoard.isWinner():
		print("Player {} wins. Congrats!".format(player))
		return True

	elif not  myBoard.isWinner() and myBoard.boardFull():
		print("It's a tie.")
		return True

def Ruturn_result(myBoard,localboard,player,myBoard_row,myBoard_col):#return the result to the global board
	# turn = 0
	global result
	if localboard.isWinner():
		# myBoard.drawBoard()
		
		if player % 2 == 0:
			result = 'O'
		else:
			result = 'X'	
		myBoard.update(myBoard_row,myBoard_col,result) 	   
		return 
	elif not myBoard.isWinner() and myBoard.boardFull():
		myBoard.drawBoard()
		print ("It's a tie.")
		result = 'D'
		myBoard.update(myBoard_row,myBoard_col,result)			 
		return   


def playAgain(Exception): #remind the player would play again
	
	try:
		while not_over:
			next_game = input("Do you want to play another game? (Y/N) ")
			# print(next_game.upper())

			if next_game.upper() == 'Y':
			
				Meta_play()
					
			elif next_game.upper() == 'N':
				print("Thanks for playing! Goodbye.")
				raise playAgain
	except:
		pass
	assert (next_game.upper() == 'N' or next_game.upper() == 'Y')," valid input"




Meta_Title = "Starting new Meta Tic Tac Toe game"#print the title
print("-" * len(Meta_Title))
print(Meta_Title)
print("-" * len(Meta_Title))


def Meta_play():
	global result
	global turn
	
	config  = open("MetaTTTconfig.txt",'r').read().splitlines()#open file for global board
	myBoard = MetaTicTacToe(config)
	myBoard.drawBoard()
	New_Game = False
	turn = 0#represent the player
	entries = []
	winner = 0
	# turn = current_player
	while not myBoard.boardFull():#if the board not full, game keep going
		enter = getMark(turn+1, entries)#player use "X","O"
		New_Game = True
		row = getCoord(turn+1, 'row')#enter dimension
		col = getCoord(turn+1, 'column')
		while (row >=3) or (col >=3):#if out of range, remind the player enter again.
			row = getWrong_Coord(turn+1, 'row')
			col = getWrong_Coord(turn+1, 'col')
		# print("1")
		localboard = myBoard.getLocalBoard(row,col)
		if localboard.isNum() == True:#determine the localboard
			numplay(localboard,myBoard,row,col)
		elif localboard.isNum() == False:
			classicplay(localboard,myBoard,row,col)
		else:
			print('Error: could not make move!')

		myBoard.drawBoard() 
		# turn = (turn+1) % 2
		if who_is_winner(myBoard,turn+1):#determine the winner
			return
		turn = (turn+1) % 2	# make the player number can not over 2
		

def numplay(localboard,myBoard,myBoard_row,myBoard_col):
	global numDescription
	global upperRange
	global lowerRange
	global turn
	newGame = True
	current_num = []#create a list for number that already entered
	while newGame:
		TITLE = ("This is a Numerical Tic Tac Toe.")
		print("-"*len(TITLE))
		print (TITLE)

		localboard = NumTicTacToe()
		gameOver = False
		num_turn = 0
		num_turn = turn
		current_player = num_turn
		#turn = current_player
		entries = []
		winner = 0
		while not gameOver:
			localboard.drawBoard()
			
			# get input from user
			if current_player + 1 == 1:#current player is 1
				entry = getEntry(num_turn+1, entries)
				if (num_turn + 1) % 2 == 0:	 #plyer2
					while entry % 2 != 0 or entry > upperRange + 1 or entry < lowerRange - 1:#if the player2 enter the odd number or out of range
						entry = getWrong_Entry(num_turn+1, entries)#remind the player enter again
				elif (num_turn + 1) % 2 != 0: #player 1
					while entry % 2 == 0 or entry > upperRange +1 or entry < lowerRange - 1:#if the player1 enter the even number or out of range
						entry = getWrong_Entry(num_turn+1, entries)
			elif current_player +1 ==2:
				entry = swich_Entry(num_turn+1, entries)#swich player
				if (num_turn + 1) % 2 == 0:	 #plyer2
					while entry % 2 == 0 or entry > upperRange + 1 or entry < lowerRange - 1:#if the player2 enter the even number or out of range
						entry = getWrong_Entry_swich(num_turn+1, entries)
				elif (num_turn + 1) % 2 != 0:
					while entry % 2 != 0 or entry > upperRange +1 or entry < lowerRange - 1:#if the player1 enter the odd number or out of range
						entry = getWrong_Entry_swich(num_turn+1, entries)
			
			for i in current_num:
				if entry == i:
					getExist_Entry(num_turn+1, entries)


			row = getCoord(num_turn+1, 'row')
			col = getCoord(num_turn+1, 'column')
			while (row >=3) or (col >=3):# if the player enter the dimension out of range
				row = getWrong_Coord(num_turn+1, 'row')
				col = getWrong_Coord(num_turn+1, 'col')
			# print("333")
								   
			if localboard.update(row, col, entry):#update board
				entries.append(entry)
				gameOver = isGameOver(localboard, num_turn+1)
				current_num.append(int(entry))
				newGame = Ruturn_result(myBoard,localboard,num_turn+1,myBoard_row,myBoard_col)
				
				num_turn = (num_turn+1) % 2	# make the player number can not over 2
			
			
			else:
				print('Error: could not make move!')
				
			

def classicplay(localboard,myBoard,myBoard_row,myBoard_col):
	
	global numDescription
	global upperRange
	global lowerRange
	global enter
	global mark
	global turn
	newGame=True
	while newGame:
		TITLE = ("This is a Classical Tic Tac Toe.")
		print("-"*len(TITLE))
		print (TITLE)

		localboard = ClassicTicTacToe()
		gameOver = False
		class_turn = 0
		class_turn = turn
		current_player = class_turn
		#turn = current_player
		entries = []
		winner = 0
		while not gameOver:
			localboard.drawBoard()
			# print("111")
			if current_player + 1 == 1:
				enter = getMark(class_turn+1, entries)#player1 use "X", player2 use"O"
			elif current_player + 1 ==2:#swich player
				enter = getMark_swich(class_turn+1, entries)#player1 use "O", player2 use"X"
			classic_row = get_ClassicCoord(class_turn+1, entries,'row')# enter the dimension
			classic_col = get_ClassicCoord(class_turn+1, entries,'col')
	
			while (classic_row >=3) or (classic_col >=3):# if the player enter the dimension out of range,remind player
				classic_row = getWrong_Coord(class_turn+1, 'row')
				classic_col = getWrong_Coord(class_turn+1, 'col')

			#print("777")					   

			if localboard.update(classic_row,classic_col,mark):#update board
				entries.append(enter)
				gameOver = isGameOver(localboard, class_turn+1)
				newGame = Ruturn_result(myBoard,localboard, class_turn+1,myBoard_row,myBoard_col)
				class_turn = (class_turn+1) % 2	# make the player number can not over 2
			 
			else:
				print('Error: could not make move!')
			



if __name__ == "__main__":
	
	not_over=True
	Meta_play()
	# while not_over:
	next_game = playAgain(Exception)


		
	