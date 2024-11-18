
while True:

    equation = input("What equation are you trying to do?: ")

    x = input("what is your first number?: ")

    y = input("what is your second number?: ")

    
    try:
        int(x)
        x = int(x)

    except:
        print("invalid first #")

        try:
            int(y)
            y = int(y)   
        except:
            print("invalid second #")
            continue
        else: 
            continue
        
    try:
        int(y)
        y = int(y)   
        
    except:
        print("invalid second #")
        continue
    

    if '//' == equation:
        print("answer:", x//y)
        break
            

    elif '*' == equation:
        print("answer:", x*y)
        break
            

    elif '+' == equation:
        print("answer:", x+y)
        break
            

    elif '/' == equation:
        print("answer:", x/y)
        break
            

    elif '^' == equation:
        print("answer:", x**y)
        break
            

    elif '-' == equation:
        print("answer:", x-y)
        break
            

    elif '%' == equation:
        print("answer:", x%y)
        break

    else:
        print("invalid equation")
        continue


print("Have a good day!")