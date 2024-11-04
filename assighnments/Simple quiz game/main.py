
correct = False

def C_O_I(user_answer, answer):

    correct = False

    if user_answer == answer:
        print()
        print("You got it right!")
        print()
        correct = True
        return correct

    else:
        print()
        print("You got it wrong.")
        print()
        return correct
print()
print("math quiz time!")
print()

#first question
user_answer = int(input("What is 2+1 (1, 2, 3 or 4): "))
answer = 3
correct = C_O_I(user_answer, answer)

while True:
    #second question hard
    if correct == True:
        user_answer = int(input("What is 2-1 (1, 2, 3 or 4): "))
        answer = 1
        correct = C_O_I(user_answer, answer)
        break

    #second question easy
    elif correct == False:
        user_answer = int(input("What is 1+1 (1, 2, 3 or 4): "))
        answer = 2
        correct = C_O_I(user_answer, answer)
        break

while True:
    #third question hard
    if correct == True:
        user_answer = int(input("What is 4/2 (1, 2, 3 or 4): "))
        answer = 1
        correct = C_O_I(user_answer, answer)
        break

    #third question easy
    elif correct == False:
        user_answer = int(input("What is 4-2 (1, 2, 3 or 4): "))
        answer = 2
        correct = C_O_I(user_answer, answer)
        break

while True:
    #fourth question hard
    if correct == True:
        user_answer = int(input("What is 2*2 (1, 2, 3 or 4): "))
        answer = 1
        correct = C_O_I(user_answer, answer)
        break

    #fourth question easy
    elif correct == False:
        user_answer = int(input("What is 2/2 (1, 2, 3 or 4): "))
        answer = 2
        correct = C_O_I(user_answer, answer)
        break

while True:
    #fith question hard
    if correct == True:
        user_answer = int(input("What is 2-1 (1, 2, 3 or 4): "))
        answer = 1
        correct = C_O_I(user_answer, answer)
        break

    #fith question easy
    elif correct == False:
        user_answer = int(input("What is 1+1 (1, 2, 3 or 4): "))
        answer = 2
        correct = C_O_I(user_answer, answer)
        break
