# 📅 Day 2 – Operators & if-else (10 Questions)
# 1. Perform all arithmetic operations on two numbers.

# num1=float(input("Enter a first number : "))
# num2=float(input("Enter a second number : "))
# print("Sum of ",num1, "and",num2,"is",num1+num2)
# print("Substraction of ",num1, "minus",num2,"is",num1-num2)
# print("Multiplication of ",num1, "and",num2,"is",num1*num2)
# print("Divide ",num1, "by",num2,"is",num1/num2)
# print("Remainder of",num1, "divide by",num2,"is",num1%num2)
# print(num1, "power",num2,"is",num1**num2)
# print("Floor value of",num1, "divide by",num2,"is",num1//num2)


# 2. Compare two numbers using relational operators.

# num1=float(input("Enter a first number : "))
# num2=float(input("Enter a second number : "))
# print(num1==num2)
# print(num1>num2)
# print(num1<num2)
# print(num1!=num2)
# print(num1>=num2)
# print(num1<=num2)

# 3. Demonstrate logical operators.

# n1=float(input("Enter a first number : "))
# n2=float(input("Enter a second number : "))
# n3=float(input("Enter a third number : "))
# n4=float(input("Enter a fourth number : "))
# print(n1<n2 and n3<n4)
# print(n1<n2 and n3>n4)
# print(n1<n2 or n3<n4)
# print(n1>n2 or n3<n4)
# print(n1<n2 or n3>n4)
# print(n1>n2 or n3>n4)
# print(not(n1<n2))
# print(not(n1>n2))


# 4. Demonstrate assignment operators.

# a=10
# a+=5
# print(a)
# a-=3
# print(a)
# a*=2
# print(a)
# a/=2
# print(a)
# a**=2
# print(a)
# a//=2
# print(a)

# 5. Check whether a number is positive or negative.

# n=float(input("Enter a  number : "))
# if n>0:
#     print(n,"is positive number")
# elif n==0:
#     print(n,"is not negative and not positive")
# else:
#     print(n,"is negative number")

# 6. Check whether a number is even or odd using if-else.

# n=int(input("Enter a  number : "))
# if n%2==0:
#     print(n,"is Even number")
# else:
#     print(n,"is odd number")

# 7. Find the largest of two numbers.

# n1=int(input("Enter a first number : "))
# n2=int(input("Enter a second number : "))
# if n1>n2:
#     print(n1,"is grater than ",n2)

# else:
#     print(n2,"is grater than",n1)
    
# 8. Find the largest of three numbers.

# n1=int(input("Enter a first number : "))
# n2=int(input("Enter a second number : "))
# n3=int(input("Enter a third number : "))
# if n1>n2:
#     if n2>n3:
#         print(n1,"is grater in ",n1,n2,n3)
#     else:
#         print(n3,"is grater in ",n1,n2,n3)
# else:
#     if n2>n3:
#         print(n2,"is grater in",n1,n2,n3)
#     else:
#         print(n3,"is grater in",n1,n2,n3)

# 9. Write a grade calculator program.

# marks=int(input("Enter a your marks : "))
# if marks>=90:
#     print("Pass with A Grade")
# elif marks>=80:
#     print("Pass with B Grade")
# elif marks>=70:
#     print("Pass with C Grade")
# elif marks>=60:
#     print("Pass with D Grade")
# elif marks>=50:
#     print("Pass with E Grade")
# else:
#     print("Fail")

# 10. Check whether a person is eligible to vote.

# age=int(input("Enter your age in Years : "))
# if age>=18:
#     print("You are eligible for Vote")
# else:
#     print("You are not eligible for Vote")