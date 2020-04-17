'''
main function responsible for the functions interface
@params none
@return none
'''
def main():			
	#Making varaibles for current chess board new chessboard
	new_chessboard = []
	current_chessboard = []
	new_chessboard = blank_chessboard()
	current_chessboard = blank_chessboard()
	while True:
		#creating a option menu
		print("\n**Chess Piece Relative Value Program**\n\t\t*Options*\n1.Create a new chessboard\n2.Move a chesspiece\n3.Show a sample chessboard\n4.About this program\n5.Quit")
		#printting chessboard with score and giving a option to a user
		print_chessboard(current_chessboard)
		score(current_chessboard)		
		option = check()
		while True:
			#each option has a diffrent objective
			if option == "_":
				break
			elif option == 1:#creates a new chessboard
				current_chessboard = create_a_chessboard(new_chessboard)
				new_chessboard = blank_chessboard()
				break
			elif option == 2:#moves a piece in a chessboard
				current_chessboard = move_a_piece(current_chessboard)
				break
			elif option == 3:
				current_chessboard = sample_chessboard()
				break	
			elif option == 4:#gives information on what the program is about then gives some instructions
				about()
				break
			elif option == 5:#exits
				exit()
				break
'''
sample_chessboard function provides a fresh new chessboard without any modifications on it
@params none
@return blank 2 dimensional chessboard in a list
'''
def blank_chessboard():
	string = "ABCDEFGH"  #takes blank list appends rows (blank2) to the list so that it creates rows and coloums
	blank = []
	for i in range(8):
		blank2 = []
		for k in range(8):
			blank2.append("-")
		blank2.insert(0, string[i])
		blank.append(blank2)
	blank.insert(0, [" ", "1" ,"2","3","4","5","6","7","8"]) #needed for a beggining row
	return blank
'''
sample_chessboard function allows the user to view a sample chessboard to see what the score would generally look like
@params none
@ s_chessboard sample chessboard in a list
'''
def sample_chessboard():
	string = "ABCDEFGH"  #takes blank list, appends rows (blank2) to the list so that it creates rows and coloums
	s_chessboard = []
	for i in range(8):
		s_chessboard_2 = []
		for k in range(8):
			s_chessboard_2.append("-")
		s_chessboard_2.insert(0, string[i])
		s_chessboard.append(s_chessboard_2)
	s_chessboard.insert(0, [" ", "1" ,"2","3","4","5","6","7","8"]) #needed for a beggining row
	s_chessboard[2].insert(5, "R")
	s_chessboard[2].pop(6)
	s_chessboard[6].insert(3, "q")
	s_chessboard[6].pop(4)
	return s_chessboard
'''
create_a_chessboard function creates a chessboard that the user would like by asking it where it wants the first players chess pieces to go, places them on the chessboard, then the second players chesspieces, then places it on the chessboard
@params chessboard 2d list containing a blank chessboard
@return chessboard user modified 2d list which is there chess board of choice
'''
def create_a_chessboard(chessboard):
	#making variables in order to create the code
	first_player = ["K", "Q", "R", "N", "B", "P"]
	second_player = ["k", "q", "r", "n", "b", "p"]
	sample_first_player = ["K (king)", "Q (queen)", "R (rook)", "N (knight)", "B (bishop)", "P (pond)"]
	sample_second_player = ["k (king)", "q (queen)", "r (rook)", "n (knight)", "b (bishop)", "p (pond)"]
	y = 0
	#first players choosing
	while True:	
		while y == 0:
			#shows the first players options
			print("\nYou have selected create a chessboard!!\nIn this option you can place any chess piece at any location below.\nStart with the first player's chess pieces.\n")
			print("These are first player selections")
			for first in sample_first_player:
				print (first)
				print ()
			#asks the first player what he would like to use and where he would like to place it
			position = input("First player: what would you like to place down and where, exp = Q, A3\ninsert c to switch to second player: ")
			if position == "c":#if inputed c, go to the next player
				y +=1
				break
			list1 = [position[0], position[-2], position[-1]]
			# Once selected the object and position, it appends it to the spot and deletes the one infront of it
			if list1[0] in first_player and list1[1] in "ABCDEFG" and list1[2] in "12345678":
				for a in range(9):
					if chessboard[a][0] == list1[1]:
						x_pos = int(list1[2])
						y_pos = a
						chessboard[y_pos].insert(x_pos, list1[0])
						chessboard[y_pos].pop(x_pos + 1)
						break
			#if the user did not enter the correct information then it will send this error and ask them to do it again		
			else:
				print("\n***ERROR***: You can only use the following Letters within the list provided to you with a comma, then a *CAPITAL* Letter within the chessboard, and a number.")
				break
		#second players choosing
		while y == 1:
			#shows second players options
			print("Now provide the second player's chess pieces.\nThese are second player selections.\n")
			for second in sample_second_player:
				print (second)
				print ()
			#asks the second player what he would like to use and where he would like to place it
			position_2 = input("Second player: what would you like to place down and where, exp = Q, A3\ninsert c to exit: ")
			if position_2 == "c":#if inputed c, then finish
				y +=1
				return chessboard
			list2 = [position_2[0], position_2[-2], position_2[-1]]
			#once selected the object and position, it appends it to the spot and deletes the one infront of it
			if list2[0] in second_player and list2[1] in "ABCDEFG" and list2[2] in "12345678":
				for b in range(9):
					if chessboard[b][0] == list2[1]:
						x_pos_2 = int(list2[2])
						y_pos_2 = b
						chessboard[y_pos_2].insert(x_pos_2, list2[0])
						chessboard[y_pos_2].pop(x_pos_2 + 1)
						break
			#if the user did not enter the correct information then it will send this error and ask them to do it again		
			else:
				print("\n***ERROR***: You can only use the following Letters within the list provided to you with a comma, then a *CAPITAL* Letter, and a number.")
				break			
'''
move_a_piece function takes the current chessboard in use then asks the user what piece it wants to move, asks where they want to move it to, and puts it on the chessboard
@params chessboard 2d list containing the state of a chessboard
@return newly modified chessboard
'''
def move_a_piece(chessboard):
	#gives a warning on if you take a piece and move it ontop of another it will take over that second pieces spot
	print("You have selected move a piece!!\nIn this option you can take any piece on the board and move it wherever you like.")
	print("Be warned that if you take a piece and move it on top of another it will take over that second pieces spot!!")
	while True:
		while True:
			#asks for the location of the chess piece the user would like to move
			location = input("what is the location of the chess piece you would like to move, exp = A3: ")
			location = location.upper()
			if location[0] in "ABCDEFG" and location[-1] in "12345678" and len(location) == 2:#makes sure its inside
				#asks for the new location of where the user would like to move it to
				new_location = input("where would you like to move it to")
				new_location = new_location.upper()
				if new_location[0] in "ABCDEFG" and new_location[-1] in "12345678" and len(new_location) == 2:
					for spot in range(9):
						if chessboard[spot][0] == location[0]:
							break
					#adds a - to the location, and pops out the chess piece		
					chessboard[spot].insert(int(location[-1]), "-")
					popped = chessboard[spot].pop(int(location[-1])+1)
					#looks for where the location would be then inserts the popped value and pops the previous value out
					for new_spot in range(9):
						if chessboard[new_spot][0] == new_location[0]:
							break
					chessboard[new_spot].insert(int(new_location[-1]), popped)
					chessboard[new_spot].pop(int(new_location[-1])+1)
					again = input("would you like to move another piece?, yes/no")
				#if user yes run the program again, and this is me trying to get all possibilities of the user saying yes, there is a way of doing this where I can only ask the user to 					#say yes or no but I feel like this will make the program quicker. the way is making an if for yes and elif for no and then adding an else for anything else and that 					#anything else would just have an error telling the user to enter specifically 'yes' or 'no
					if again in "yesYESyaYAYesYa":
						break
					else:
						return chessboard
				else:
					#gives error when user does  not enter the correct information
					print("\n***ERROR***: You can only use the following letters between A-H, numbers between 1-8, and must have 1 letter and 1 integer, exp = A3")
					break
					
			else:
				#gives error when user does  not enter the correct information
				print("\n***ERROR***: You can only use the following letters between A-H and numbers 1-8, exp = A3")
				break
'''
score function takes the chessboard given breaks it down to check everypiece inside, if its a player 1 piece find its value, then add it to the player 1 score, and do some for the player 2 peices. Once done check who has the greater score and print who is winning
@params chessboard 2d list containing the state of a chessboard
@return none
'''
def score(chessboard):
	#making variables for the code
	data = []
	fp_score = 0
	sp_score = 0
	value = [0, 10, 5, 3.5, 3, 1]
	first_player = ["K", "Q", "R", "N", "B", "P"]
	second_player = ["k", "q", "r", "n", "b", "p"]
	#making data a 3d list containing the first player characters, second player characters, and the value for both 
	for jk in range(6):
		data.append([first_player[jk], second_player[jk], value[jk]])
	#searches through the chessboard and finds characters of first and second player and then adds them to a score sheet
	for number_data in chessboard:
		for i in number_data[1:]:#[1:] is used to ignore the ABCDEFGH at the beggining of each row because it can inflict with the score
			
			for lol in range(6):
				if i in data[lol]:
					if i == data[lol][0]:
						fp_score += data[lol][2]
						break
					elif i == data[lol][1]:
						sp_score += data[lol][2]
						break
	#if statments used to give the score back to the user
	if fp_score > sp_score:
		print("First player has a score of,",fp_score,"\nWhile second player has a score of,", sp_score, "\nTherefore First player is currently winning.")
	elif sp_score > fp_score:
		print("Second player has a score of,", sp_score,"while First player has a score of,", fp_score, "\nTherefore Second player is currently winning.")
	elif fp_score == sp_score:
		print("Both scores are the same at the moment\nFirst players score: ", fp_score, "\nSecond players score: ", sp_score,)
'''
check is a function reponsible for checking if the option that the user made was not one of the options showed. This was created by me to make the program keep running if somebody accidently pressed enter or something that was not one of the options by accident at the start, so it would not crash
@params none
@return if the users option was correct then it will return the users option, if not the program will run again and they can try again
'''
def check():
	#asks for user input 
	user_input = input("Select an option: ")
	#checks to see if the user inputed something within the range of the options
	for ad in range(1,6):
		if str(ad) == user_input:
			return int(user_input)
	#gives an error when user inputs something that is not valid
	print("\n***ERROR***: You can only insert integers between 1 and 5.\n")
	return "_"
'''
about function prints out what the program does with some instructions
@params none
@return none
'''
def about():
	#prints everything that the user needs to know about this program
	print("\nThis program was designed to find out who is winning in a chess game based off of the chess pieces on the board.")
	print("Please pick any options that are listed below and further instructions will be given.\n")
'''
print_chessboard function takes the list of the current chessboard and prints it out as 2d string
@params chessboard 2d list containing the state of a chessboard
@return none
'''
def print_chessboard(chessboard):
	string = ""
	for data in chessboard:
		
		for i in data:
			string += i
		string += "\n"
	print(string)











main()
