yourname = input("Enter your name to continue: ")
print("Welcome, " + yourname + ".")
print("I will import some Python code from my Pythonroom account, just to have some fun :]")
print("Project 1:")
print("Conditionals With Cards")
codeContinue = True
while codeContinue = True:
print("This document started out as a regular conditionals lesson in my school.")
print("But then, my dad wanted me to make it a real python piece of code.")
print("This was the conditional: if(card drawn is greater than 6) then(give person who drew card 1 point else give other player(s) one point each).")
print("My dad and I worked together to create this document, which does exactly the conditional listed above.")

'''NOTE: The code below may not work, so I may need to adjust it, because recently Pythonroom got acquired by Tynker, so I think some
mechanics of Pythonroom may be different from other Python environments.'''

import random #This line of code imports the "random" module from the Python Modules


#Lines 10 and 11 define a variable to equal the integer "0" (Note: In Python, you do not need to create variables, meaning you can just type the name of the variable, and assign it a value
playerOneScore = 0
playerTwoScore = 0
#Line 13 includes the input function, which asks a string (A string is symbols and letters surrounded by double quotes), and then waits for an answer, which can be stored in a variable
playerOneName = input("What is Player 1's name?")
playerTwoName = input("What is Player 2's name?")
playerOne = playerOneName
playerTwo = playerTwoName

s1 = playerOneName.title() #The title function capitalizes the first letter of the first word
s2 = playerTwoName.title() 
whoIsPlaying = playerOne

continueGame = True #True is self-explanatory

while (continueGame): #This is a loop (explained further in FCOGamingIdiots's video "Python Coding Part 1: Conditionals")
	cardValue = random.randint(1, 13) #We are defining a variable and giving it a value of a random number from 1 - 13
	if(cardValue > 6):
		if(playerOne == whoIsPlaying):
			playerOneScore = playerOneScore + 1
		elif(playerTwo == whoIsPlaying):
			playerTwoScore = playerTwoScore + 1
	elif(cardValue < 6):
		if(playerOne == whoIsPlaying):
			playerTwoScore = playerTwoScore + 1
		elif(playerTwo == whoIsPlaying):
			playerOneScore = playerOneScore + 1
		
	print("The card drawn by %s is %d" % (whoIsPlaying, cardValue))
	stopOrRun = input("Do you want to keep on playing (Yes or No)?")
	if(stopOrRun == "No"):
		continueGame = False
		if(playerOneScore > playerTwoScore):
			print("%s is the winner!" % (s1))
		elif(playerTwoScore > playerOneScore):
		    print("%s is the winner!" % (s2))
		elif(playerOneScore == playerTwoScore):
			print("Both %s and %s are the winners!" % (playerOneName, playerTwoName))
		print("So %s got %d points and %s got %d points" % (s1, playerOneScore, s2, playerTwoScore))	
	else:
		continueGame = True
		if(whoIsPlaying == playerOne):
			whoIsPlaying = playerTwo
		elif(whoIsPlaying == playerTwo):
			whoIsPlaying = playerOne
continueCodeOne = input("Congratulations! You just finished my first project! Want to continue? Type, 'Yes,' or, 'No,': ")
if continueCodeOne = "Yes" or "yes":
    	print("Okay then, continue!")
elif continueCodeOne = "No" or "no":
    	codeContinue = False
print("Time to move on to the second project!")
print("Project 2: Dad's Python Code Compilation")
print("Hey guys! Wanna have some neat pieces of code displayed?")
print("Well, if you do, this is the place to be!")
yourname = input("First, what is your name?")
print("Welcome to this document, " + yourname + ", which will be edited by me and Perusworld")

print("Now here are some neat pieces of code, created by Perusworld")
#The name of this file is "Exponents: By Perusworld (A.K.A my dad) (Some of the strings may be edited for the sake of formality)
def powerOf(base, exponent):
	number = 1
	for counter in range (1, exponent + 1):
		number = number * base
	return number

base = int(input('Enter a base to the right:'))
exponent = int(input('Enter an exponent to the right:'))

print('Using the data you provided, the value of ' + str(base) + ' to the power of ' + str(exponent) + ' is ' + str(powerOf(base, exponent)))
print('How was that? Let\'s do another one, made by Perusworld, again')
#The name of this file is "Multiplication Table: By Perusworld
print("Have you ever wanted to find out all the facts for one number? Type one number in, and the code will give you the facts!")
def printMultiplicationTable(fornumber):
	print ('The facts for ' + str(fornumber) + ' are:')
	for index in range (1, 100):
		print(str(index) + ' * ' + str(fornumber) + ' = ' + str(index * fornumber))

fornumber = int(input('Enter the number to print the multiplication table for: '))
printMultiplicationTable(fornumber)

print("Ready for one more piece of code, again, made by Perusworld? (FYI: I have no idea what the following code is going to do)")
#The name of this file is "Functions: By Perusworld"
def printCounter(till):
	print('Now i am going to print counter for number ' + str(till))
	for count in range (1,till+1):
		print(count)
		
def insanePrintCounter(till):
	for count in range (1, till+1):
		printCounter(count)

print('What do you want to print')
print('Type 1 for printCounter')
print('Type 2 for insanePrintCounter')
whattodo = input('Enter your choice (1 or 2) :')
endnumber = int(input('Enter the number you want to print till :'))
if whattodo == '1':
	printCounter(endnumber)
elif whattodo == '2':
	insanePrintCounter(endnumber)
else:
	print('Dude i told you 1 or 2 :-(')
continueCodeTwo = print("End of Project 2! Just one more to go! Would you like to continue? ")
if continueCodeTwo = "Yes" or "yes":
    print("Well, go ahead, dude!")
elif continueCodeTwo = "No" or "no":
	codeContinue = False
print("Project 3: I like to code like a SAVAGE (lol).")
import time

print("Hi! I'm back with another Python code (and this time I am not taking exerts from Perusworld) and I just wanted to share it with you guys.")
print("As I always do, please kindly write your name.")
name = input("Name: ")
print("Now I hope that this password thing works, so yeah, enter a password to look at this document (I hope it works).")
password = input("Enter the password: ")
if password != "":
	print("Okay you are let in! (P.S. '" + password + "' is not the password).")
print("Hi, " + name + ".")
print("Now, I definetaly am not a pro at coding, so my coding will be lamer than Perusworld's (unless I use a Python book) :/.")
print("Just a note before you start, the first answer is when I put the first number you entered after the second number to calculate the answer, while the second answer is when I put the second number you entered after the first number before putting the symbol in the middle (so there will be different results for the difference and quotient section).")
print("Well, just to start off, enter two numbers below.")
rightsumnum1 = input("Enter a number: ")
rightsumnum2 = input("Enter another number: ")
rightsum = int(rightsumnum1) + int(rightsumnum2)
print("The sum of those random numbers you gave (I think it is " + str(rightsumnum1) + " and " + str(rightsumnum2) + ") is " + str(rightsum) + ".")
reversesumnum1 = input("Enter a number: ")
reversesumnum2 = input("Enter another number: ")
reversesum = int(reversesumnum1) + int(reversesumnum2)
print("The sum of those random numbers you gave (I think it is " + str(reversesumnum1) + " and " + str(reversesumnum2) + ") is " + str(reversesum) + ".")
print("Ready for more? Just tell me below (Say Yes or No).")
doYouWantToContinue = input("Would you like to continue? ")
if doYouWantToContinue == "No":
	print("Okay then, go do something else.")
	plsansweragain = input()
	if plsansweragain != "":
		print("Okay fine, you can continue.")
	
elif doYouWantToContinue == "Yes":
	print("Okay, let's continue!")
		
rightdifferencenum1 = input("Enter a number: ")
rightdifferencenum2 = input("Enter another number: ")
rightdifference = int(rightdifferencenum1) - int(rightdifferencenum2)
print("The difference of those random numbers you gave (Okay now I got the hang of it I know your numbers) is " + str(rightdifference) + ".")
reversedifferencenum1 = input("Enter a number: ")
reversedifferencenum2 = input("Enter another number: ")
reversedifference = int(reversedifferencenum1) - int(reversedifferencenum2)
print("The difference of those random numbers you gave (Okay now I got the hang of it I know your numbers) is " + str(reversedifference) + ".")
print("Wanna continue (Yeah I'm gonna ask this every single time just get with the flow)? Just tell me below (Say Yes or No).")
doYouWantToContinue = input("Would you like to continue?")
if doYouWantToContinue == "No":
	print("Okay then, go do something else.")
	plsansweragain = input()
	if plsansweragain != "":
		print("Okay fine, you can continue.")
	
elif doYouWantToContinue == "Yes":
	print("Okay, let's continue!")
		
print("Did you know python could calculate the product and quotient of two numbers? (gasp) <<<That is a sarcastic gasp.")
print("Just a word of caution: If there is a remainder when dividing, Python only prints out the whole number and ignores the remainder :/.")
print("Also, if the first number is smaller than the second number on the first answer for the quotient part, that is because Python does not support decimal numbers (at least the code I am using doesn't support decimal numbers) :/.")
rightproductnum1 = input("Enter a number: ")
rightproductnum2 = input("Enter another number: ")
rightproduct = int(rightproductnum1) * int(rightproductnum2)
print("The product is " + str(rightproduct) + ".")	
reverseproductnum1 = input("Enter a number: ")
reverseproductnum2 = input("Enter another number: ")
reverseproduct = int(reverseproductnum1) * int(reverseproductnum2)
print("The product is " + str(reverseproduct) + ".")
print("Ready for more? Just tell me below (Say Yes or No).")
doYouWantToContinue = input("Would you like to continue?")
if doYouWantToContinue == "No":
	print("Okay then, go do something else.")
	plsansweragain = input()
	if plsansweragain != "":
		print("Okay fine, you can continue.")
	
elif doYouWantToContinue == "Yes":
	print("Okay, let's continue!")
rightquotientnum1 = input("Enter a number: ")
rightquotientnum2 = input("Enter another number: ")
rightquotient = int(rightquotientnum1) / int(rightquotientnum2)
print("The quotient is " + str(rightquotient) + ".")
reversequotientnum1 = input("Enter a number: ")
reversequotientnum2 = input("Enter another number: ")
reversequotient = int(reversequotientnum1) / int(reversequotientnum2)
print("The quotient is " + str(reversequotient) + ".")
print("Ready for more? Just tell me below (Say Yes or No).")
doYouWantToContinue = input("Would you like to continue?")
if doYouWantToContinue == "No":
	print("Okay then, go do something else.")
	plsansweragain = input()
	if plsansweragain != "":
		print("Okay fine, you can continue.")
	
elif doYouWantToContinue == "Yes":
	print("Okay, let's continue!")
print("WHEW! Okay finally I can take a break (wait how can I take a break when I have to type all the time?")
print("Okay let me just take a break and let you sit here.")
print("LOL why would I just leave you here of course I will continue!")
print("Let's see... What would a good coder write?")
print("OH YEAH! The for loop! I almost forgot (literally I almost forgot while I was coding this).")
thethingyouwanttoprintfivehundredtimes = input("Enter something that you want to be printed 500 times: ")
for x in range (1, 500):
	print(thethingyouwanttoprintfivehundredtimes)
codeContinue = False
print("Phew! Did that last piece of code wreck your page? If not, then you're free to go!")
print("Thanks for viewing my latest Python code on GitHub!")
print("Bye!")



	

    	
	    
