data = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]

#res = tuple(filter(lambda n: n % 2 == 0, data))
res = tuple(filter(lambda n: n * n, data))  #if the returning value is not falsy like 0, None, False, null then it will filter out the number
print(res)