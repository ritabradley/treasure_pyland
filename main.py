print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")

if direction.lower() == "left":
	boat_swim = input('''
	You come to a lake. There is an island in the middle of the lake. 
	Type \"wait\" to wait for a boat. Type \"swim\" to swim across.
	''')
	if boat_swim.lower() == "wait":
		which_door = input('''
		You arrive at the island unharmed. There is a house with 3 doors. 
		One red, one yellow, and one blue. Which color do you choose? 
		''')
		if which_door.lower() == "yellow":
			print("You've found the treasure. You win!")
		elif which_door.lower() == "blue":
			print("You're eaten by beasts. Game over.")
		elif which_door.lower() == "red":
			print("You're burned by a fire. Game over.")
		else:
			print("Game over.")
	else:
		print("You're attacked by trout. Game over.")
else:
	print("You fall into a hole. Game over.")
