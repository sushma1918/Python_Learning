# Create a string in Python
"""
string = "Hello, My name is Sushma"
print(string)

a ="Hello, I am Sushma."
print(a)
"""
#Single_line 
'He Said,"I want to eat an apple".'

apple = 'He Said,"I want to eat an apple".'
print('He Said,"I want to eat an apple".')

#MultiLine String
a = """ It looks like your background could be a 
match for this Digital Marketing Manager role.
Please submit a quick application if you have any interest."""
print(a)

#Access the 5th character of a string
"""
a = "Python"
print(a[3])

x = "Python"
print(x[5])

z = "Sushma Sharma"
print(z[8])

b="Sushma"
print(b[-4])
"""
#Reverse a string
"""
x = "Sushma Sharma"
reversed_x = x[::-2]
print(reversed_x)
"""
"""
s1 = "Python"
s2 = 'Sushma' 
s3 = ''' 
My name is sushma sharma
i am using python '''
print(s1,s2,s3)
"""
# string pratices
# My Name Is "Sushma"

S1 = 'My Name Is "Sushma Sharma"'
print(S1)

#length()
"""
S2 = "Sushma Sharma"
print(len(S2))

S3 = "Python"
print(len(S3))
"""

#len And reverse(whlie)
"""
string = "I Love Python"
l = len(string)
i = 0
while i<l: #5<5 
    print(string[i], end=" ")
    i+=1
print()

#unary minus
i=1
l=len(string)
while i<=l : #5<=5
    print(string[-i], end=" ")
    i+=1
print()
"""
# Slicing 
'''
Slicing 
String_name[start:stop:step]
Start = 0
Stop = n-1
Step = +1
'''
"""
string = "I Love Python"
for i in string [ ::-1]:
    print(i,end= " ")
print() 

String = "I Love Python"
print(String [2:3:2])
"""

#String reverse
'''String_name[start:stop:step]
Start=0
Stop=n-1
Step=+1
'''
S2 = "I Love Python"
print(S2[2:5:2])

S4 = "I Love Python"
print(S4[::2])

S5 = "My Name Sushma Sharma"
print(S5[::-2])

# multiplication
''' String_name*n '''
new = "Python"
slice = new[0:2:1]
print(slice*2)

new1 = " I Am Sushma Sharma"
slice = new1[3:6:4] #n-1 2-1 =1
print(slice*2)

new1 = " I Am Sushma Sharma"
slice = new1[0:6:4]
print(slice*5)

#Conceatenate
''' + Concatenation operation
'''
