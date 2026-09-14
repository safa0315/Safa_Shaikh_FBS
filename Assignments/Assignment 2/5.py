#WAP to calculate selling price of book based on cost price and discount.
#Selling Price (from Discount): Marked Price - Discount
#if discount given in amount
cost = int(input('Enter cost price: '))
disc = int(input('Enter discount amount: '))

selling_p = cost - disc

print(f'Selling price of book is {selling_p} Rs.')