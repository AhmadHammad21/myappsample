from random import randint
import time

print("Let's play a game Rock, Paper ,scissors !!")


playerCount = computerCount = 0
playing = False


def rockPaperScissor():
	print("Rock = 1")
	print("Paper = 2")
	print("Scissors = 3")
	global player
	player = int(input("Make a move: "))

def load():
	print("1....")
	time.sleep(1)
	print("2....")
	time.sleep(1)
	print("3!")

def winner():
	global playerCount
	global computerCount

	computer = randint(1, 3)
	
	if computer == 1:
		print("Computer threw rock!")
	elif computer == 2:
		print("Computer threw paper!")
	else:
		print("Computer threw scissors!")	

	if computer == player:
		print("Tie Game")
	elif abs(computer - player) == 1:
		if computer > player:
			print("The computer laughs as you realise you have been defeated")
			computerCount += 1
		else:
			print("You win !!")
			playerCount += 1
	else:
		if computer < player:
			print("The computer laughs as you realise you have been defeated")
			computerCount += 1
		else:
			print("You win !!")
			playerCount += 1


def bye():
	print("Thank you for playing our game.")
	print("High Scores:")
	print("Player: ", playerCount) 
	print("Computer: ", computerCount) 

while True:
	rockPaperScissor()
	load()
	winner()
	again = input("Would you like to play again? (y/n): ")
	if again == "y":
		print("Next round...")
	else:
		bye()
		break



