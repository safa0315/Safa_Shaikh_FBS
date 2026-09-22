# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

area_rectangle = length * breadth
area_circle = 3.14 * radius * radius / 2

area = area_rectangle + area_circle

perimeter = length + length + breadth + 3.14 * radius

print("Area =", area)
print("Perimeter =", perimeter)