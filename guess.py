import random
import time

print("Welcome to this Guessing game prototype!")
time.sleep(1)
print("I will think of an animal and you have figure out which one I picked!")
time.sleep(2)
print("Shall we start?")

player = None
compick = random.choice(["dog","cat","penguin","goat","elephant","monkey","gorilla","bear","wolf","horse","tiger","lion","pig"])
time.sleep(2)
print("Okay, I have my pick.")

while True:
	player = input("Please enter your best guess (or quit with 'q'): ").lower()
	comrep = random.choice(["Not really, try again!","Well, that's not it...","Nope, try another animal!","Close, but so far away...","No, try again!"])
	if player:
		if player == compick:
			print("Congrats! You have guessed it! Well played!")
			break
		elif player == 'q':
			print("Thanks for playing. Bye!")
			break
		else:
			print(comrep)
	else:
		print("You have to enter something, mate...")
