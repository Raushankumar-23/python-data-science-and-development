# 📅 Python Programming Paradigms – Assignment / Practice Questions
# 🟢 Easy Level (Programs)

# Write a program using procedural programming to calculate the sum of two numbers.

# a = 12
# b = 13
# sum = a + b
# print(sum)

# Write a program using procedural approach to find the largest of three numbers.

# a = 120
# b = 105
# c = 90

# if a > b:
#     if a > c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b > c:
#         largest = b
#     else:
#         largest = c

# print(largest)

#Write a program using functional programming with filter() to extract even numbers from a list.

# nums = [1,2,3,4,5,6,7,8]

# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)

# Write a program using functional programming with reduce() to find the sum of all elements in a list.

from functools import reduce

nums = [1,2,3,4,5]

total = reduce(lambda a, b: a + b, nums)
print(total)

# Write a program using functional programming to square numbers in a list using map().

# t1=[1,2,3,4,5,6,7,8,9,11]

# result=set(map(lambda i:i*i,t1))
# print(result)

# 🟡 MEDIUM LEVEL

# Q. Write a program using functional programming to convert a list of strings into uppercase using map().

# words = ["python", "java", "c", "html"]

# upper_words = list(map(lambda x: x.upper(), words))
# print(upper_words)

# Q. Write a program using functional programming to extract numbers greater than 10 from a list using filter().

# nums = [3, 7, 12, 18, 5, 25, 9]

# greater_than_10 = list(filter(lambda x: x > 10, nums))
# print(greater_than_10)

# Q. Write a program using functional programming to find square and cube of numbers using map().
# nums = [1, 2, 3, 4, 5]

# result = list(map(lambda x: (x*x, x*x*x), nums))
# print(result)


# Q. Write a program using functional programming to extract vowels from a string using filter().

# text = "programming"

# vowels = list(filter(lambda x: x in "aeiou", text))
# print(vowels)


# Q. Write a program using procedural + functional approach to count even numbers in a list.
# nums = [10, 15, 20, 25, 30, 35]

# even_count = len(list(filter(lambda x: x % 2 == 0, nums)))
# print("Even count:", even_count)


# 🔴 HARD LEVEL (5 Questions)
# Q. Write a program using functional programming to find the sum of squares of a list using map() and reduce().

# from functools import reduce

# nums = [1, 2, 3, 4]

# result = reduce(lambda a, b: a + b,
#                 map(lambda x: x*x, nums))
# print(result)


# Q. Write a program using functional programming to remove duplicate values from a list.

# nums = [1,2,2,3,4,4,5,5,6]

# unique = list(set(filter(lambda x: True, nums)))
# print(unique)


#Q. Write a program using procedural and functional programming to validate a password.

# pwd = input("Enter password: ")

# valid = (
#     len(pwd) >= 8 and
#     any(map(str.isdigit, pwd)) and
#     any(map(str.isupper, pwd))
# )

# print("Valid Password" if valid else "Invalid Password")


#Q. Write a program using generator-based paradigm to generate prime numbers up to a given limit.
# def primes(n):
#     for num in range(2, n):
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             yield num

# for p in primes(20):
#     print(p, end=" ")


#Q. Write a program combining procedural, functional, and generator paradigms.
# def squares(nums):      # generator
#     for n in nums:
#         yield n*n

# nums = [1,2,3,4,5]      # procedural

# even_squares = list(filter(lambda x: x % 2 == 0, squares(nums)))
# print(even_squares)