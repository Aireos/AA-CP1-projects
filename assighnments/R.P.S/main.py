

import time
import random
placements = []
print("Welcome to tick tac toe!")
print()
rounds = int(input("How many rounds would you like to play?: "))
print()
while rounds >= 1:
    placement = int(input("What place on the bourd do you want to place a X at?: "))
    if placement in placements:
        print("this ")