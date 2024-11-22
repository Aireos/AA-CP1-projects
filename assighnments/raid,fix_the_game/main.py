import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 9
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts+1} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess and game_over == False:
            attempts += 1
            print("Too high! Try again.")
        elif guess < number_to_guess and game_over == False:
            attempts += 1
            print("Too low! Try again.")  
        continue
    print("Game Over. Thanks for playing!")
start_game()

# the first error i found was that the "guess" variable is not a int so i just added int() around the input
# the second error i found was that it would nover add to # of attemps so i added "attempts =+ 1" before to high and to low, try again.
# the third error i found was that it gave you eleven trys so i minused one from max attemtpts and added one to print function in "if attempts >= max_attempts:"
# the final error i found wsa that it would say "Too low! Try again." after you lost the game. to fix this I added "and game_over == False" into the two elif functions
