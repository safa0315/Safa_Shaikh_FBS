#Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = input('Enter any alphabet: ')
vowel =['a', 'e', 'i','o', 'u']

if(alpha in vowel):
    print('Alphabet is a vowel.')

else:
    print('Alphabet is a consonent.')