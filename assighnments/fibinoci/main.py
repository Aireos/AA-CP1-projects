n_o_n = 25
number = 0
number_two = 1
next_number = number_two
count = 1
print("0","1", end=" ")
while count <= n_o_n:
    print(next_number, end=" ")
    count += 1
    number, number_two = number_two, next_number
    next_number = number + number_two


    

