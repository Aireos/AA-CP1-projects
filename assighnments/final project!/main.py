while True:
    full_name = input("What is your full name?: ")
    try:
        full_name = int(full_name)
        print("your name cannot have numbers in it.")
    except:
        if not ' ' in full_name:

