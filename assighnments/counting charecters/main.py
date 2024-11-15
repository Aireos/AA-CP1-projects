
amounts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def letter_finder(x):

    if x == 'A':
        amounts[0] += 1

    if x == 'B':
        amounts[1] += 1

    if x == 'C':
        amounts[2] += 1

    if x == 'D':
        amounts[3] += 1

    if x == 'E':
        amounts[4] += 1

    if x == 'F':
        amounts[5] += 1

    if x == 'G':
        amounts[6] += 1

    if x == 'H':
        amounts[7] += 1

    if x == 'I':
        amounts[8] += 1

    if x == 'J':
        amounts[9] += 1

    if x == 'K':
        amounts[10] += 1

    if x == 'L':
        amounts[11] += 1

    if x == 'M':
        amounts[12] += 1

    if x == 'N':
        amounts[13] += 1

    if x == 'O':
        amounts[14] += 1

    if x == 'P':
        amounts[15] += 1

    if x == 'Q':
        amounts[16] += 1

    if x == 'R':
        amounts[17] += 1

    if x == 'S':
        amounts[18] += 1

    if x == 'T':
        amounts[19] += 1

    if x == 'U':
        amounts[20] += 1

    if x == 'V':
        amounts[21] += 1

    if x == 'W':
        amounts[22] += 1

    if x == 'X':
        amounts[23] += 1

    if x == 'Y':
        amounts[24] += 1

    if x == 'Z':
        amounts[25] += 1


grid = [

['A', 'B', 'C', 'D', 'E'],

['F', 'G', 'H', 'I', 'J'],

['K', 'L', 'M', 'N', 'O'],

['P', 'Q', 'R', 'S', 'T'],

['U', 'V', 'W', 'X', 'Y', 'Z'] ]



for i in grid:
    for x in i:
        letter_finder(x)

print("Number of...")
print("A:",amounts[0])
print("B:",amounts[1])
print("C:",amounts[2])
print("D:",amounts[3])
print("E:",amounts[4])
print("F:",amounts[5])
print("G:",amounts[6])
print("H:",amounts[7])
print("I:",amounts[8])
print("J:",amounts[9])
print("K:",amounts[10])
print("L:",amounts[11])
print("M:",amounts[12])
print("N:",amounts[13])
print("O:",amounts[14])
print("P:",amounts[15])
print("Q:",amounts[16])
print("R:",amounts[17])
print("S:",amounts[18])
print("T:",amounts[19])
print("U:",amounts[20])
print("V:",amounts[21])
print("W:",amounts[22])
print("X:",amounts[23])
print("Y:",amounts[24])
print("Z:",amounts[25])

