import time

time_left = int(input("How long (in seconds) do you want you timer to be?: "))
print(time_left)
while time_left > 0:
    (time.sleep(1))
    time_left = time_left - 1
    print(time_left)