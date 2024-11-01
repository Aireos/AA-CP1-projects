
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

print("math quiz time!")
print()
print("A = 1")
print("B = 2")
print("C = 3")
print("D = 4")
print()

#first question
user_answer = input("What is 2+1 (A, B, C or D): ").lower()
answer = "c"
correct = C_O_I(user_answer, answer)

#second question hard
if correct == True:
    user_answer = input("What is 2-1 (A, B, C or D): ")
    answer = "a"
    correct = C_O_I(user_answer, answer)

#second question easy
elif correct == False:
    user_answer = input("What is 1+1 (A, B, C or D): ")
    answer = "b"
    correct = C_O_I(user_answer, answer)

