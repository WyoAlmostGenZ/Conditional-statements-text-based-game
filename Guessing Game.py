import time

print("Welcome to The Treasure island which way do u wish to go \n")
time.sleep(2)


left_or_Right = input("LEFT/RIGHT\n").lower()
if left_or_Right == "LEFT".lower():
	Swim_or_wait = input("SWIM/WAIT\n").lower()
	if Swim_or_wait == "WAIT".lower():
		Door = input("Which Door do u wish to enter\nBLUE/YELLOW/RED\n").lower()
		if Door == "YELLOW".lower():
			print("YOU WIN !!")
		elif Door == "BLUE".lower():
			print("Eaten by Efreet , Game Over")
		elif Door == "RED".lower():
			print("Burned by fire , Game Over")
		else:
			print("Game Over.")
	else:
		print("A giant trout ate you. You Lose !")
else:
	print("You feel into a hole, You Lose")
