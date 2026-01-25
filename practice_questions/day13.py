# 📅 Generators in Python – Assignment / Practice Questions
# 🟢 Easy Level (Basics)

# What is a generator in Python? How is it different from a function?

# def my_generatr(n):
#     i=1
#     while i<=n:
#         yield i
#         i+=1  
# result=my_generatr(10)
# for i in result:
#     print(i)

# Write a generator that yields numbers from 1 to 10.

# def my_generatr(n):
#     i=1
#     while i<=n:
#         yield i
#         i+=1  
# result=my_generatr(10)
# for i in result:
#     print(i)

# Write a generator to yield even numbers up to n.

# def my_generatr(n):
#     i=1
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1  
        
# num=int(input("Enter number : "))
# result=my_generatr(num)
# for i in result:
#     print(i)

# Write a generator that yields characters of a string one by one.

# def my_generatr(string1):
#     for char in string1:
#         yield char 
        
# string1="Hello how are you"
# result=my_generatr(string1)
# for i in result:
#     print(i)

# Write a generator to yield squares of numbers from 1 to n.

# def my_generatr(n):
#     i=1
#     while i<=n:
#         yield i*i
#         i+=1  
        
# num=int(input("Enter number : "))
# result=my_generatr(num)
# for i in result:
#     print(i)


# 🟡 Medium Level (Logic Building)

# Write a generator to generate Fibonacci series up to n terms.

# def my_generatr(n):
#     a,b=0,1
#     i=1
#     while i<=n:
#         yield a
#         a,b=b,a+b
#         i+=1

# num=int(input("Enter number : "))
# result=my_generatr(num)
# for i in result:
#     print(i)

# Write a generator to yield prime numbers up to n.

# def my_generatr(n):
#     for i in range(2, n + 1):
#         is_prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield i

# num=int(input("Enter number : "))
# result=my_generatr(num)
# for i in result:
#     print(i)

# Write a generator to yield elements of a list in reverse order.

# def my_generatr(list1):
#     for i in range(len(list1)-1,-1,-1):
#         yield list1[i]
        
# list1=[1,2,3,4,5,6,"Raushan",8,9,10,"hello"]
# result=my_generatr(list1)
# for i in result:
#     print(i)
    
# Write a generator that reads a file line by line.

# def my_generatr():
#     with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r") as fh:
#         for line in fh:
#             yield line

    
# result=my_generatr()
# for i in result:
#     print(i,end=" ")
    


# Write a generator to yield numbers divisible by both 3 and 5.

# def my_generatr(num):
#     i=1
#     while i<=num:
#         if i%3==0 and i%5==0:
#             yield i
#         i+=1
        

# num=int(input("Enter number : "))
# result=my_generatr(num)
# for i in result:
#     print(i)


# 🔴 Hard Level (Advanced)

# Write a generator that flattens a nested list.

def my_generatr(list1):
    for i in range(len(list1)):
        if type(list1[i])==list:
            for j in range(len(list1[i])):
                yield list1[i][j]
                
        else:
            yield list1[i]
        
list1=[1,2,3,4,5,[6,"Raushan"],8,9,10,"hello"]
result=my_generatr(list1)
for i in result:
    print(i)

# Write a generator that produces an infinite sequence of natural numbers.

# def natural_numbers():
#     n = 1
#     while True:        # infinite loop
#         yield n
#         n += 1

# gen = natural_numbers()

# for i in gen:
#     if i > 10:
#         break
#     print(i)


# Write a generator that yields unique elements from a list.

# def my_generatr(list1):
#     seen = set()
#     for item in list1:
#         if item not in seen:
#             seen.add(item)
#             yield item

# list1=[1,2,3,3,4,5,6,"Raushan",9,8,9,10,"hello"]
# result=my_generatr(list1)
# for i in result:
#     print(i)
    
# Write a generator that limits memory usage for large datasets.

# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,64,24,64]

# result = (x for x in list1 if x % 2 == 0)

# for i in result:
#     print(i)

# Write a generator expression to filter even numbers from a list.

# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,64,24,64]

# result = (x for x in list1 if x % 2 == 0)

# for i in result:
#     print(i)
