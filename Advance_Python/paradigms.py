#1️⃣ Procedural Programming Paradigm

def add(a, b):
    return a + b

# def subtract(a, b):
#     return a - b

# x = 10
# y = 5

# print(add(x, y))
# print(subtract(x, y))


#2️⃣ Object-Oriented Programming (OOP) Paradigm
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print(self.name, self.marks)

# s1 = Student("John", 90)
# s2 = Student("Lisa", 85)

# s1.display()
# s2.display()


#3️⃣ Functional Programming Paradigm

# numbers = [1, 2, 3, 4, 5]

# squares = list(map(lambda x: x*x, numbers))
# evens = list(filter(lambda x: x % 2 == 0, numbers))

# print(squares)
# print(evens)


#4️⃣ Imperative Programming Paradigm

# total = 0
# for i in range(1, 6):
#     total += i

# print(total)

# 5️⃣ Declarative Programming Paradigm

# numbers = [1, 2, 3, 4, 5]

# result = sum(numbers)
# print(result)

#6️⃣ Event-Driven Programming Paradigm

# def on_click():
#     print("Button clicked!")

# on_click()   # event triggered

#7️⃣ Concurrent / Parallel Programming Paradigm

import threading

def task():
    print("Task running")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
