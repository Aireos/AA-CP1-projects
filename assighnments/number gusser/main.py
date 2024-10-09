#Make code where program generates a number between 1 and 10 and tell the user if they got it right.

#it should first tell them what it is, then have programm randomly generate number, then it will tell them to guess a number one through ten and tell them if it is correct.

#need to import random, make random number generater and get eh number in int form of what they gussed

#Import random (for generater)
#print "number gusser game" at the top right as code starts
#Ask for their guess (set to guess varaible)
#using random, generate number 1-10 (set to number varaible)
#set that if guess == number: tell them that they were correct
#set else: tell them that they were incorrect

totalcorrect = 0
totalwrong = 0
import random
print("Welcome to the 10 number guessing game!")

while True:
    number = random.randint(1, 10)
    guess = int(input("What is your guess for what number it is?: "))

    if guess == number:
        totalcorrect += 1
        y_or_n = input("You got it! Would you like to continue playing? (y or n): ")
        print('')
        
        if y_or_n == 'n':

            y_or_n_2 = input("would you like to see your win-to-loss ratio? (y or n): ")

            if y_or_n_2 == 'y':
                print("Your current win-to-loss ratio is:")
                print(totalcorrect, '/', totalwrong + totalcorrect)
                print('')
                break

            else: 
                print("ending game...")
                print('')
                break            

        elif y_or_n == 'y':
            y_or_n_2 = input("would you like to see your win-to-loss ratio? (y or n): ")

            if y_or_n_2 == 'y':
                print("Your current win-to-loss ratio is:")
                print(totalcorrect, '/', totalwrong + totalcorrect)
                print('')
                

            else: 
                print("reseting game...")
                print('')
    else:
        totalwrong += 1
        y_or_n = input("You missed it. Would you like to continue playing? (y or n): ")
        print('')
        
        if y_or_n == 'n':

            y_or_n_2 = input("would you like to see your win-to-loss ratio? (y or n): ")

            if y_or_n_2 == 'y':
                print("Your current win-to-loss ratio is:")
                print(totalcorrect, '/', totalwrong + totalcorrect)
                print('')
                break

            else: 
                print("ending game...")
                print('')
                break            

        elif y_or_n == 'y':
            y_or_n_2 = input("would you like to see your win-to-loss ratio? (y or n): ")

            if y_or_n_2 == 'y':
                print("Your current win-to-loss ratio is:")
                print(totalcorrect, '/', totalwrong + totalcorrect)
                print('')
                

            else: 
                print("reseting game...")
                print('')



# Does the program run?
# Yes
# Did you do something that made the program stop working, if so then what?
# entered random symbols
# Were you able to use the program without any help from the programmer (Meaning nothing had to be explained to you)
# Yes
# If you needed further explanation on things, what explanations did you need?
# None
#--------------------------------------------------------------------------------------------------------------------
# Does the program run?
# Yes
# Did you do something that made the program stop working, if so then what?
# random symbols
# Were you able to use the program without any help from the programmer (Meaning nothing had to be explained to you)
# Yes
# If you needed further explanation on things, what explanations did you need?
# What to do after gussing the number
#--------------------------------------------------------------------------------------------------------------------
# I could add spaces between questions to make it easier to understand and follow along.
# I could tell the user if their guess was to high or low
# Explain how to play a little better before the first question