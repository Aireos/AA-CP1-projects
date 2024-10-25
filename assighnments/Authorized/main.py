

admins = ["Jerry","Hamilton","Ms.Larose","Luke"]

users = ["Billy","Bob","Joe","Alex"]

name = (input("What is your name?: "))

if name in admins:
    status = "a admin"

elif name in users:
    status = "a user"

else:
    status = "unautherized"

print("you are", status)
