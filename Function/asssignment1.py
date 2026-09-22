#check prime number: type 1:

def check():
    num = int(input("Enter a number: "))

    count = 0

    for i in range(1, num + 1):
        if (num % i == 0):
            count = count + 1

    if (count == 2):
        print("Prime number")
    else:
        print("Not a prime number")


check()


#type 2:

def check(num):

    count = 0

    for i in range(1, num + 1):
        if (num % i == 0):
            count = count + 1

    if (count == 2):
        print("Prime number")
    else:
        print("Not a prime number")


num = int(input("Enter a number: "))
check(num)


#type 3
def check():
    num = int(input("Enter a number: "))

    count = 0

    for i in range(1, num + 1):
        if (num % i == 0):
            count = count + 1

    if (count == 2):
        return "Prime number"
    else:
        return "Not a prime number"


result = check()
print(result)

#type 4


def check(num):

    count = 0

    for i in range(1, num + 1):
        if (num % i == 0):
            count = count + 1

    if (count == 2):
        return "Prime number"
    else:
        return "Not a prime number"


num = int(input("Enter a number: "))
result = check(num)
print(result)


