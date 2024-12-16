import random
import time

nospace = ""
onespace = " "
tunnel_collapse = False
game_end = False
crystals = False
shipwreck_found = False
directions = ["do you want to go", "up,", "down,", "left,", "see your (stats),", "or go", "right?: "]
crazy_wanderer = 0
armor_found = False
continueing_times = 0
working = 10
gold = 100
shop_choice_answer = ""
lockbox_found = False
ogre_won = False

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
items = []

def weapon_player(items):
    for list in items:
        if list[0] == "Weapon(+5)":
            return 5
    for list in items:
        if list[0] == "Weapon(+4)":
            return 4
    for list in items:
        if list[0] == "Weapon(+3)":
            return 3
    for list in items:
        if list[0] == "Weapon(+2)":
            return 2
    for list in items:
        if list[0] == "Weapon(+1)":
            return 1
    else:
        return 0

def ring_player(items):
    for list in items:
        if list[0] == "Ring(+5)":
            return 5
    for list in items:
        if list[0] == "Ring(+4)":
            return 4
    for list in items:
        if list[0] == "Ring(+3)":
            return 3
    for list in items:
        if list[0] == "Ring(+2)":
            return 2
    for list in items:
        if list[0] == "Ring(+1)":
            return 1
    else:
        return 0

def armor_player(items):
    for list in items:
        if list[0] == "Armor(+5)":
            return 5
    for list in items:
        if list[0] == "Armor(+4)":
            return 4
    for list in items:
        if list[0] == "Armor(+3)":
            return 3
    for list in items:
        if list[0] == "Armor(+2)":
            return 2
    for list in items:
        if list[0] == "Armor(+1)":
            return 1
    else:
        return 0

ring = int(ring_player(items))
armor = int(armor_player(items))
weapon = int(weapon_player(items))
User_stats = [10 + weapon, 10 + ring, 10 + armor, full_name]

def stat_checker(items, full_name):
    ring = int(ring_player(items))
    armor = int(armor_player(items))
    weapon = int(weapon_player(items))
    User_stats = [10 + weapon, 10 + ring, 10 + armor, full_name]
    return User_stats


# Ogre stats list
#            dmg  hth arm
Ogre_stats = [14, 18, 13, "Ogre"]

# Contestants list that will include ten contestants of differing strengths.
Contestants = [[9, 9, 9, "goblin"], [12, 12, 12, "Archer"],[13, 13, 13, "Palidin"],[11, 11, 11, "Rogue"],[15, 15, 15, "Dwarf"],[14, 14, 14, "Bard"],[16, 16, 15, "Champion"]]

# a item list for the blacksmith
blacksmith_list = [["Armor(+1)", 10, 1, 1], ["Armor(+2)", 20, 2, 1], ["Armor(+3)", 30, 3, 1], ["Armor(+4)", 40, 4, 1]]

# a item list for the ring shop
ring_list = [["Ring(+1)", 10, 1, 2], ["Ring(+2)", 20, 2, 2], ["Ring(+3)", 30, 3, 2], ["Ring(+4)", 40, 4, 2]]

# a item list for the shop in the arena
arena_list = [["Weapon(+1)", 10, 1, 3], ["Weapon(+2)", 20, 2, 3], ["Weapon(+3)", 30, 3, 3], ["Weapon(+4)", 40, 4, 3]]

# an item list for the traveling trader’s shop.
trader_list = [["Armor(+1)", 8, 1, 1], ["Ring(+1)", 8, 1, 2], ["Weapon(+1)", 8, 1, 3]]


# chance function that will be used whenever there is a chance an event occurs.
def chance(percent):
    if (random.randint(1,percent)) == 1:
        return True
    else:
        return False
    
# battle function that will check who wins based on their three stats.
# 1 output = player1 won, 2 output = player2 won, 3 = it was a tie
def battle(player1,player2,continueing_times, User_stats):
    if player1 == User_stats:
        User_stats = stat_checker(items, full_name)
        player1 = User_stats
    continueing_times = 0
    player2health = player2[1] - (player1[0] - player2[2])
    player1health = player1[1] - (player2[0] - player1[2])
    if player1health <= 0:
        if player2health <= 0:
            if player2health > player1health:
                print(player2[3], "won!")
                return 2
            elif player1health > player2health:
                print(player1[3], "won!")
                return 1
            else:
                print("It was a tie!")
                return 3
        print(player2[3], "won!")
        return 2
    elif player2health <= 0:
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
                    elif player1health > player2health:
                        print(player1[3], "won!")
                        return 1
                    else:
                        print("It was a tie!")
                        return 3
                print(player2[3], "won!")
                return 2
            elif player2health <= 0:
                print(player1[3], "won!")
                return 1
            elif continueing_times >= 50:
                print("It was a tie!")
            if player1health and player2health > 0 and continueing_times < 50:
                continueing_times += 1
                continue


# function for shops so that it is easy to make all the shops work
def shop(shoplist, gold, items):
    print("current gold:", gold)
    while True:
        item_found = False
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
                        item_found = True               
                        continue
        if wanted_item == "leave":
            return gold, items
        if item_found == True:
            continue
        else:
            print("That item does not exist!")
            continue

# While the variable game_end is equal to false
while game_end == False:

    User_stats = stat_checker(items, full_name)

# input asking if they want to go up, down, left, or right
    direction_choice = input(onespace.join(directions))

    if direction_choice == "stats":
        print("Weapon:", User_stats[0])
        print("Health:", User_stats[1])
        print("Armor:", User_stats[2])

# if statement for up
    if direction_choice == "up":
# print the statement: “You are now in the town square.”
        print("Welcome to the town square.")
        directions[1] = "town(up),"
# A while true statement
        while True:
# input statement asking if they want to go to the blacksmith, bank, or grocery.
            town_square_decicion = input("Do you want to go to the (blacksmith), (bank), or the health (ring) shop? (type leave if you want to go back to crossroad): ")
            if town_square_decicion == "leave":
                break
# if statement for Blacksmith
            if town_square_decicion == "blacksmith":
# Run the shop function with the item list for the blacksmith
                gold, items = shop(blacksmith_list, gold, items)
# If statement for grocery
            if town_square_decicion == "ring":
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
                            if item[1] == 8:
                                gold += 4
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
                    if bank_choice != "no" and bank_choice != "yes":
                        print("invalid input")
                        continue
            leave_town = input("Do you want to leave the town? (yes or no): ")
            if leave_town == "yes":
                break
            if leave_town == "no":
                continue




# If statement for down
    if direction_choice == "down":
        directions[2] = "trail split(down),"
# 	A while true statement
        while True:
# 		Input asking at a trail split to go down a sandy trail or a rocky one
            if game_end == True:
                break
            if armor_found == True:
                armor_found = False
                break
            if ogre_won == True:
                ogre_won = False
                break
            trail_split_decicion = input("You have reached a trail split, would you like to go down the (sandy) trail or the (rocky) trail? (type leave if you want to go back to crossroad): ")
            if trail_split_decicion == "leave":
                break
# 		If input for sandy
            if trail_split_decicion == "sandy":
# 			While True statement
                while True:
                    if armor_found == True:
                        break
# 				Input asking if you want to go to a strange man on the beach or wander around admiring the beauty.
                    sandy_decicion = input("Do you want to go to a strange (man) on the beach or (wander) around admiring the beauty? (type exit to leave): ")
# 			If the input is the man
                    if sandy_decicion == "exit":
                        break
                    if sandy_decicion == "man":
# 				If you have crystals
                        if crystals == True:
# 					Print saying “he sees the crystals and decides to let you onto his raft for free.”
                            print("The man sees the crystals and while admiring their beauty lets you get on his raft.")
# 					Print saying “you sail into the horizon looking for your next adventure”
                            print("You realize your time on the island is over and you can't wait for your next adventure.")
# 					Make variable game_end equal to True
                            game_end = True
                            break
# 				If you have two hundred gold
                        if gold >= 200:
# 					Print saying “he magically takes two hundred gold from you and lets you go on his raft.”
                            print("He magically takes two hundred gold from you and lets you go on his raft.")
# 					Print saying “you ask why he just stole your gold and he tells you that it was the payment”
                            print("You ask why he took your gold and he says it was payment.")
# 					Print saying “you sail into the horizon a little disgruntled but happy to get off the island.”
                            print("As you see the island for the last time, you are a little disgruntled from the fact that he stole your gold but are happy to be going forward towards a new adventure.")
# 					Make variable game_end equal to True
                            game_end = True
                            break
# 				Else print that he turns away saying not good enough yet and walks away, then set input to wander
                        if gold < 200 and crystals == False:
                            print("You hear him mumble that your not good enough yet and he walks away")
# 		    If the input is wander
                    if sandy_decicion == "wander":
    # 			While True statement
                        while True:
    # 			Chance function at 10%
                            boat_chance = chance(5)
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
                                armor_found = True
    # 				Break
                                break
    # 			If the chance function is equal to false
                            if boat_chance == False or shipwreck_found == True:
    # 						Input saying that they did not find anything but do they want to try again?
                                if shipwreck_found == False:
                                    wander_decicion = input("You did not find anything but do you want to try again? (yes or no):")
                                if shipwreck_found == True:
                                    if crazy_wanderer == 20:
                                        print("Ok, If you really are doing this, I as the creator, force you off the island!")
                                        game_end = True
                                        break
                                    print("Why did you wander, if you already found the shipwreck!?")
                                    crazy_wanderer += 1
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
                                if wander_decicion != "yes" and wander_decicion != "no":
                                    print("invalid input, will count as false.")
                                    break
                    elif sandy_decicion != "wander" and sandy_decicion != "man":
                        print("invalid input")
                        continue
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
                        secret_tunnel_trap = chance(2)
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

                        ogre_battle = battle(User_stats, Ogre_stats, continueing_times, User_stats)
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
                            ogre_won = True
# 							Break
                            break
                        if ogre_battle == 3:
                            print("you decided to go back to the crossroad after the fight.")
                            break
# 			Else print that it was invalid input and continue
                    if runaway_or_not != "yes" and  runaway_or_not != "no":
                        print("Invalid input")
                        continue
#else statement
            if trail_split_decicion != "rocky" and trail_split_decicion != "sandy":
                print("invalid input")
                continue


# 	If statement for left
    if direction_choice == "left":
        directions[3] = "arena(left),"
        print("Welcome to the arena")
# 		A while True statement
        while True:
            #Input asking if they want to go to the stands, betting stand, store or fight.
            arena_input = input("Do you want to go to the stands, betting stand, store, fight, or leave?: ")
            if arena_input == "leave":
                break
# 			If input is equal to stands
            if arena_input == "stands":
# 				While true statement
                while True:
                    player1 = Contestants[random.randint(0, 5)]
                    player2 = Contestants[random.randint(0, 5)]
                    while player2 == player1:
                        player2 = Contestants[random.randint(0, 5)]
# 					Print that they are watching (name) and (name) fight
                    print("You are watching", player1[3], "and", player2[3], "fight.")
# 					Do fighting function for the two of them
                    battle(player1, player2, continueing_times, User_stats)
# 					Input asking if they want to watch again
                    stands_decicion = input("Do you wish to watch again? (yes or no): ")
# 					If input is equal to no
                    if stands_decicion == "yes":
                        continue
# 					If input is equal to yes
                    if stands_decicion == "no":
                        break
# 					Else print invalid input: will count as yes
                    if stands_decicion != "yes" and stands_decicion != "no":
                        print("invalid input, will count as yes")
                        continue
# 			If input is equal to betting stand
            if arena_input == "betting stand":
# 				While true statement
                while True:
# 					Print that they are watching (name) and (name) fight
                    player1 = Contestants[random.randint(0, 5)]
                    player2 = Contestants[random.randint(0, 5)]
                    while player2 == player1:
                        player2 = Contestants[random.randint(0, 5)]
# 					Print that they are watching (name) and (name) fight
                    print("You are watching 1:", player1[3], "and 2:", player2[3], "fight.")
# 					User guess input asking who that think will win
                    betting_input = int(input("who do you think will win? (1 or 2): "))
# 					Input asking how much they are willing to bet
                    while True:
                        print("you currently have", gold, "gold.")
                        betting_amount = int(input("how much gold are you wanting to bet?: "))
# 					If input 2 is less then or equal to their money amount
                        if betting_amount <= gold:
# 						Print that the transaction worked
                            print("transaction completed")
                            break
# 					Else print that they don’t have that much money and continue
                        else:
                            print("you do not have that much money.")
                            continue
# 					Do fighting function for the two of them
                    betting_battle = battle(player1, player2, continueing_times, User_stats)
# 					If the users guess is correct
                    if betting_battle == betting_input:
# 						Give double gold back
                        print("you got double your betted gold!")
                        gold += betting_amount
#                   if battle equals 3 print that the person they guessed for tied with the other one and give their gold back that they bet
                    elif betting_battle == 3:
                        print("because they tied you don't lose or gain anything.")
# 					if battle is the other person won
                    elif betting_battle != betting_input and betting_battle != 3:
# 						Tell user that they lost all the gold
                        print("you lost all the gold you bet")
                        gold -= betting_amount
# 					Input asking if they want to bet again
                    bet_again = input("do you wish to bet again? (yes or no): ")
# 					If input equals yes
                    if bet_again == "yes":
# 						Continue
                        continue
# 					If input equals no
                    if bet_again == "no":
# 						Break
                        break
                    else:
                        print("invalid input, will count as no.")
                        break



# 			If input is equal to the store
            if arena_input == "store":
# 				Run the shop function with the item list for the arena store
                gold, items = shop(arena_list, gold, items)




# 			If the input is equal to fight
            if arena_input == "fight":
# 				While True statement
                while True:
                    player2 = Contestants[random.randint(0, 5)]
# 				if gold is less then 30 print that they do not have enough money and break
                    if gold < 20:
                        print("you do not have enough gold")
                        break
# 					Print that they are fighting (name)
                    print("you are fighting", player2[3])
# 				Do fighting function for the two of them
                    user_battle = battle(User_stats, player2, continueing_times, User_stats)
# 				If user won
                    if user_battle == 1:
# 					Give user 60 gold
                        gold += 40
                        print("gain 40 gold")
# 				If user lost
                    if user_battle == 2:
# 					Have user lose 60 gold
                        gold -= 20
                        print("loose 20 gold")
                    if user_battle == 3:
                        print("don't lose or gain anything")
# 				Input asking if they want to fight again
                    user_battle_input = input("do you want to fight again? (yes or no): ")
# 				If input is equal to yes
                    if user_battle_input == "yes":
# 					Continue
                        continue
# 				If input is equal to no
                    if user_battle_input == "no":
# 					Break
                        break
# 		Else print that it was a invalid input and break
                    else:
                        print("invalid input, will count as no")
# 		                Break
                        break
            elif arena_input != "fight" and arena_input != "betting stand" and arena_input != "stands" and arena_input != "store":
                print("invalid input")
                continue

# If statement for right
    if direction_choice == "right":
        directions[6] = "merchent(right)?: "
# 	Print that they have met the traviling merchant and he says hello
        print("you have meet a traviling merchant and he says hello")
# 	While true statement
        while True:
# 	Input statement asking if they want to Buy anything or work for him
            trader_decicion = input("He asks if you want to (buy) anything, (work) for him, or (leave): ")
            if trader_decicion == "leave":
                break
# 	If input is equal to buy anything
            if trader_decicion == "buy":
# 		Run the shop function with the item list for the traviling trader
                gold, items = shop(trader_list, gold, items)
# 	If input is equal to work for him
            if trader_decicion == "work":
# 		While times working here is at least 1
                if working != 0:
                    while True:
                        if working == 0:
                            break
                        working -= 1
# 			Tell user that they did hard labor and have used one of their ten times working here
                        print("you can only work", working, "times more.")
# 			Give user 5 gold
                        gold += 5
                        print("you gain 5 gold")
# 			Chance function at 10%
                        box_find = chance(10)
# 			If chance function is true and lockbox found is equal to false
                        if box_find == True and lockbox_found == False:
                            lockbox_found = True
# 				Tell user they found a secret lockbox with 100 gold inside
                            print("you found a secret lockbox with 100 gold inside!")
# 					Lockbox found set to true
# 				Input asking user if they want to steal it
                            steal_input = input("Do you wish to steal the lockbox? (yes or no): ")
# 				If input is equal to true
                            if steal_input == "yes":
# 					Chance function at 50%
                                stealing = chance(2)
# 					If chance function is true
                                if stealing == True:
# 						Tell user they got away
                                    print("you got away and gained 100 gold")
# 						Give user 100 gold
                                    gold += 100
# 						Break
                                    break
# 					Else print that they go caught
                                else:
                                    print("you got caught and lost half of all your money")
# 						Have user lose 50% of all money
                                    gold = gold/2
# 						Break
                                    break
# 			If chance function is false	
                            if steal_input == "no":
                                print("The wandering trader is happy for you not stealing his money and gives you a +5 ring")
                                items += ["Ring(+5)", 50, 5, 1]
# 			Ask user if they want to work again right now
                        trader_input = input("would you like to work again right now? (yes or no): ")
# 			If user answer is yes
                        if trader_input == "yes":
# 				Continue
                            continue
# 			If user answer is no 
                        if trader_input == "no":
# 				Break
                            break
# 	Else print that it is a invalid input and break
                        elif trader_input != "yes" and trader_input != "no":
                            print("invalid input, will count as no")
                            break
            elif trader_decicion != "work" and trader_decicion != "buy":
                print("invalid input")
                continue
# 	Break
            break
# Else print that is a invalid input and continue
    elif direction_choice != "up" and direction_choice != "down" and direction_choice != "right" and direction_choice != "left" and direction_choice != "stats":
        print("invalid input")
        continue
# Print “thanks for playing my game”
print("Thanks for playing my game!")



