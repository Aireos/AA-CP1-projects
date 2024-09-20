score = 0
question1 = int(input("what is 1+1?:"))
question2 = int(input("what is 3+1?:"))
question3 = int(input("what is 3*2?:"))
question4 = int(input("what is 20/2?:"))
question5 = int(input("what is 72/4?:"))
if question1 == 2:
    score += 1
if question2 == 4:
    score += 1
if question3 == 6:
    score += 1
if question4 == 10:
    score += 1
if question5 == 18:
    score += 1
print("Your score is:", score, "/ 5")

