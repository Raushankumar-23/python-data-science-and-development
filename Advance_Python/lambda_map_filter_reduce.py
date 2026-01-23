# Lambda 
#normal function
# def double(a):
#     return a*2

# sum=double(5)

# use lambda function

# double= lambda x: x*2
# cube = lambda x:x**3
# print(double(5))
# print(cube(5))

# average = lambda n1,n2,n3,n4 : (n1+n2+n3+n4)/4 
# print(average(3,4,5,7))

# Nested lambda
# add= lambda x=10 : (lambda y : x+y )
# a=add()
# print(a(30))

# map() filter() reduce()

# def cube(x):
#     return x**3

# l=[1,2,3,4,5]

# newl = list(map(cube,l))
# print(newl)

# cube = lambda t:t**3
# t=[1,2,3,4,5]
# newl = list(map(cube,t))
# print(newl)

# filter

# def filter_function(a):
#     return a>4

# l=[1,2,3,4,5,6]

# newnewl = list(filter(filter_function,l))
# print(newnewl)
    
# num=lambda l:l>4
# l=[1,2,3,4,5,6]
# newnewl = list(filter(num,l))
# print(newnewl)

# map function
# items = [1,2,3,4,5,6]
# new_items=list(map(lambda x:x*x,items))
# print(new_items)


# filter function
# items = [1,2,3,4,5,6]
# new_items=list(filter(lambda x:(x%2==0),items))
# print(new_items)

# reduce function
from functools import reduce
items = [1,2,3,4,5,6]
print(items)