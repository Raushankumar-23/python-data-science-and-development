# 📘 Lambda, map, filter & reduce – Assignment / Practice Questions
# 🟢 Easy Level (Basics)

# Write a lambda function to add two numbers.

# add=lambda a,b:a+b
# n1=int(input("Enter first number : "))
# n2=int(input("Enter first number : "))
# print("Sum is",add(n1,n2))

# Write a lambda function to find the square of a number.

# squar=lambda x:x*x
# n=int(input("Enter a number : "))
# print("Square of ",n,"is",squar(n))

# Use map() to find the square of each element in a list.

# l=[1,2,3,4,5,6]
# squar = list(map(lambda x:x*x,l))
# print(squar)

# Use filter() to get all even numbers from a list.

# l=[1,2,3,4,5,6,7,9,11,12,14,16,17]
# even=list(filter(lambda x:(x%2==0),l))
# print(even)

# Use map() with a lambda function to convert a list of strings to uppercase.

# string="Hello Raushan How are You"
# uppe=list(map(lambda x:x.upper(),string.split()))
# print(uppe)


# 🟡 Medium Level (Logic Building)

# Use filter() to get numbers greater than 50 from a list.
# l=[1,20,100,60,90,110,55,141,56,3,4,5,6]
# nums=list(filter(lambda x:( x>50),l))
# print(nums)


# Use map() to add 10 to each element of a list.

# l=[1,2,3,4,5,6]
# add=list(map(lambda x:x+10,l))
# print("New list",add)

# Use filter() to get all prime numbers from a list.

l = [1, 20, 100, 60, 90, 110, 55, 141, 56, 3, 4, 5, 6]

primes = list(filter(
    lambda x: x > 1 and all(x % i != 0 for i in range(2, x)),
    l
))

print("Prime numbers:", primes)


# Use map() to find the length of each string in a list.

# string="Hello Raushan How are You"
# length=list(map(lambda x:len(x),string.split()))
# print(string)
# print("length is string",length)


# Use reduce() to find the sum of all elements in a list.

# from functools import reduce

# l = [1, 2, 3, 4, 5, 6]
# result = reduce(lambda x, y: x + y, l)

# print("Sum of elements:", result)



# 🔴 Hard Level (Advanced)

# Use reduce() to find the product of all numbers in a list.

# from functools import reduce
# l=[1,2,3,4,5,6]
# resut=reduce(lambda x, y: x * y, l)
# print("Product of all list element is",resut)

# Use map() + filter() together to get squares of even numbers from a list.

# l=[1,2,3,4,5,6,10]
# squares=list(map(lambda x:x*x ,filter(lambda x:x%2==0 ,l)))
# print("Square of even no from list is :",squares)

# Use lambda + reduce() to find the maximum element in a list.

# from functools import reduce
# l=[1,2,3,4,5,6]
# large=reduce(lambda x,y:x if x>y else y,l)
# print(large)


# Use map() to create a list of tuples (number, square) from a list.

# l=[1,2,3,4,5,6]
# lists=list(map(lambda x:(x,x*x),l))
# print(lists)


# Use filter() to remove empty strings from a list.


# string = ["Hello", " ", "Raushan", "How", " ", "are", "You"]

# result = list(filter(lambda x: x.strip() != "", string))
# print(result)
