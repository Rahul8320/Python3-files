print("\t * Welcome to Guess The Number Games * ")

import random

name = input("Hey! what is your name >> ")

secrete_num = random.randint(1,20)
print("I guess my number in between 1 to 20.")
print("Now, your trun :) ")
count = 0
chance = 3

while chance>0:
	print(f"{name}, You have only {str(chance)} chances. Good Luck!")
	num = int(input("Guess me >>>   "))
	count += 1
	chance -= 1
	if num == secrete_num:
		print(f"{name},You Guess the Number at {str(count)} guesses!")
		print(f"[*] Welldone {name}! You win the Game.")
		break
	elif num > secrete_num:
		print ("OK! I give you a hint!")
		print("You Guess greater Number!")
	elif num < secrete_num:
		print ("OK! I give you a hint!")
		print("You Guess smaller Number!")
	

else:
	print(f"[*] Sorry {name}! You loose the Game.")
	print(f"[*] My Guess number is {secrete_num}")
