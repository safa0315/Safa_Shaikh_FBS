#write an algorithm to find out the maximum and 2nd max element from the given list

li = [40, 50, 20, 60, 30, 10]

max = li[0]
smax = 0
for ind in range (0, len(li)):
    if(li[ind] > max):
        smax = max
        max = li[ind]

    elif(li[ind] > smax):
        smax = li[ind]

    else:
        pass
print('Max element:', max)
print('Max 2 element:', smax)