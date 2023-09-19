#Gets user input
user_bin_input = input("Input a maximum 8 digit binary number: ")

#This bool will be what tracks if it is actually a binary number
pure_bin = False

while len(user_bin_input) > 8 or pure_bin == False: #If either length or charcters are not what we want we enter the loop
	while len(user_bin_input) > 8: #If the length is over 8 we tell them to input a new number
		print("Your input is too long, try again!")
		user_bin_input = input("Input a maximum 8 digit binary number: ")
	while pure_bin == False: #This is where the program defaults since pure_bin is False at the start
		if set(user_bin_input) <= {'0','1'}: #If the set of all characters in user_bin_input is a subset of the 0 and 1 set its a binary number
			pure_bin = True #If the first input was correct this is where the program defaults
		else:
			print("Your input is not a binary number, try again!") #Tell them to do it again
			user_bin_input = input("Input a maximum 8 digit binary number: ")

def bin_to_dec(binary_string: str) -> int: #This indicates the output of this should be an integer
	#The final output
	finalOutput = 0
	for exponent, char in enumerate(reversed(binary_string)):
		finalOutput += (char=='1')*(2**exponent) #The thing we're printing out will have 2^exponent added to it, exponent is the number in the string (using the start at 0 rule)
	return finalOutput #This makes the output of the function equal whatever finalOutput is

#Prints out final answer
print("Your answer in decimal is: " + str(bin_to_dec(user_bin_input)))