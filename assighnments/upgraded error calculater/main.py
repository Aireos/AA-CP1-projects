

while True:

    equation = input("What equation are you trying to do?: ")

    x = (input("what is your first number?: "))

    y = (input("what is your second number?: "))


    if is int(x):
        break
    else:
        print("invalid first #")
        continue
    

    if not y == int:
        print("invalid second #")
        continue


    if '//' in equation:
        print("answer:", x//y)
        break

    elif '*' in equation:
        print("answer:", x*y)
        break

    elif '+' in equation:
        print("answer:", x+y)
        break

    elif '/' in equation:
        print("answer:", x/y)
        break

    elif '^' in equation:
        print("answer:", x**y)
        break

    elif '-' in equation:
        print("answer:", x-y)
        break

    elif '%' in equation:
        print("answer:", x%y)
        break

print("Have a good day!")