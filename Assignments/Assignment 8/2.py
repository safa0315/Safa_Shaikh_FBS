# 2. Write a program to calculate area of circle

def area_circle(radius):
    area = 3.14 * radius * radius
    return area


radius = int(input("Enter radius: "))

result = area_circle(radius)

print("Area of circle =", result)