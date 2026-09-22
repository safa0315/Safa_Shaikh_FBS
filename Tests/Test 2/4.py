# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.


area = float(input("Enter area of one wall: "))
cost = float(input("Enter painting cost per square unit: "))

total_area = 4 * area

total_cost = total_area * cost

print("Total painting cost =", total_cost)