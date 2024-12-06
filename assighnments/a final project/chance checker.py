import random
def chance(percent):
    chance_variable = (random.randint(1,percent))
    if chance_variable == 1:
        return True
    elif chance_variable != 1:
        return False

def checker(percent):
    number_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while number_list != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        number = (random.randint(1,percent))
        if number in number_list:
            continue
        else:
            if number == 1:
                number_list[0] = 1
            if number == 2:
                number_list[1] = 2
            if number == 3:
                number_list[2] = 3
            if number == 4:
                number_list[3] = 4
            if number == 5:
                number_list[4] = 5
            if number == 6:
                number_list[5] = 6
            if number == 7:
                number_list[6] = 7
            if number == 8:
                number_list[7] = 8
            if number == 9:
                number_list[8] = 9
            if number == 10:
                number_list[9] = 10
    print(number_list)

percent = random.randint(10,11)
number = checker(percent)
