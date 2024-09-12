

#making the definition of calulate_one
def calculate_one(x, y):
    area = x * y
    return area


#making def of calculate_two
def calculate_two(a, b, c):
    volume = calculate_one(a, b)
    result = volume * c
    return result

#calulation to find the flat size
length_2d = 5
width_2d = 3
twoD_area= calculate_one(length_2d, width_2d)
print(f"The 2d item's area is: {twoD_area}")

length_3d = 4
width_3d = 6
height_3d = 2
threeD_volume = calculate_two(length_3d, width_3d, height_3d)
print(f"The 3d item's volume is: {threeD_volume}")
