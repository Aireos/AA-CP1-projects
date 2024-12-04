nospace = ""
onespace = " "

while True:
    full_name = input("What is your full name?: ")
    try:
        full_name = int(full_name)
        print("your name cannot have numbers in it.")
        continue
    except:
        if not ' ' in full_name:
            print("you need a first and last name. (type none for last name if you don't have one.)")
            continue
        break

firstname, lastname = full_name.split(" ")
firstname = firstname.capitalize()
lastname = lastname.capitalize()

if 'None' == lastname:
    random_lastname_number = random.randint(1,8)
    if random_lastname_number == 1:
        lastname = "Hilton"
        full_name = firstname + " " + lastname
    if random_lastname_number == 2:
        lastname = "West"
        full_name = firstname + " " + lastname
    if random_lastname_number == 3:
        lastname = "Hope"
        full_name = firstname + " " + lastname
    if random_lastname_number == 4:
        lastname = "Lopez"
        full_name = firstname + " " + lastname
    if random_lastname_number == 5:
        lastname = "Dawson"
        full_name = firstname + " " + lastname
    if random_lastname_number == 6:
        lastname = "Pierce"
        full_name = firstname + " " + lastname
    if random_lastname_number == 7:
        lastname = "Ashford"
        full_name = firstname + " " + lastname
    if random_lastname_number == 8:
        lastname = "Spade"
        full_name = firstname + " " + lastname
    

print("Welcome,", full_name + ", to the island of Merina")
armor = 0
ring = 0
weapon = 0
# Import random
import random
# Ogre stats list
#                              dmg  hth arm
Ogre_stats = [random.randint(13,18), 20, 0]
# User base stats list
User_stats = [11 + weapon, 11 + ring, 11 + armor]
# Contestants list that will include ten contestants of differing strengths.
Contestants = [[random.randint(25,30), 8, 8, "Archer"],[random.randint(12,17), 13, 13, "Warriar"],[random.randint(9,14), 30, 16, "Palidin"],[random.randint(15,30), 10, 10, "Spear-weilder"],[random.randint(10,20), 9, 14, "Rogue"],[random.randint(12,24), 11, 8, "Wizard"],[random.randint(5,30), 10, 9, "Barbarian"],[random.randint(12,16), 20, 18, "Dwarf"],[random.randint(10,15), random.randint(12,21), 10, "Bard"],[18, 18, 18, "Champion"]]
# a item list for the blacksmith
blacksmith_list = [["Armor (+1)", 10, 1, 1], ["Armor (+2)", 20, 2, 1], ["Armor (+3)", 30, 3, 1], ["Armor (+4)", 40, 4, 1]]
# a item list for the ring shop
ring_list = [["Ring (+1)", 10, 1, 2], ["Ring (+2)", 20, 2, 2], ["Ring (+3)", 30, 3, 2], ["Ring (+4)", 40, 4, 2]]
# a item list for the shop in the arena
arena_list = [["Weapon (+1)", 10, 1, 3], ["Weapon (+2)", 20, 2, 3], ["Weapon (+3)", 30, 3, 3], ["Weapon (+4)", 40, 4, 3]]
# an item list for the traveling trader’s shop.
blacksmith_list = [["Armor (+1)", 10, 1, 1], ["Ring (+1)", 10, 1, 2], ["Weapon (+1)", 10, 1, 3]]
# chance function that will be used whenever there is a chance an event occurs.
def chance(percent):
    if (random.randint(1,percent)) == 1:
        return True
    else:
        return False
# battle function that will check who wins based on their three stats.
# function for shops so that it is easy to make all the shops work
# Print the statement: “Welcome to the island of Merina”
# While the variable game_end is equal to false
# input asking if they want to go up, down, left, or right
# if statement for up
# A while true statement
# print the statement: “You are now in the town square.”
# input statement asking if they want to go to the blacksmith, bank, or grocery.
# if statement for Blacksmith
# Run the shop function with the item list for the blacksmith
# Break
# If statement for grocery
# While true statement
# Input asking if they want health items/food or stat-increasers/potions
# If statement for food
# Run the shop function with the item list for the grocery
# Break
# If statement for potions
# Run the shop function with the item list for the potion grocery
# Break
# otherwise/else statement
# Print that they had a invalid input and they should enter potions or food
# Continue
# If statement for bank
# While true statement
# Print a list of all their items
# Input asking what they want to sell
# If the item is in the list of all their items
# Sell item
# While true statement
# Input asking if they want to sell something else
# If  they say no, break
# If they say yes, continue
# Else it should say invalid input and continue
# Else it should print invalid input and continue
# Break
# Else it should say invalid input and continue
# Break








# If statement for down
# 	A while true statement
# 		Print a statement saying that they have gone onto a trial
# 		Input asking at a trail split to go down a sandy trail or a rocky one
# 		If input for sandy
# 			While True statement
# 				Input asking if you want to go to a strange man on the beach or wander around admiring the beauty.
# 			If the input is the man
# 				If you have crystals
# 					Print saying “he sees the crystals and decides to let you onto his raft for free.”
# 					Print saying “you sail into the horizon looking for your next adventure”
# 					Make variable game_end equal to True
# 					break
# 				If you have two hundred gold
# 					Print saying “he magically takes two hundred gold from you and lets you go on his raft.”
# 					Print saying “you ask why he just stole your gold and he tells you that it was the payment”
# 					Print saying “you sail into the horizon a little disgruntled but happy to get off the island.”
# 					Make variable game_end equal to True
# 					break
# 				Else print that he turns away saying not good enough yet and walks away, then set input to wander

# 		If the input is wander
# 			While True statement
# 			Chance function at 10%
# 			If the chance function is equal to true
# 				Print that they found a shipwreck
# 				Print that the player looked inside and found a secret chest with a +5 armor inside
# 				Print that the player decided to head back to town to celebrate
# 				Break
# 			If the chance function is equal to false
# 						Input saying that they did not find anything but do they want to try again?
# 						If input is equal to true 
# 							Continue
# 						If input is equal to false
# 							Break
# 						Else print invalid input, will count as false, and then break
# 				Else it should say invalid input and continue
# 				Break
# 		If input for rocky
# 			While True statement
# 				Print that they have entered a cave
# 				Chance function at 10%
# 				If chance function is equal to true and tunnel_collapse is equal to false
# 					Print that they found  secret side tunnel
# 					Chance function at 50%
# 					If chance function is equal to true
# 						Print that they found a secret trap and were able to avoid it
# 						Print that they gained crystals from the chest						
# 					If chance function is equal to false
# 						Print that they broke a tripwire and the whole tunnel collapses
# 						Set tunnel_collapse equal to true
# 						break




				
# it should print that they see an ogre
# 				Input asking if they want to run away
# 				If input is equal to true
# 					Break
# 				If input is equal to false
# 						Do fighting function with user and ogre
# 						If win is equal to true
# 							Print that they found a +5 sword
# 							Print that they decided to head back to town after the battle
# 							Break
# 						If win is equal to false
# 							Print that they lost
# 							Break
# 			Else print that it was invalid input and continue
# 			Break
# 	If statement for left
# 		A while True statement
# 			Input asking if they want to go to the stands, betting stand, store or fight.
# 			If input is equal to stands
# 				While true statement
# 					Print that they are watching (name) and (name) fight
# 					Do fighting function for the two of them
# 					Tell user who won
# 					Input asking if they want to watch again
# 					If input is equal to no
# 						Break
# 					If input is equal to yes
# 						Continue
# 					Else print invalid input: will count as yes
# 			If input is equal to betting stand
# 				While true statement
# 					Print that they are watching (name) and (name) fight
# 					User guess input asking who that think will win
# 					Input asking how much they are willing to bet
# 					If input 2 is less then or equal to their money amount
# 						Print that the transaction worked
# 					Else print that they don’t have that much money and continue
# 					Do fighting function for the two of them
# 					If the users guess is correct
# 						Give double gold back
# 					If the users guess is wrong
# 						Tell user that they lost all the gold
# 					Else print that the person they guessed for didn’t exist and give their gold back that they bet
# 					Input asking if they want to bet again
# 					If input equals yes
# 						Continue
# 					If input equals no
# 						Break
# 			If input is equal to the store
# 				Run the shop function with the item list for the arena store




# 			If the input is equal to fight
# 				While True statement
# 				If they have 30 gold 
# 					Print that they are fighting (name)
# 				Else print that they do not have enough money and break
# 				Do fighting function for the two of them
# 				Tell user who won
# 				If user won
# 					Give user 60 gold
# 				If user lost
# 					Have user lose 30 gold
# 				Input asking if they want to fight again
# 				If input is equal to yes
# 					Continue
# 				If input is equal to no
# 					Break
# 		Else print that it was a invalid input and continue
# 		Break
# If statement for right
# 	Print that they have met the traviling merchant and he says hello
# 	While true statement
# 	Input statement asking if they want to Buy anything or work for him
# 	If input is equal to buy anything
# 		Run the shop function with the item list for the traviling trader
# 	If input is equal to work for him
# 		While times working here is at least 1
# 			Tell user that they did hard labor and have used one of their ten times working here
# 			Give user 5 gold
# 			Chance function at 5%
# 			If chance function is true and lockbox found is equal to false
# 				Tell user they found a secret lockbox with 100 gold inside
# 				Input asking user if they want to steal it
# 				If input is equal to true
# 					Lockbox found set to true
# 					Chance function at 50%
# 					If chance function is true
# 						Tell user they got away
# 						Give user 100 gold
# 						Break
# 					Else print that they go caught
# 						Have user lose 50% of all money
# 						Break
# 			If chance function is false	
# 			Ask user if they want to work again right now
# 			If user answer is yes
# 				Continue
# 			If user answer is no 
# 				Break
# 	Else print that it is a invalid input and continue
# 	Break
# Else print that is a invalid input and continue
# Continue
# Print “thanks for playing my game”



