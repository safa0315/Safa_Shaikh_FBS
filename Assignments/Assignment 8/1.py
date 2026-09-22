#Write a program to calculate area od rectangle:

def area_rectangle(length, breadth):
    area = length * breadth
    return area


length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

result = area_rectangle(length, breadth)

print("Area of rectangle =", result)