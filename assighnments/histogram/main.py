nospace = ""

input1 = (input("What is your first input?: "))
input2 = (input("What is your second input?: "))
input3 = (input("What is your third input?: "))
input4 = (input("What is your fourth input?: "))
input5 = (input("What is your fifth input?: "))
input6 = (input("What is your sixth input?: "))

amount1 = []
amount2 = []
amount3 = []
amount4 = []
amount5 = []
amount6 = []

for i in input1:
    i = int(i)
    while i >= 1:
        i -= 1
        amount1 += "*"
amount1 = nospace.join(amount1)
print("1:",amount1)

for i in input2:
    i = int(i)
    while i >= 1:
        i -= 1
        amount2 += "*"
amount2 = nospace.join(amount2)
print("2:",amount2)

for i in input3:
    i = int(i)
    while i >= 1:
        i -= 1
        amount3 += "*"
amount3 = nospace.join(amount3)
print("3:",amount3)

for i in input4:
    i = int(i)
    while i >= 1:
        i -= 1
        amount4 += "*"
amount4 = nospace.join(amount4)
print("4:",amount4)

for i in input5:
    i = int(i)
    while i >= 1:
        i -= 1
        amount5 += "*"
amount5 = nospace.join(amount5)
print("5:",amount5)

for i in input6:
    i = int(i)
    while i >= 1:
        i -= 1
        amount6 += "*"
amount6 = nospace.join(amount6)
print("6:",amount6)