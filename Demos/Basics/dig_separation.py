num = 795

while(num > 0):
    d = num % 10   #to find the remainder which will be the number at unit's place (5)
    print(d)        #print that number
    num = num // 10   #to put the remaining value in the original variable (79) 
                       #this will go on till all the numbers are done 