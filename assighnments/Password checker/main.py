
special_character = "@" or "#" or "$" or "%" or "*" or "&"

wrongthings = []

is_password_enough = False

def is_there_a_number(s):
    return any(i.isdigit() for i in s)

while is_password_enough == False:

    wrongthings = []

    password = input("what do you want your password to be?: ")

    if len(password) < 8:
        print("Your password is not long enough.(needs at least 8 charecters)")
        wrongthings += "1"

    if is_there_a_number(password) == False:
        print("You need a number in your password.")
        wrongthings += "2"

    if not special_character in password:
        print("Your need a special character in your password.")
        wrongthings += "3"

    if wrongthings == []:
        is_password_enough = True

print("good job making your password! Your password is:", password)
