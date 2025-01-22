'''
# Using %
name = "Sushma Sharma"
age = 27
print("My name is %s and I am %d years old." % (name, age))

# Using .format()
name = "Sushma Sharma"
age = 27
print("My name is {} and I am {} years old.".format(name, age))

#Using f-strings
name = "Sushma Sharma"
age = 27
print(f"My name is {name} and I am {age} years old.")

'''

# Converting
string1 = "Sushma Sharma"
print(string1.lower())
print(string1.upper())

#compersion

String_1 = "SUSHMA SHARMA"
String_2 = "sushma shrama"
print(String_1.lower == String_2.upper())

S1 = "Sushma Sharma"
S2 = "sushma sharma"
print(S1.lower() == S2.lower())

P1 = "SUSHMA SHARMA"
P2 = "Sushma Sharma"
print(P1.upper() == P2.upper())

SA = "SUSHMA SHARMA"
SB= "sushma sharma"
print(SA.upper() == SB.lower())

PA = "SUSHMA SHARMA"
PB = "Sushma Sharma"
print(PA.upper() == PB.upper())