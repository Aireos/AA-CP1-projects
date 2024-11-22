name = str(input("What do you want your charecter name to be?: "))
print()
while True:

    Race = input("What race do you want to be? (Human, Elf, Dwarf or Halfling): ").lower()
    print()
    if Race == "human":
        health = 4
        strength = 4
        dexterity = 4
        intelligence = 4
        break

    if Race == "elf":
        health = 3
        strength = 3
        dexterity = 5
        intelligence = 5
        break

    if Race == "dwarf":
        health = 5
        strength = 5
        dexterity = 3
        intelligence = 3
        break

    if Race == "halfling":
        health = 3
        strength = 5
        dexterity = 3
        intelligence = 5
        break

    else: print("that is not a valid race.")
    print()

while True:

    Class = input("What class do you want to be? (Rouge, Paleden, Ranger, Warrior or Wizard): ").lower()
    print()
    if Class == "rouge":
        health -= 1
        strength -= 1
        dexterity += 2
        intelligence += 0
        break

    if Class == "paleden":
        health += 2
        strength += 1
        dexterity -= 2
        intelligence -= 1
        break

    if Class == "ranger":
        health -= 1
        strength += 1
        dexterity += 1
        intelligence -= 1
        break

    if Class == "warrior":
        health += 1
        strength += 1
        dexterity -= 1
        intelligence -= 1
        break

    if Class == "wizard":
        health -= 2
        strength -= 2
        dexterity += 1
        intelligence += 3
        break

    else: print("that is not a valid class.")
    print()
print("Name:", name)
print()
print("Race:", Race)
print()
print("Class:", Class)
print()
print("Health:", health)
print()
print("Strength:", strength)
print()
print("Dexterity:", dexterity)
print()
print("Intelligence:", intelligence)
print()