

import random
nospace = ("")
print(" ")
before = input("What would you like to make into a secret message? (Make sure to put a space inbetween each letter/number): ")
split = before.split(" ")
split1 = before.split(" ")
random.shuffle(split)
randomized = nospace.join(split)
before1 = nospace.join(split1)
print(" ")
print("Before:", before1)
print("After: ", randomized)


