str1 = input("Write word: ")
rev = ""

for i in range(len(str1) - 1, -1, -1):
    rev = rev + str1[i]

print(rev)