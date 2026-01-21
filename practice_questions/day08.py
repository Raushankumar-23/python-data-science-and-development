# 📘 Python Exceptions – Assignment / Practice Questions
# 🟢 Easy Level

# Write a program to handle ZeroDivisionError.

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# try:
#     div = num1 / num2
#     print(div)
# except ZeroDivisionError:
#     print("Divide by zero is not possible")

# print("rest of code")

# Write a program to handle ValueError when converting input to integer.

# try:
#     num1 = int(input("Enter first number : "))
#     print(100/num1)
    
# except ValueError:
#     print("Enter correct value")
    
# except ZeroDivisionError:
#     print("Divide by zero is not possible")

# print("rest of code")

# Write a program to handle IndexError while accessing a list element.

# numbers=[3,5,6,8,10,9,3]
# try:
#     print(numbers[8])
    
# except IndexError:
#     print("Invalid index ")
    
# print("rest of code")

# Write a program to handle KeyError while accessing a dictionary key.

# student={
#     "name":"Raushan",
#     "roll_number":90,
#     "marks":90   
    
# }
# try:
#     print(student["age"])
    
# except KeyError:
#     print("Key is not present")
    
# print("rest of code")

# Write a program to use try and except to print a custom error message.

# numbers=[3,5,6,8,10,9,3]
# try:
#     print(numbers["name"])
    
# except:
#     print("custom error")

# print("rest of code")

# 🟡 Medium Level

# Write a program using try–except–else.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# try:
#     div = num1 / num2
# except ZeroDivisionError:
#     print("Divide by zero is not possible")
# else:
#     print("Division successful:", div)

# print("rest of code")


# Write a program using try–except–finally.

# Write a program using try–except–finally.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# try:
#     div = num1 / num2
#     print(div)

# except ZeroDivisionError:
#     print("Divide by zero is not possible")

# else:
#     print("No exception occurred")

# finally:
#     print("Always executed")


# Write a program to handle multiple exceptions in a single try block.

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# try:
#     div = num1 / num2
#     print(di)
# except ZeroDivisionError:
#     print("Divide by zero is not possible")
    
# except NameError:
#     print("variable name is not correct")
    

# print("rest of code")

# Write a program to validate user input and raise an exception for invalid input.

# Write a program to validate user input and raise an exception for invalid input.

# try:
#     num1 = int(input("Enter a number: "))
#     if num1 <= 0:
#         raise ValueError("Number must be greater than zero")
#     print(100 / num1)

# except ValueError as e:
#     print("Invalid input:", e)

# print("rest of code")


# 🔴 Hard Level

# Write a program to raise a custom exception for invalid age.

try:
    age=int(input("Enter your age "))
    if age<0:
        raise ValueError
    print("Your age is : ",age)
except ValueError:
    print("Enter valid age ")
    
print("reset of code")


# Write a program to create and use a user-defined exception class.

# Write a program to handle exceptions inside a function.

# Write a program to handle exceptions while performing dictionary operations.

# Write a program to demonstrate nested try–except blocks.