# 📅 Iterators in Python – Assignment / Practice Questions
# 🟢 Easy Level (Basics)

# 🟢 Easy Level (Programs)

# Write a program to create an iterator from a list and print its elements using next().

# list1=[1,2,3,4,5,6,7,8,9,10]
# iterator=iter(list1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# for i in iterator:
#     print(i)

# Write a program to iterate over a string using iter() and next().

# text = "Hello Raushan How are You"

# iterator = iter(text)

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

# Write a program to check whether a given object is iterable or an iterator.

# text = "Hello Raushan How are You"

# # Check iterable
# if hasattr(text, "__iter__"):
#     print("Object is Iterable")

# # Create iterator
# iterator = iter(text)

# # Check iterator
# if hasattr(iterator, "__next__"):
#     print("Object is an Iterator")


# Write a program to convert a tuple into an iterator and print all its elements.

# num=(1,2,3,4,5,6,7)
# itera=iter(num)
# while True:
#     try:
#         print(next(itera))
#     except StopIteration:
#         break

# Write a program to iterate through a list using an iterator and print all values.

# list1=[1,2,3,4,5,6,7,8,9,10]
# iterator=iter(list1)
# while True:
#     try:
#         print(next(iterator))
        
#     except StopIteration:
#         break

# 🟡 Medium Level (Programs)

# Write a program to create a custom iterator class that prints numbers from 1 to n.

# class Fantastic:
#     def __init__(self, n):
#         self.n = n
#         self.num = 1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num <= self.n:
#             value = self.num
#             self.num += 1
#             return value
#         else:
#             raise StopIteration
        
# FF = Fantastic(10)

# for i in FF:
#     print(i)


# Write a program to create an iterator that generates even numbers up to n.

# class Fantastic:
#     def __init__(self, n):
#         self.n = n
#         self.num = 2   # even numbers start from 2
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num <= self.n:
#             value = self.num
#             self.num += 2   # jump to next even
#             return value
#         else:
#             raise StopIteration

        
# FF = Fantastic(10)

# for i in FF:
#     print(i)


# Write a program to iterate through dictionary keys and values using an iterator.

# dicto={
#     "name":"Raushan",
#     "Branch":"Computer Science And Engineering",
#     "College":"Gaya College Of Engineering Gaya",
#     "CGPP":8.23
# }

# itor=iter(dicto.keys())
# # key
# while True:
#     try:
#         print("key:",next(itor))
        
#     except StopIteration:
#         break

# itor=iter(dicto.values())

# while True:
#     try:
#         print("Value:",next(itor))
        
#     except StopIteration:
#         break

# other mthod
# dicto = {
#     "name": "Raushan",
#     "Branch": "Computer Science And Engineering",
#     "College": "Gaya College Of Engineering Gaya",
#     "CGPP": 8.23
# }

# itor = iter(dicto.items())

# while True:
#     try:
#         key, value = next(itor)
#         print(key, ":", value)
#     except StopIteration:
#         break

# Write a program to manually iterate over a list using next() and handle StopIteration.

# list1=[1,2,3,4,5,6,7,8,9,10]
# itor=iter(list1)
# while True:
#     try:
#         print(next(itor))
        
#     except StopIteration:
#         break
    

# Write a program to create an iterator that returns the square of numbers.

# class Fantastic:
#     def __init__(self, n):
#         self.n = n
#         self.num = 1   # even numbers start from 2
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num <= self.n:
#             value = self.num*self.num
#             self.num += 1   # jump to next even
#             return value
#         else:
#             raise StopIteration

        
# FF = Fantastic(10)

# for i in FF:
#     print(i)


# 🔴 Hard Level (Programs)

# Write a program to create a custom iterator for the Fibonacci series.

# class Fibonacci:
#     def __init__(self, n):
#         self.n = n          # number of terms
#         self.count = 0
#         self.a = 0
#         self.b = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count < self.n:
#             value = self.a
#             self.a, self.b = self.b, self.a + self.b
#             self.count += 1
#             return value
#         else:
#             raise StopIteration

# fib = Fibonacci(10)

# for i in fib:
#     print(i)

# Write a program to create an iterator that reads a file line by line.

# def my_generatr(filename):
#     with open(filename, "r") as fh:
#         for line in fh:
#             yield line


# result = my_generatr(
#     r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt"
# )

# for i in result:
#     print(i, end="")

# Write a program to create an iterator that cycles through a list infinitely.

# class InfiniteCycle:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.lst:
#             raise StopIteration

#         value = self.lst[self.index]
#         self.index = (self.index + 1) % len(self.lst)  # reset to start
#         return value
    
    
# list1 = [1, 2, 3]
# cycle = InfiniteCycle(list1)

# count = 0
# for x in cycle:
#     print(x)
#     count += 1
#     if count == 10:   # limit, otherwise infinite
#         break


# Write a program to create an iterator that skips alternate elements in a list.

# list1=[1,2,3,4,5,6,7,8,9,10]
# iterator=iter(list1)
# while True:
#     try:
#         print(next(iterator))
#         next(iterator)
        
#     except StopIteration:
#         break
    
# Write a program to create a custom iterator that limits the number of iterations.
class LimitedIterator:
    def __init__(self, data, limit):
        self.data = data
        self.limit = limit
        self.index = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data) and self.count < self.limit:
            value = self.data[self.index]
            self.index += 1
            self.count += 1
            return value
        else:
            raise StopIteration
list1 = [10, 20, 30, 40, 50, 60]

itr = LimitedIterator(list1, 3)   # limit = 3

for i in itr:
    print(i)
