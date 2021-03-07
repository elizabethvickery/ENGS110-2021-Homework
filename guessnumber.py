import random

savedNumeber = random.randint(3,9)

numberOfSteps = 0

userGuess = 0

while(True):
	userGuess = input("Please guess a number in range from 1 to 100.")

	if (savedNumber == userGuess):
		print("You are the winner! after", numberOfSteps, " steps")
		break
	elif(savedNumber > userGuess):
		print("The number is too small.")
		numberOfSteps = numberOfSteps + 1
	else:
		print("The number is too large.")
		numberOfSteps = numberOfSteps + 1
print ("Goodbye")

