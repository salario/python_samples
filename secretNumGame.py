import random
secretNumber = random.randint(1, 100)
print('I\'m thinking of a number between 1 and 100. You have 8 tries to guess the correct number.')

for guessesTaken in range(1, 8):
	print('Take a guess.')
	guess = int(raw_input())
	
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high.')
	else:
		break

if guess == secretNumber:
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('You suck at life! The number I was thinking of was ' + str(secretNumber))