#Write a program to calculate profit or loss.
#Profit: Profit = SP - CP (when SP > CP) #Loss: Loss = CP - SP (when CP > SP)

sp = int(input('Enter selling price: '))
cp = int(input('Enter cost price: '))

if(sp > cp):
    print('Profit.')

elif(cp > sp):
    print('Loss')

else:
    print('No profit, No loss.')