#📅 Day 4 – Functions (Assignment)
#🟢 Easy Level

# 1. Write a function to print a welcome message.

# def greet():
#     print("Welcomes python learners")

# greet()

# def welcome(name):
#     print("Welcome ",name)

# welcome("Raushan")

# 2. Write a function to add two numbers and return the sum.

# def add(a,b):
#     return a+b

# result=add(5,6)
# print("Sum is ",result)

# n1=float(input("Enter a first number : "))
# n2=float(input("Enter a second number : "))

# def add(a,b):
#     return a+b

# total=add(n1,n2)
# print("Sum of",n1,"and",n2,"is",total)


# 3. Write a function to check whether a number is even or odd.

# num=int(input("Enter a number : "))
# def check(n1):
#     if n1%2==0:
#         print(n1,"is even number")
#     else:
#         print(n1,"is odd number")
        
# check(num)

# 4. Write a function to find the square of a number.

# def square(n):
#     return n**2

# num=int(input("Enter a number : "))

# result=square(num)
# print("Square of ",num,"is",result)

# 🟡 Medium Level

# Write a function to find the factorial of a given number.

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact

# num=int(input("Enter a number : "))

# result=factorial(num)
# print("Factorial of ",num,"is",result)
        

# Write a function to generate the Fibonacci series up to n terms.

# def fib(i):
#     if i==1:
#         return 0
#     elif i==2 or i==3:
#         return 1
#     else:
#         return fib(i-1)+fib(i-2)
            
# num=int(input("Enter a number : "))

# def ses(a):
#     print("the ",num,"fibonacci term is : ")
#     i=1
#     while i<=a:
#         print(fib(i) ,end=" ")
#         i=i+1
        
# ses(num)

# Write a function to find the sum of digits of a number.

# def sum_of_digit(n):
#     i=n
#     sum=0
#     while i>0:
#         sum=sum+i%10
#         i=i//10
        
#     return sum

# num=int(input("Enter a number : "))
# result=sum_of_digit(num)
# print("Sum of digit of",num,"is",result)
    

# Write a function to check whether a number is a palindrome.

# def palindrome(n):
#     rev=0
#     i=n
#     while i>0:
#         rev=rev*10+i%10
#         i=i//10
    
#     if rev==n:
#         print(n,"is palindrome")
        
#     else:
#         print(n,"is not a palindrome")

# num=int(input("Enter a number : "))

# palindrome(num)

# 🔴 Hard Level

# Write a function to find the largest element in a list.

# def largest_element(list):
#     largest=list[0]
#     i=0
#     while i<len(list):
#         if list[i]>largest:
#             largest=list[i]
        
#         i=i+1
        
#     return largest
        
# list=[1,2,3,4,5]
# print(largest_element(list))


# Write a function to count vowels in a string.

# def count_vowel(string):
#     vow=0
#     for i in string:
#         if i.lower() in ["a","e","i","o","u"]:
#             vow=vow+1
            
#     return vow

# string="Raushan"
# print(count_vowel(string))


# Write a function to check whether a number is prime.

# def check_prime(n):
#     if n <= 1:
#         print(n, "is not a prime number")
#         return

#     i = 2
#     while i < n:
#         if n % i == 0:
#             print(n, "is not a prime number")
#             return
#         i = i + 1

#     print(n, "is a prime number")


# num = int(input("Enter a number: "))
# check_prime(num)

# Write a recursive function to calculate factorial or Fibonacci.

#factorial

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# num = int(input("Enter a number: "))
# res=fact(num)
# print(res)

def fib(i):
    if i==1:
       return 0
    elif i==2 or i==3:
        return 1
    else:
        return fib(i-1)+fib(i-2)
            
num=int(input("Enter a number : "))

def ses(a):
    print("the ",num,"fibonacci term is : ")
    i=1
    while i<=a:
        print(fib(i) ,end=" ")
        i=i+1
        
ses(num)
