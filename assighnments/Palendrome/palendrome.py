#Alexander Anderson  palandrom
text = input('What do you want to check to see if it is a palendrome?: ')
reversedtext = text[::-1]
if text == reversedtext:
    print()
    print(text, "is a palendrome")
else:
    print()
    print(text, "is not a palendrome")
