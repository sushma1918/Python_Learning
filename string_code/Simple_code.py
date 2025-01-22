# 1. Print "Hello, World!"

print("Hello, World!")

# 2. Write a Python program to print "Hello, World!" to the console.
print("Hello, World!")

# 3.Write a Python program that takes two numbers as input and prints their sum.
Integer


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_of_numbers = num1 + num2

print(f"The sum of {num1} and {num2} is {sum_of_numbers}")

Float
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_of_numbers = num1 + num2

print(f"The sum of {num1} and {num2} is {sum_of_numbers}")
"""
# 4. Sum of Two Numbers
Integer

"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum1 = a + b

print("The sum is:", sum1)

Float
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

sum2 = x + y

print("The sum is:", sum2)

"""
# 5. SImple Calculater
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    print(f"The result is: {num1 + num2}")
elif choice == '2':
    print(f"The result is: {num1 - num2}")
elif choice == '3':
    print(f"The result is: {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
else:
    print("Error: Division by zero is not allowed.")

"""
# 6. Write a Python program that takes two numbers and an operator (+, -, *, /) as input,
#  then performs the corresponding arithmetic operation and prints the result.
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    print(f"The result is: {num1 + num2}")
elif operator == "-":
    print(f"The result is: {num1 - num2}")
elif operator == "*":
    print(f"The result is: {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operator!")


# Check Positive or Negative

number = float(input("Enter a number: "))

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

# 7.Write a Python program that takes a number as input and checks whether the number is positive, negative, or zero.
a = int(input("Enter a number: "))
if a > 0:
    print("The number is positive.")
elif a < 0:
    print("The number is negative.")
else:
    print("The number is zero." )


# 8. Print the Length of a String

a = input("Enter a string: ")
length = len(a)
print(f"The length of the string is : {length}")

# 9.Write a Python program that takes a string as input and prints its length.
user_string = input("Enter a string: ")
string_length = len(user_string)
print(f"The length of the string is: {string_length}")


# 10.Check Leap Year

year = int(input("Enter a year: "))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    
    print(f"This is a leap year")
else:
    print(f"This is not a leap year")


# 11.Print Multiples of a Number
# Write a Python program to print the first 10 multiples of a given number.
num = int(input(" Enter a number: "))
for i in range (1,11):
    print(f"{num} x {i} = {num * i}")


# 12. Write a Python program that counts the number of digits in a given number.
# Count the Number of Digits in a Number
n1= int(input("Enter a number:"))
count = 0
while n1 != 0:
    n1 //= 10
    count += 1
print(f"The number of digit is :{count}")

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)



## Check Even or Odd (using a function)
def check(number):
    if number%2 ==0:
        return"Even"
    else:
        return"Odd"
num = int(input("Enter a number : "))
result = check(number)
print(f"The number {num} is {result}.")

# Write a Python function that checks whether a given number is even or odd.
def is_even(number):
    return number % 2 == 0

num = int(input("Enter a number: "))

if is_even(num):
    print(f"The number {num} is Even.")
else:
    print(f"The number {num} is Odd.")

