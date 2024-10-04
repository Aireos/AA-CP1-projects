list = []

while True:
    action = input("""What would you like to do?
                             Enter 1 to add item

                             Enter 2 to remove item
                             
                             Enter 3 to see list
                   
                             Enter 4 to leave the list:\n""") 

    if action =="1":
        item = input("Please enter the item you want to add to your list:\n")
        list.append(item)

    if action =="3":
        print("your current list is:", list)

    if action =="2":
        if list == []:
            print("you have nothing to remove!")
            break
        print(list)
        item = input("what item would you like to remove?:")
        list.remove(item)

    elif action == "4":

        print("Have a nice day!")
        break