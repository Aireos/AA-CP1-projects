import random
nospace = ""
onespace = " "

while True:
    full_name = input("What is your full name?: ")
    try:
        full_name = int(full_name)
        print("your name cannot have numbers in it.")
        continue
    except:
        if not ' ' in full_name:
            print("you need a first and last name. (type none for last name if you don't have one.)")
            continue
        break

firstname, lastname = full_name.split(" ")
firstname = firstname.capitalize()
lastname = lastname.capitalize()

if 'None' == lastname:
    random_lastname_number = random.randint(1,8)
    if random_lastname_number == 1:
        lastname = "Hilton"
        full_name = firstname + " " + lastname
    if random_lastname_number == 2:
        lastname = "West"
        full_name = firstname + " " + lastname
    if random_lastname_number == 3:
        lastname = "Hope"
        full_name = firstname + " " + lastname
    if random_lastname_number == 4:
        lastname = "Lopez"
        full_name = firstname + " " + lastname
    if random_lastname_number == 5:
        lastname = "Dawson"
        full_name = firstname + " " + lastname
    if random_lastname_number == 6:
        lastname = "Pierce"
        full_name = firstname + " " + lastname
    if random_lastname_number == 7:
        lastname = "Ashford"
        full_name = firstname + " " + lastname
    if random_lastname_number == 8:
        lastname = "Spade"
        full_name = firstname + " " + lastname
    

print("Welcome,", full_name)