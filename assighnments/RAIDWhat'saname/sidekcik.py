
def calculate_stuff(x, y):
    z = x * y
    return z

def another_calculation(a, b, c):
    temp = calculate_stuff(a, b)
    result = temp * c
    return result

thing1 = 5
thing2 = 3
flat_thing = calculate_stuff(thing1, thing2)
print(f"The flat thing's size is: {flat_thing}")

foo = 4
bar = 6
baz = 2
big_thing = another_calculation(foo, bar, baz)
print(f"The big thing's size is: {big_thing}")