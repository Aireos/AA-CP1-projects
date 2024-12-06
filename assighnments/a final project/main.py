import random
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
    if random_lastname_number == 2:
        lastname = "West"
    if random_lastname_number == 3:
        lastname = "Hope"
    if random_lastname_number == 4:
        lastname = "Lopez"
    if random_lastname_number == 5:
        lastname = "Dawson"
    if random_lastname_number == 6:
        lastname = "Pierce"
    if random_lastname_number == 7:
        lastname = "Ashford"
    if random_lastname_number == 8:
        lastname = "Spade"
    
full_name = firstname + " " + lastname
print("Welcome,", full_name + ", to the island of Merina")
armor = 0
ring = 0
weapon = 0
gold = 1000
items = []

# Ogre stats list
#                              dmg  hth arm
Ogre_stats = [random.randint(12,18), 20, 15, "Ogre"]

# User base stats list
User_stats = [11 + weapon, 11 + ring, 11 + armor, full_name]

# Contestants list that will include ten contestants of differing strengths.
Contestants = [[random.randint(25,30), 8, 8, "Archer"],[random.randint(12,17), 13, 13, "Warriar"],[random.randint(9,14), 30, 16, "Palidin"],[random.randint(15,30), 10, 10, "Spear-weilder"],[random.randint(10,20), 9, 14, "Rogue"],[random.randint(12,24), 11, 8, "Wizard"],[random.randint(5,30), 10, 9, "Barbarian"],[random.randint(12,16), 20, 18, "Dwarf"],[random.randint(10,15), random.randint(12,21), 10, "Bard"],[18, 18, 18, "Champion"]]

# a item list for the blacksmith
blacksmith_list = [["Armor(+1)", 10, 1, 1], ["Armor(+2)", 20, 2, 1], ["Armor(+3)", 30, 3, 1], ["Armor(+4)", 40, 4, 1]]

# a item list for the ring shop
ring_list = [["Ring(+1)", 10, 1, 2], ["Ring(+2)", 20, 2, 2], ["Ring(+3)", 30, 3, 2], ["Ring(+4)", 40, 4, 2]]

# a item list for the shop in the arena
arena_list = [["Weapon(+1)", 10, 1, 3], ["Weapon(+2)", 20, 2, 3], ["Weapon(+3)", 30, 3, 3], ["Weapon(+4)", 40, 4, 3]]

# an item list for the traveling trader’s shop.
trader_list = [["Armor(+1)", 10, 1, 1], ["Ring(+1)", 10, 1, 2], ["Weapon(+1)", 10, 1, 3]]


# chance function that will be used whenever there is a chance an event occurs.
def chance(percent):
    if (random.randint(1,percent)) == 1:
        return True
    else:
        return False
    

# battle function that will check who wins based on their three stats.
# 1 output = player1 won, 2 output = player2 won, 3 = it was a tie
def battle(player1,player2):
    player2health = player2[1] - (player1[0] - player2[2])
    player1health = player1[1] - (player2[0] - player1[2])
    if player1health <= 0:
        if player2health <= 0:
            if player2health > player1health:
                print(player2[3], "won!")
                return 2
            if player1health > player2health:
                print(player1[3], "won!")
                return 1
            else:
                print("It was a tie!")
                return 3
        print(player2[3], "won!")
        return 2
    if player2health <= 0:
        print(player1[3], "won!")
        return 1
    else:
        while True:
            player2health = player2health - (player1[0] - player2[2])
            player1health = player1health - (player2[0] - player1[2])
            if player1health <= 0:
                if player2health <= 0:
                    if player2health > player1health:
                        print(player2[3], "won!")
                        return 2
                    if player1health > player2health:
                        print(player1[3], "won!")
                        return 1
                    else:
                        print("It was a tie!")
                        return 3
                print(player2[3], "won!")
                return 2
            if player2health <= 0:
                print(player1[3], "won!")
                return 1
            else:
                continue


# function for shops so that it is easy to make all the shops work
def shop(shoplist, gold, items):
    print("current gold:", gold)
    while True:
        for list in shoplist:
            print(list[0], "costs:", list[1])
        wanted_item = str(input("What one of these items do you want? if you want to leave type (leave), write full name, example: Armor(+1): "))
        for list in shoplist:
            if wanted_item == list[0]:
                if list[1] <= gold:
                    gold -= list[1]
                    items += [list]
                    print("Item bought, leftover gold:", gold)
                    return gold, items
                else:
                    print("Too expensive!")
                    shop_choice = input("do you wish do leave (yes) or type anything else to buy somthing else: ")
                    if shop_choice == "yes":
                        return gold, items
                    else:
                        continue
        if wanted_item == "leave":
            return gold, items
        else:
            print("That item does not exist!")
            continue
tunnel_collapse = False
game_end = False
crystals = False
shipwreck_found = False
directions = ["do you want to go", "up,", "down,", "left,", "or", "right?: "]
# While the variable game_end is equal to false
while game_end == False:
# input asking if they want to go up, down, left, or right
    direction_choice = input(onespace.join(directions))
# if statement for up
    if direction_choice == "up":
# print the statement: “You are now in the town square.”
        print("Welcome to the town square.")
# A while true statement
        while True:
# input statement asking if they want to go to the blacksmith, bank, or grocery.
            town_square_decicion = input("Do you want to go to the blacksmith, bank, or the ring shop?: ")
# if statement for Blacksmith
            if town_square_decicion == "blacksmith":
# Run the shop function with the item list for the blacksmith
                gold, items = shop(blacksmith_list, gold, items)
# If statement for grocery
            if town_square_decicion == "ring shop":
# Run the shop function with the item list for the potion grocery
                gold, items = shop(ring_list, gold, items)
# If statement for bank
            if town_square_decicion == "bank":
# While true statement\
                found_bank_item = False
                print()
                while True:
                    for item in items: print(item[0])
# Input asking what they want to sell
                    bank_input = input("do you want to sell any of the items above at 1/2 buy cost? (write no if you don't want to sell anything): ")
# If the item is in the list of all their items
# Sell item
                    for item in items:
                        if bank_input == "no":
                            found_bank_item = True
                            break
                        if bank_input == item[0]:
                            print("Item sold")
                            if item[1] == 10:
                                gold += 5
                            if item[1] == 20:
                                gold += 10
                            if item[1] == 30:
                                gold += 15
                            if item[1] == 40:
                                gold += 20
                            if item[1] == 50:
                                gold += 25
                            items.remove(item)
                            found_bank_item = True
                            break

                    if bank_input == "no":
                        break

                    if found_bank_item == False:
                        print("invalid input")
                        continue
# Input asking if they want to sell something else
                    bank_choice = input("Do you want to sell anything else? (yes or no): ")
# If  they say no, break
                    if bank_choice == "no":
                        break
# If they say yes, continue
                    if bank_choice == "yes":
                        continue
# Else it should say invalid input and continue
                    else:
                        print("invalid input")
                        continue
            leave_town = input("Do you want to leave the town? (yes or no): ")
            if leave_town == "yes":
                break
            if leave_town == "no":
                continue







# If statement for down
    if direction_choice == "down":
# 	A while true statement
        while True:
# 		Input asking at a trail split to go down a sandy trail or a rocky one
            trail_split_decicion = input("You have reached a trail split, would you like to go down the (sandy) trail or the (rocky) trail?: ")
# 		If input for sandy
            if trail_split_decicion == "sandy":
# 			While True statement
                while True:
# 				Input asking if you want to go to a strange man on the beach or wander around admiring the beauty.
                    sandy_decicion = input("Do you want to go to a strange (man) on the beach or (wander) around admiring the beauty?: ")
# 			If the input is the man
                    if sandy_decicion == "man":
# 				If you have crystals
                        if crystals == True:
# 					Print saying “he sees the crystals and decides to let you onto his raft for free.”
                            print("The man sees the crystals and while admiring their beauty lets you get on his raft.")
# 					Print saying “you sail into the horizon looking for your next adventure”
                            print("You realize your time on the island is over and you can't wait for your next adventure.")
# 					Make variable game_end equal to True
                            game_end = True
# 					break
                            break
# 				If you have two hundred gold
                        if gold >= 200:
# 					Print saying “he magically takes two hundred gold from you and lets you go on his raft.”
                            print("He magically takes two hundred gold from you and lets you go on his raft.")
# 					Print saying “you ask why he just stole your gold and he tells you that it was the payment”
                            print("You ask why he took your gold and he says it was payment.")
# 					Print saying “you sail into the horizon a little disgruntled but happy to get off the island.”
                            print("As you see the island for the last time, you are a little disrunled from the fact that he stole your gold but are happy to be going forward towards a new adventure.")
# 					Make variable game_end equal to True
                            game_end = True
# 					break
                            break
# 				Else print that he turns away saying not good enough yet and walks away, then set input to wander
                        else:
                            print("You hear him mumble that your not good enough yet and he walks away")
                            sandy_decicion = "wander"
# 		If the input is wander
                if sandy_decicion == "wander":
# 			While True statement
                    while True:
# 			Chance function at 10%
                        boat_chance = chance(10)
# 			If the chance function is equal to true
                        if boat_chance == True and shipwreck_found == False:
# 				Print that they found a shipwreck
                            shipwreck_found = True
                            print("You found a shipwreck!")
# 				Print that the player looked inside and found a secret chest with a +5 armor inside
                            print("you found a secret chest with +5 armor inside!")
                            items += ["Armor(+5)", 50, 5, 1]
# 				Print that the player decided to head back to town to celebrate
                            print("you decide to head back to the crossroad after finding the armor")
# 				Break
                            break
# 			If the chance function is equal to false
                        if boat_chance == False or shipwreck_found == True:
# 						Input saying that they did not find anything but do they want to try again?
                            if shipwreck_found == False:
                                wander_decicion = input("You did not find anything but do you want to try again? (yes or no):")
                            if shipwreck_found == True:
                                print("Why did you wander, if you already found the shipwreck!?")
                                break
# 						If input is equal to true 
                            if wander_decicion == "yes":
# 							Continue
                                continue
# 						If input is equal to false
                            if wander_decicion == "no":
# 							Break
                                break
# 						Else print invalid input, will count as false, and then break
                            else:
                                print("invalid input, will count as false.")
                                break
# 				Else it should say invalid input and continue
                else:
                    print("invalid input")
                    continue
# 				Break
                break
# 		If input for rocky
            if trail_split_decicion == "rocky":
# 			While True statement
                while True:
# 				Print that they have entered a cave
                    print("you have entered a cave.")
# 				Chance function at 10%
                    secret_tunnel_find = chance(10)
# 				If chance function is equal to true and tunnel_collapse is equal to false
                    if secret_tunnel_find == True and tunnel_collapse == False:
# 					Print that they found  secret side tunnel
                        print("You found a secret side tunnel!")
# 					Chance function at 50%
                        secret_tunnel_trap = chance(50)
# 					If chance function is equal to true
                        if secret_tunnel_trap == True:
# 						Print that they found a secret trap and were able to avoid it
                            print("You see a tripwire and carefully step over it")
# 						Print that they gained crystals from the chest
                            print("you open a chest and gain magical crystals! (It is not in your items because you can't gain anything from them unless someone likes really shiny stuff...)")
                            crystals = True
# 					If chance function is equal to false
                        if secret_tunnel_trap == False:
# 						Print that they broke a tripwire and the whole tunnel collapses
                            print("you break a tripwire and the whole secret tunnel collapses (the normal tunnel is fine).")
# 						Set tunnel_collapse equal to true
                            tunnel_collapse = True
# 						break
                            break
	
# it should print that they see an ogre
                    print("you see an ogre")
# 				Input asking if they want to run away
                    runaway_or_not = input("Do you wish to run away? (yes or no): ")
# 				If input is equal to true
                    if runaway_or_not == "yes":
# 					Break
                        print("you run all the way to the crossroad in fear")
                        break
# 				If input is equal to false
                    if runaway_or_not == "no":
# 						Do fighting function with user and ogre
                        ogre_battle = battle(User_stats, Ogre_stats)
# 						If win is equal to true
                        if ogre_battle == 1:
# 							Print that they found a +5 sword
                            print("You found a +5 sword!")
# 							Print that they decided to head back to town after the battle
                            print("You decide to head back to the crossroad after the fight.")
# 							Break
                            break
# 						If win is equal to false
                        if ogre_battle == 2:
# 							Print that they lost
                            print("You respawn at the crossroad")
# 							Break
                            break
                        if ogre_battle == 3:
                            print("you decided to go back to the crossroad after the fight.")
                            break
# 			Else print that it was invalid input and continue
                    else:
                        print("Invalid input")
                        continue
# 			Break
                    break
            break


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



