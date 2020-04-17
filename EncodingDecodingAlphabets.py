''' 
This function will load a text file
@ params file name, the name of the file to be loaded
@ return an uppercase string containing the data read from the file
'''


def load_text(file_name):
	file_hndl = open(file_name, "r")
	file_data = file_hndl.read()
	file_hndl.close()
	return file_data.upper()
'''
This function will save data to a text file
@ params file_name the name of the file to be saved
	 file_data, the data to be written on the file
@ return none
'''

def save_text(file_name, file_data):
	file_hndl = open(file_name, "w")
	file_hndl.write(file_data)
	file_hndl.close()

'''
main function responsible for the functions interface
@params none
@return none
'''

def main():
	current_text = ""
	initial_text = ""
	current_alphabet = ""
	while True:
		print("\n", "Current Text:\t", current_text, "\n", "initial Text:\t", initial_text, "\n")
		print("\t *Options*\n")
		print("1.Load a file\n2.Save a file\n3.Encode\n4.Decode\n5.Input your own text!\n\tAlphabets:\n6.Caeser\n7.Keyword\n8.Cryptogram\n9.Quit\n")
		option = check()
		while True:
			if option == "_":
				break
			elif option == 1:
				filename = input("What is the file name: ")
				initial_text = load_text(filename)
				break

			elif option == 2:
				save_filename = input("what would you like to name your file: ")
				user_saved_file = save_text(save_filename, current_text)
				break
			elif option == 3:
				if initial_text == "" or current_alphabet == "":
					print("\n***ERROR***: You have not picked a Alphabet or forgot to load a file first, please select the option again and retry.\n")
					break
				else:
					current_text = encode(initial_text, current_alphabet)
					break
			elif option == 4:
				if initial_text == "" or current_alphabet == "":
					print("\n***ERROR***: You have not picked a Alphabet or forgot to load a file first, please select the option again and retry.\n")
					break
				else:
					current_text = decode(initial_text, current_alphabet)
					break
			elif option == 5:
				initial_text = input("What would you like to encode or decode: ")
				initial_text = initial_text.upper()
				break
			elif option == 6:
				current_alphabet = caeser_cipher_alphabet(int(input("Enter your shift number: ")))
				break
			elif option == 7:
				current_alphabet = keyword_cipher_alphabet(input("What is your keyword: "))
				break
			elif option == 8:
				current_alphabet = cryptogram_alphabet()
				break
			elif option == 9:
				exit()
'''
encode function responsible encodeing the message that the user has loaded using a certian alphabet
@params string, the message the user would like to encode
	alphabet, the alphabet the user would like to encode in
@return an upper case string containing the encoded message
'''
def encode(string, alphabet):
	string = string.upper()
	general_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	encoded_solution = ""
	length_string = len(string)
	for b in range(length_string):
		for a in range(26):	
			if not string[b] in general_alphabet:
				encoded_solution += string[b]
				break
			elif general_alphabet[a] == string[b]:
				encoded_solution += alphabet[a]
				break
	return encoded_solution
'''
decode function responsible decodeing the message that the user has loaded using a certian alphabet
@params string, the message the user would like to decode
	alphabet, the alphabet the user would like to encode in
@return an upper case string containing the decoded message
'''				
def decode(string, alphabet):
	string = string.upper()
	general_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	decoded_solution = ""
	length_string = len(string)
	for b in range(length_string):
		for a in range(26):	
			if not string[b] in general_alphabet:
				decoded_solution += string[b]
				break
			elif alphabet[a] == string[b]:
				decoded_solution += general_alphabet[a]
				break
	return decoded_solution
'''
keyword_cipher_alphabet function responsible for making a alphabet using the keyword of the users choice
@params string, the keyword that the user would like to use 
@return the keyword cipher alphabet in a list 
'''
def keyword_cipher_alphabet(string):
	general_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	keyword_list = []
	string = string.upper()
	length_string = len(string)
	for b in range(length_string):
		if not string[b] in keyword_list:
			keyword_list.append(string[b])
	both_lists = general_alphabet + keyword_list
	length_bothlists = len(both_lists)
	for i in range(26):
		if not general_alphabet[i] in keyword_list:
			keyword_list.append(general_alphabet[i])
	if " " in keyword_list:
		print("\n***ERROR***: You must enter a single keyword, Exp. Hey, or robert, please select the option again and retry.")
		return "_"
	return keyword_list
'''
caeser_cipher_alphabet function is responsible for making an alphabet by using the integer the user has given and shift the alphabet by that integer
@params shift_number, the amount the user would like the alphabet to be shifted by 
@return the shifted alphaet in a list
'''
def caeser_cipher_alphabet(shift_number):
	general_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	if shift_number > 26 or shift_number < 0:
		shift_number = shift_number % 26
		print(shift_number)
	caeser_alphabet = []
	temporary_list = []
	for g in range(shift_number):
		letter = general_alphabet.pop(0)
		temporary_list.append(letter)
	caeser_alphabet = general_alphabet + temporary_list
	return caeser_alphabet
'''
cryptogram_alphabet function is responsible for creating an alphabet with 26 letters of the english alphabet in any order
@params none
@return the users own personally created alphabet in a list
'''
def cryptogram_alphabet():
	general_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	cryptogram_list = []
	user_alphabet = input("Type the 26 letters of the english alphabet in any order")
	for o in range(10):
		o = str(o)
		if o in user_alphabet:
			print("\n***ERROR***: You can only insert a letters, The alphabet has been set back to the general alphabet, please select the option again and retry.\n")
			return general_alphabet
	user_alphabet = user_alphabet.upper()
	length_user_alphabet = len(user_alphabet)
	if length_user_alphabet == 26:
		for a in range(length_user_alphabet):
			if user_alphabet[a] in cryptogram_list:
				print("\n***ERROR***: You have inserted duplicates. The alphabet has been set back to the general alphabet, please select the option again and retry.\n")
				return general_alphabet
			else:
				cryptogram_list.append(user_alphabet[a])
	else: 
		print("\n***ERROR***: You have inserted more or less than 26 characters. The alphabet is changed back to normal, please select the option again and retry.\n")
		return general_alphabet
	return cryptogram_list
'''
check is a function reponsible for checking if the option that the user made was not one of the options showed. This was created by me to make the program keep running if somebody accidently pressed enter or something that was not one of the options by accident at the start, so it would not crash
@params none
@return if the users option was correct then it will return the users option, if not the program will run again and they can try again
'''
def check():
	user_input = input("Select an option, Exp. 1 = Load a file: ")
	for ad in range(1,10):
		if str(ad) == user_input:
			return int(user_input)
	print("\n***ERROR***: You can only insert integers between 1 and 9.\n")
	return "_"
			

main()

























