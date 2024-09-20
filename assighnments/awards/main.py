


staff = int(input("how many staff are attending?"))

if staff == 0:
    print("You need staff.")

elif staff > 0: 
    students = int(input("How many students are being awarded?"))
    if students == 0:
        print("There will be no ceremony needed.")
    elif students > 0: 
        possible_guests = (students * 2)
        amount_of_tables = (possible_guests + staff + students)
