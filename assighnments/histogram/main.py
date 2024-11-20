nospace = ""

input1 = input("What is your first input?: ")
input2 = input("What is your second input?: ")
input3 = input("What is your third input?: ")
input4 = input("What is your fourth input?: ")
input5 = input("What is your fifth input?: ")
input6 = input("What is your sixth input?: ")

amounts = [input1, input2, input3, input4, input5, input6]
outputs = ['','','','','','']
placment = -1

for i in amounts:

    placment += 1
    amount = []
    i = int(i)

    while i >= 1:
        i -= 1
        amount += '*'
    number = placment + 1
    number = str(number)
    print(number + ":", nospace.join(amount))
