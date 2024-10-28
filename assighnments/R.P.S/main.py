

import time
import random
gamedone = False
score = 0
(time.sleep(0.25))

print("Welcome to Rock, Paper, Scissors!")
print()
while True:

    computer_input = random.randint(1,3)

    if computer_input == 1:
        computer_input = "rock"

    if computer_input == 2:
        computer_input = "paper"

    if computer_input == 3:
        computer_input = "scissor"
    

    user_input = input("Would you like to do rock, paper, or scissor?: ")
    user_input = user_input.lower()


    if computer_input == "rock" and user_input == "rock":
        print()
        print("The computer chose rock")
        print()
        print("You both chose rock.")
        print()
        continue

    if computer_input == "rock" and user_input == "paper":
        print()
        print("The computer chose rock")
        print()
        print("You won!")
        score += 1
        print()
        choice = input("Would you like to play again? (yes or no): ")
        print()
        if choice == "yes":
            continue
        if choice == "no":
            break

    if computer_input == "rock" and user_input == "scissor":
        print()
        print("The computer chose rock")
        print()
        print("You lost")
        score += -1
        print()
        choice = input("Would you like to play again? (yes or no): ")
        print()
        if choice == "yes":
            continue
        if choice == "no":
            break 


    if computer_input == "paper" and user_input == "rock":
        print()
        print("The computer chose paper")
        print()
        print("You lost")
        score += -1
        print()    
        choice = input("Would you like to play again? (yes or no): ")
        print()
        if choice == "yes":
            continue
        if choice == "no":
            break

    if computer_input == "paper" and user_input == "paper":
        print()
        print("The computer chose paper")
        print()
        print("You both chose paper.")
        print()
        continue

    if computer_input == "paper" and user_input == "scissor":
        print()
        print("The computer chose paper")
        print()
        print("You won!")
        score += 1
        print()
        choice = input("Would you like to play again? (yes or no): ")
        print()
        if choice == "yes":
            continue
        if choice == "no":
            break


    if computer_input == "scissor" and user_input == "rock":
        print()
        print("The computer chose scissor")
        print()
        print("You won!")
        score += 1
        print()
        choice = input("Would you like to play again? (yes or no): ")
        print()
        if choice == "yes":
            continue
        if choice == "no":
            break

    if computer_input == "scissor" and user_input == "paper":
        print()
        print("The computer chose scissor")
        print()
        print("You lost")
        score += -1
        print()
        choice = input("Would you like to play again? (yes or no): ")
        print()
        if choice == "yes":
            continue
        if choice == "no":
            break

    if computer_input == "scissor" and user_input == "scissor":
        print()
        print("The computer chose scissor")
        print()
        print("You both chose scissor.")
        print()
        continue


    else: 
        print()
        print("Invalid entry, try again")
        print()
        continue
print("you score was:",score)
print()
print("Bye!")
print()