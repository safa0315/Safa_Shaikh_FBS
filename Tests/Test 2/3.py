# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

radius = 20
length = 50
breadth = 40
cost = 35

semicircle = 3.14 * radius

perimeter = 2 * length + breadth + semicircle

total_wire = perimeter * 5

total_cost = total_wire * cost

print("Perimeter =", perimeter)
print("Total wire required =", total_wire)
print("Total cost =", total_cost)