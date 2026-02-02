# 🔹 03 Feb 2026 – Encapsulation & Abstraction
# 🟢 Easy

# Create private variables using __.

# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password   # private variable

#     def show_user(self):
#         print("Name:", self.name)
#         print("Password:", self.__password)

# u1 = User("Raushan", "secret123")
# u1.show_user()




# Access private variables using methods.


# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password

#     def get_password(self):
#         return self.__password

#     def set_password(self, new_password):
#         if len(new_password) >= 6:
#             self.__password = new_password
#         else:
#             print("Password must be at least 6 characters long")

# u1 = User("Raushan", "secret123")

# print(u1.get_password())      # access private variable

# u1.set_password("newpass")    # modify private variable
# print(u1.get_password())




# Create getter and setter methods.


# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         return self.__age

#     def set_name(self, name):
#         self.__name = name

#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be positive")

# u1 = User("Raushan", 21)

# print(u1.get_name())
# print(u1.get_age())

# u1.set_name("Aman")
# u1.set_age(25)

# print(u1.get_name())
# print(u1.get_age())



# Protect sensitive data in a class.

# class SecureUser:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

#     def get_password(self):
#         return "******"

#     def set_password(self, new_password):
#         if len(new_password) >= 6:
#             self.__password = new_password
#         else:
#             print("Password must be at least 6 characters long")

#     def verify_password(self, password):
#         return self.__password == password

#     def __str__(self):
#         return f"User(username={self.username})"

# u1 = SecureUser("raushan", "secret123")

# print(u1)                       # safe output
# print(u1.get_password())        # masked

# print(u1.verify_password("123"))       # False
# print(u1.verify_password("secret123")) # True

# u1.set_password("newpass")





# Validate input before assignment.

# class User:
#     def __init__(self, username, age):
#         self.__username = None
#         self.__age = None
#         self.set_username(username)
#         self.set_age(age)

#     def set_username(self, username):
#         if isinstance(username, str) and len(username) >= 3:
#             self.__username = username
#         else:
#             raise ValueError("Username must be a string with at least 3 characters")

#     def set_age(self, age):
#         if isinstance(age, int) and age > 0:
#             self.__age = age
#         else:
#             raise ValueError("Age must be a positive integer")

#     def get_username(self):
#         return self.__username

#     def get_age(self):
#         return self.__age

# u1 = User("Raushan", 21)

# print(u1.get_username())
# print(u1.get_age())

# # Invalid input examples
# # User("Ra", 21)       → ValueError
# # User("Aman", -5)     → ValueError



# 🟡 Medium

# Use abc module to create abstract class.

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass

# class UPIPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using UPI")

# class CardPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Card")

# p1 = UPIPayment()
# p2 = CardPayment()

# p1.pay(500)
# p2.pay(1200)



# Create abstract method and implement in child.

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# r = Rectangle(10, 5)
# print("Area of rectangle:", r.area())




# Build abstract data processor class.

# from abc import ABC, abstractmethod

# # Abstract base class
# class DataProcessor(ABC):

#     @abstractmethod
#     def process(self, data):
#         pass


# # Child class 1: Number processing
# class NumberProcessor(DataProcessor):
#     def process(self, data):
#         return f"Sum = {sum(data)}"


# # Child class 2: String processing
# class StringProcessor(DataProcessor):
#     def process(self, data):
#         return f"Joined string = {' '.join(data)}"


# # Child class 3: Dictionary processing
# class DictProcessor(DataProcessor):
#     def process(self, data):
#         return f"Total keys = {len(data)}"


# # Polymorphic function
# def run_processor(processor, data):
#     return processor.process(data)


# # Usage
# num_p = NumberProcessor()
# str_p = StringProcessor()
# dict_p = DictProcessor()

# print(run_processor(num_p, [10, 20, 30]))
# print(run_processor(str_p, ["Hello", "World"]))
# print(run_processor(dict_p, {"id": 1, "name": "Raushan"}))



# Hide internal logic using abstraction.


# from abc import ABC, abstractmethod

# class Vehicle(ABC):   # Abstract class
#     @abstractmethod
#     def start(self):
#         pass

# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts with kick")

# class Car(Vehicle):
#     def start(self):
#         print("Car starts with key")

# b = Bike()
# b.start()

# c = Car()
#c.start()



# Create abstraction for API services.





# 🔴 Hard

# Design secure backend model using encapsulation.

# Create abstract ML pipeline structure.

# Enforce method implementation using abstraction.

# Combine inheritance + abstraction.

# Build extensible architecture using abstract base classes.

# 🔹 04 Feb 2026 – OOP Practice (Mixed)

# Build a User Management System using OOP.

# Create a mini Banking System using all OOP concepts.

# Build a Test Automation Framework structure.

# Design data processing classes for analytics.

# Refactor old procedural code into OOP.




# 🔹 05–06 Feb 2026 – OOP Mini Project
# 🎯 Mini Project Ideas (Choose ONE)

# Bank Management System

# Student Result Management System

# API Test Case Manager (QA role)

# Dataset Loader & Analyzer (Data Analyst)

# Backend User & Order Management

# Project Must Include:

# Classes & Objects

# Constructors

# Inheritance

# Polymorphism

# Encapsulation

# Dunder methods

# Decorators / Generators (bonus)