

def square_area_alg():
    length = int(input("What is the side length?: "))
    area = length * length
    return area

def rectangle_area_alg():
    length = int(input("What is the length?: "))
    width = int(input("What is the width?: "))
    area = length * width
    return area

def triangle_area_alg():
    length = int(input("What is the length?: "))
    height = int(input("What is the height?: "))
    area = ((length * height) / 2)
    return area

def circle_area_alg():
    radius = int(input("What is the radius?: "))
    area = ((radius^2) * 3.14)
    return area

def trapezoid_area_alg():
    length = int(input("What is the base length?: "))
    length_two = int(input("What is the second base length?: "))
    height = int(input("What is the height?: "))
    area = (((length + length_two) / 2) * height)
    return area



print("   square = 1")
print("rectangle = 2")
print(" triangle = 3")
print("   circle = 4")
print("trapezoid = 5")
type = int(input("What would you like to caluculate?: "))

if type == 1:
    area = square_area_alg()
    print("The area of your shape is:", area)

if type == 2:
    area = rectangle_area_alg()
    print("The area of your shape is:", area)

if type == 3:
    area = triangle_area_alg()
    print("The area of your shape is:", area)

if type == 4:
    area = circle_area_alg()
    print("The area of your shape is:", area)

if type == 5:
    area = trapezoid_area_alg()
    print("The area of your shape is:", area)

elif type:
    print("Invalid Number")






