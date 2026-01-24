# 📅 Decorators in Python – Assignment / Practice Questions
# 🟢 Easy Level (Basics)

# What is a decorator in Python? Explain in your own words.

# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

# Write a simple decorator that prints a message before a function runs.

# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

# Write a decorator that prints a message after a function runs.

# def my_decorator(func):
#     def wrapper():
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

# Write a decorator that counts how many times a function is called.
# def count_calls(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         count += 1
#         print(f"Function called {count} times")
#         return func()
#     return wrapper

# @count_calls
# def say_hello():
#     print("Hello")

# say_hello()
# say_hello()
# say_hello()



# Write a decorator to convert the output of a function to uppercase.

# def decor(func):
#     def inner():
#         result=func().upper()
#         return result
#     return inner 
# @decor
# def get_name():
#     name=input("Enter first name : ")
#     sirname=input("Enter sirname : ")
#     full_name=name+" "+sirname
#     return full_name

# print(get_name())

# 🟡 Medium Level (Logic Building)

# Write a decorator that measures the execution time of a function.


# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end - start:.6f} seconds")
#         return result
#     return wrapper

# @timer
# def example():
#     time.sleep(2)
#     print("Function executed")

# example()

# Write a decorator that checks if a number is positive before executing a function.

# def check_positive(func):
#     def wrapper(num):
#         if num > 0:
#             return func(num)
#         else:
#             print("Number is not positive")
#     return wrapper

# @check_positive
# def square(n):
#     return n * n

# num = int(input("Enter a number: "))
# print(square(num))

# Write a decorator that logs function name and arguments.

# def log_details(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function name: {func.__name__}")
#         print(f"Arguments: {args}")
#         print(f"Keyword arguments: {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @log_details
# def div1(a, b):
#     return a / b

# @log_details
# def div2(a, b, c):
#     return a / b / c

# print(div1(10, 5))
# print(div2(20, 5, 2))


# Write a decorator that restricts a function to only integer inputs.

# def only_integers(func):
#     def wrapper(*args):
#         for arg in args:
#             if not isinstance(arg, int):
#                 print("Only integer inputs are allowed")
#                 return
#         return func(*args)
#     return wrapper

# @only_integers
# def square(n):
#     return n * n

# @only_integers
# def add(a, b):
#     return a + b

# print(square(10))      # ✅ works
# print(square(10.8))    # ❌ blocked
# print(add(5, 6))       # ✅ works
# print(add(5, 2.5))     # ❌ blocked


# Write a decorator that repeats a function execution n times.

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     print("Hello", name)

# greet("Raushan")


# 🔴 Hard Level (Advanced)

# Write a decorator that handles exceptions inside a function.

# def deco(func):
#     def inner(a, b):
#         try:
#             return func(a, b)
#         except Exception as e:
#             print("Error occurred:", e)
#     return inner

# @deco
# def add(a, b):
#     return a / b   # exception example (ZeroDivisionError)

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# print(add(num1, num2))

# Write a decorator that checks user authentication before running a function.

# def deco(func):
#     def inner(n):
#         password=input("Enter a password : ")
#         if password=="Raushan@123":
#             return func(n)
#         else:
#             print("Invalid password ")
            
#     return inner

# @deco
# def numb(n):
#     return n*2

# num=int(input("Enter a nummber : "))
# print(numb(num))

# Write a decorator that validates input range (e.g. 1–100).

# def deco(func):
#     def inner(n):
#         if n>0 and n<100:
#             return func(n)
#         else:
#             print("number is out of range")
            
#     return inner

# @deco
# def numb(n):
#     return n*2

# n=float(input("Enter a nummber : "))
# print(numb(n))
    


# Write a decorator that caches function results (memoization).

# def memoize(func):
#     cache = {}
#     def wrapper(n):
#         if n in cache:
#             print("Returning cached result")
#             return cache[n]
#         result = func(n)
#         cache[n] = result
#         return result
#     return wrapper

# @memoize
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))
# print(factorial(5))   # cached result


# Write a decorator that can be used with or without arguments.

# Decorator usable with or without arguments

def repeat(func=None, times=1):
    if func is None:
        def decorator(func):
            return repeat(func, times)
        return decorator

    def wrapper(*args, **kwargs):
        for i in range(times):
            func(*args, **kwargs)
    return wrapper


@repeat
def greet1():
    print("Hello (no arguments)")

@repeat(times=3)
def greet2():
    print("Hello (with arguments)")


greet1()
greet2()
