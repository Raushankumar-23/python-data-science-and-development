#Python Practice Questions
#Topic: Loops, break, continue, patterns, sum of digits


# Q1. Write a Python program to print numbers from 1 to 10 using a loop.

# for i in range(1,11):
#     print(i)
# print("Done")

# Q2. Write a Python program to print numbers from 1 to 20 but skip multiples of 3 using continue.

# for i in range(1,21):
#     if i%3!=0:
#         print(i)
#print("Done")

# Q3. Write a Python program to calculate the sum of digits of a given number using a loop.

# num=int(input("Enter a number : "))
# n=num
# sum=0
# while n>0:
#     sum=sum+n%10
#     n=n//10
# print("Sum of digint in ",num,"of",sum)
    
# Q4. Write a Python program to print all even numbers between 1 and 50 using a loop.

# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i+=1
        
# print("Done")

# for i in range(1,51):
#     if i%2==0:
#         print(i)

# print("Done")

# MEDIUM LEVEL

# Q5. Write a Python program to print numbers from 1 to 100 and stop when the number reaches 50 using break.

# for i in range(1,101):
#     if i==50:
#         break
#     print(i)
# print("Done")


# Q6. Write a Python program to keep taking numbers from the user and calculate their sum.
# Stop when the user enters 0.

# total = 0

# while True:
#     num = int(input("Enter a number (0 to stop): "))
    
#     if num == 0:
#         break
    
#     total = total + num

# print("Sum of all numbers is:", total)

    
# Q7. Write a Python program to print the following pattern:
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()
        
# print("Prenting Done")

# Q8. Write a Python program to print the following pattern:
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#      for j in range(i):
#          print(j+1,end="")
#      print()
        
# print("Prenting Done")

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
        
#     i=i+1

# print("prenting is Done")

# HARD LEVEL

# Q9. Write a Python program to reverse a number using a loop and then find the sum of its digits.

# num=int(input("Enter a number : "))
# n=num
# sum=0
# rev=0
# while n>0:
#     sum=sum+n%10
#     rev=rev*10+n%10
#     n=n//10
# print("Sum of digint in ",num,"of",sum)
# print("Reverse of digint",num,"is ",rev)
 

# Q10. Write a Python program to print numbers from 1 to 100 such that:
# - Skip numbers divisible by 5
# - Stop the loop when the number is divisible by 17

# i=1
# while i<=100:
#     if i%17==0:
#         break
#     if i%5==0:
#         i=i+1
#         continue
    
#     print(i)
#     i=i+1
        
# Q11. Write a Python program to print the following pattern:
# *****
# ****
# ***
# **
# *
# i=5
# while i>0:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j=j+1
#     print()
        
#     i=i-1

# print("prenting is Done")

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
# print("prenting is Done")

# Q12. Write a Python program to check whether a given number is a palindrome using a loop.

num=int(input("Enter a number : "))
i=num
rev=0
while i>0:
    rev=rev*10+i%10
    i=i//10
    
    
if num==rev:
    print(num,"Is palindrome number ")
else:
    print(num,"is not a palindrome number ")