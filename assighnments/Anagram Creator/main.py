


nospace = ""
import random
name = input("Type you're name with spaces in between each letter: ")

splitname = name.split(" ")
random.shuffle(splitname)
randomized_name = nospace.join(splitname)
print(" ")
print(randomized_name)
print(" ")
random.shuffle(splitname)
randomized_name1 = nospace.join(splitname)
if randomized_name1 != randomized_name:
    print(randomized_name1)
    print(" ")
random.shuffle(splitname)
randomized_name2 = nospace.join(splitname)
if randomized_name2 != randomized_name or randomized_name1:
    print(randomized_name2)
    print(" ")
random.shuffle(splitname)
randomized_name3 = nospace.join(splitname)
if randomized_name3 != randomized_name or randomized_name1 or randomized_name2:
    print(randomized_name3)
    print(" ")
random.shuffle(splitname)
randomized_name4 = nospace.join(splitname)
if randomized_name4 != randomized_name or randomized_name1 or randomized_name2 or randomized_name3:
    print(randomized_name4)
    print(" ")
print(" ")