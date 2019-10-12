#This game is to be run in Python 3, preferably using the Command Line for best performance.
print "\t\t\t\t\t\tWELCOME TO THE GAME OF MINDS"
print "***********************************************************************************************************************"
print "Following are the rules of the game:"
print "\t 1. The players can chose to start first or second"
print "\t 2. The player with first turn has to start from 1."
print "\t 3. The player has to input either 1 , 2 or 3 consecutive values that come after the ongoing number"
print "\t 4. The game will continue till 21 is readched and whoever enters 21 at the end loses."
print "\t 5. As soon as any rule is broken the game will be stopped and the player who violates the rule loses."

def nearest_multiple(num):
	if num >= 4:
		near = num + (4 - (num % 4))
	else:
		near = 4
	return near


		
def lose1(name):
	print "\n\n"
	print name,
	print ", YOU LOSE!"
	print "\n\n*****************************************************************************************************************"
	exit(0)

def check(xyz):
	i = -len(xyz)
	#print i
	if i == 0:
		return True
	elif i == -1:
		return True
	else:
		while i < -1:
			if xyz[i] - xyz[i + 1] == -1:
				ch = True
			else:
				ch = False
			i = i + 1
	return ch

def start1(name):
	xyz = []
	last = 0
	print "Enter 'Y' if you'd like to go first."
	print "Enter 'N' if you'd like to go second."
	chance = raw_input('> ')
	if chance == "Y":
		while True:
			if last == 20:
				lose1(name)
			else:
				print name,
				print ", your turn."
				print "How many numbers do you wish to enter? Please be sensible and enter either 1, 2, or 3."
				input = int(raw_input('> '))
				if input > 0 and input <= 3:
					comp = 4 - input
				else:
					print "You'd better learn counting first. Goodbye!!"
					lose1(name)
		
				i = 1
				j = 1
				print "Enter the values. Again, sensibility is mandatory."
				while i <= input:
					xyz.append(int(raw_input('> ')))
					i = i + 1
				last = xyz[-1] #store the last element of xyz.
				if check(xyz) == True:
					if last == 21:
						lose1(name)
					else:
						print "Computer's turn."
						while j <= comp:
							xyz.append(last + j)
							j = j + 1
						print "This is what you entered:"
						print xyz
						last = xyz[-1]
				else:
					print "\nYou did not input consecutive integers."
					print "Goodbye, loser!!."
					lose1(name)
	elif chance == "N":
		comp = 1
		last = 0
		while last < 20:
			print "Computer's turn"
			j = 1
			while j <= comp:
				xyz.append(last + j)
				j = j + 1
			print xyz
			if xyz[-1] == 20:
				lose1(name)
				
			else:
				print name,
				print ", your turn."
				print "How many numbers do you wish to enter?"
				input = int(raw_input('> '))
				i = 1
				print "Enter your values"
				while i <= input:
					xyz.append(int(raw_input('> ')))
					i = i + 1
				last = xyz[-1]
				if check(xyz) == True:
					print xyz
					near = nearest_multiple(last)
					comp = near - last
					if comp == 4:
						comp = 3
					else:
						comp = comp
				else:
					print "\nYou did not input consecutive integers."
					print "You are disqualified from the game."
					lose1(name)
		print "\n\nCONGRATULATIONS!!!"
		print name,
		print "WINS!"
		print "\n\n*****************************************************************************************************************"
		exit(0)
		
	else:
		print "wrong choice"
		exit(0)
			
		
			
		
def start2(name1, name2):
	abc = []
	
	while True:
		if check(abc) == True:
			print name1,
			print ", your turn."
			print "How many numbers do you wish to enter?"
			input1 = int(raw_input('> '))
			if input1 > 0 and input1 <= 3:
				i = 1
				print "Enter your values:"
				while i <= input1:
					abc.append(int(raw_input('> ')))
					i = i + 1
				last = abc[-1]
				print "The order of inputs is as follows:"
				print abc
				if last == 21:
					lose(name1)
				else:
					if check(abc) == True:
						print name2,
						print ", your turn"
						print "How many numbers do you wish to enter?"
						input2 = int(raw_input('> '))
						if input2 > 0 and input2 <= 3:
							j = 1
							print "Enter your values:"
							while j <= input2:
								abc.append(int(raw_input('> ')))
								j = j + 1
							last = abc[-1]
							print "The order of inputs is follows:"
							print abc
							if last == 21:
								lose(name2)
							else:
								continue
							
						else:
							print "\nWrong input."
							print name2,
							print ", you are disqualified from the game."
							lose1(name2)
					else:
						print "\nPlayer 1 did not input consecutive integers."
						print name1,
						print ", you are disqualified from the game."
						lose1(name1)
			else:
				print "\nWrong input"
				print name1,
				print ", you are disqualified from the game."
				lose1(name1)
		else:
			print "\nPlayer 2 did not input consecutive integers."
			print name2,
			print ", you are disqualified from the game."
			lose1(name2)
	
		
game = True		
while game == True:
	print "\nEnter the number of players:"
	player = raw_input('> ')
	if player == "1":
		print "Enter the name of Player 1: "
		name = raw_input('> ')
		print "Player 2 is Computer."
		print name,
		print ", click 'SPACEBAR' to start the game"
		if raw_input('> ') == " ":
			start1(name)
		else:
			print "Do you want quit the game?(yes / no)"
			next = raw_input('> ')
			if next == "yes":
				print "You are quitting the game..."
				exit(0)
			elif next == "no":
				print "Continuing..."
			else:
				print "Sorry I could not get that."
				exit(0)
		
	elif player == "2":
		print "The player who wants the first chance enters the name first."
		print "Enter the name of Player 1:"
		name1 = raw_input('> ')
		print "Enter the name of Player 2:"
		name2 = raw_input('> ')
		print "Press 'spacebar' to start the game."
		if raw_input('> ') == " ":
			start2(name1, name2)
		else:
			print "Do you want quit the game?(yes / no)"
			next = raw_input('> ')
			if next == "yes":
				print "You are quitting the game..."
				exit(0)
			elif next == "no":
				print "Continuing..."
			else:
				print "Sorry I could not get that."
				exit(0)
	else:
		print "More than two players are not allowed."
		exit(0)
