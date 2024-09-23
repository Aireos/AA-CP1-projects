
nospace = ""
import random
name = input("Type you're name with spaces in between each letter: ")
splitname = name.split(" ")
random.shuffle(splitname)
randomized_name = nospace.join(splitname)
print(" ")
print(randomized_name)
print(" ")