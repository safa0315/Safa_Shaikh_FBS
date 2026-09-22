num = 795

sum = 0
while(num > 0):
    d = num % 10   #to find the remainder which will be the number at unit's place (5)
    #print(d)  
    sum += d      #sum = sum + d
    num = num // 10 
print(sum)    #sum of all numbers 