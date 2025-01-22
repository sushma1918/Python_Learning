#String Reversal: Write a Python function to reverse a given string without using the built-in reverse function.
''' String_name[start:stop:step]
Start=0
Stop=n-1
Step=+1'''
"""
S = "Sushma Sharma"
print("original string:",S)
print("Reversed string:",(S))

S2 = "Sushma"
print(S2[2:5:2])

S3 = "My Name Sushma Sharma"
print(S3[::-2])

a = input("Enter String_name: ")
print(a[-1::-1])

b = input("Enter the String: ")
for i in range ((len(a)-1),-1,-1):
    print(a[i],end="")

"""

#Count Vowels and Consonants : Write a Python program that accepts a string and counts the number of vowels and consonants in the string.
a = input("Enter a string: ")
vowel= 0
consonant= 0
for i in range(0,len(a)):
    if (a[i] ==" "):
        if (a[i]== 'a'or a[i]== 'e' or a[i]=='i' or a[i]=='o' or a[i]=='u'
            or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
            vowel = vowel+1
        else:
            consonant = consonant+1
print("Total Vowel=",vowel)
print("Total consonant=",consonant)

#Palindrome Check
#Write a Python program to check if a given string is a palindrome (reads the same forward and backward).

a = input("Enter String: ")
b = a[-1::-1]
if(a==b):
    print("Palindrame String")
else:
    print("Not Palindrame String")

