
equation = input("What equation are you trying to do?: ")
x = int(input("what is your first number?: "))
y = int(input("what is your second number?: "))


if '//' in equation:
    print("answer:", x//y)

elif '*' in equation:
    print("answer:", x*y)

elif '+' in equation:
    print("answer:", x+y)

elif '/' in equation:
    print("answer:", x/y)

elif '^' in equation:
    print("answer:", x**y)

elif '-' in equation:
    print("answer:", x-y)

elif '%' in equation:
    print("answer:", x%y)

