import random
spacer = "~~~~~~~~~~~~~"
row1 = ["|"," ","1"," ","|"," ","2"," ","|"," ","3"," ","|"]
row2 = ["|"," ","4"," ","|"," ","5"," ","|"," ","6"," ","|"]
row3 = ["|"," ","7"," ","|"," ","8"," ","|"," ","9"," ","|"]

def gameboard():
    print()
    print()
    print()
    print()
    print()
    print(spacer)
    print(''.join(row1))
    print(spacer)
    print(''.join(row2))
    print(spacer)
    print(''.join(row3))
    print(spacer)

while True:
    while True:
        gameboard()
        placment = int(input("What place on the bourd do you want to place a X on? (1-9): "))
        if placment in row1 or row2 or row3:
            if placment == 1:
                row1[2] = "X"
            if placment == 2:
                row1[6] = "X"
            if placment == 3:
                row1[10] = "X"
            if placment == 4:
                row2[2] = "X"
            if placment == 5:
                row2[6] = "X"
            if placment == 6:
                row2[10] = "X"
            if placment == 7:
                row3[2] = "X"
            if placment == 8:
                row3[6] = "X"
            if placment == 9:
                row3[10] = "X"        
            gameboard()
            break
        else:
            print("That placement is already taken, try again.")

    while True:
        number = random.randint(1,9)
        if number in row1 or row2 or row3:
            if number == 1:
                row1[2] = "O"
            if number == 2:
                row1[6] = "O"
            if number == 3:
                row1[10] = "O"
            if number == 4:
                row2[2] = "O"
            if number == 5:
                row2[6] = "O"
            if number == 6:
                row2[10] = "O"
            if number == 7:
                row3[2] = "O"
            if number == 8:
                row3[6] = "O"
            if number == 9:
                row3[10] = "O"        
            gameboard()
            break
    
    if row
