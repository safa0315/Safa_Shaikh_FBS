li = [[10, 20], [30, 40], [50, 60]]
#li = [5, [10, 20], [30, 40], [50, 60]]
#WAP to calculate sum of all elements

# sum = 0

# for subli in li:
#     for ele in subli:
#         sum = sum + ele

# print(sum)



total = 0

for i in range(len(li)):
    for j in range(len(li[i])):
        total = total + li[i][j]

print(total)



