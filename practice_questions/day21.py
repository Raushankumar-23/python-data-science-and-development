# 🔹 02 Feb 2026 – Dunder (Magic) Methods
# 🟢 Easy

# Implement __init__() in a class.

# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def show_data(self):
#         print(f"Name of user is  : {self.name}")
#         print(f"Age of user is  : {self.age}")
    
    
# u1=User("Raushan Kumar chaurasiya ",21)
# u1.show_data()

# Use __str__() to print object details.

# class User:
#     def __init__(self, name):
#         self.name = name
        
#     def __str__(self):
#         return f"{self.name} is string data type"


# u1 = User("Raushan Kumar Chaurasiya")
# print(u1)



# Use __len__() in a custom class.

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show_data(self):
#         print(f"Name of user is : {self.name}")
        
#     def __len__(self):
#         return len(self.name)   # must return an int

# u1 = User("Raushan Kumar Chaurasiya", 21)

# u1.show_data()
# print(len(u1))




# Use __repr__() for debugging output.

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def __repr__(self):
#         return f"User(name='{self.name}', age={self.age})"

# u1 = User("Raushan Kumar Chaurasiya", 21)

# print(u1)        # uses __repr__
# u1               # interpreter also uses __repr__

# User(name='Raushan Kumar Chaurasiya', age=21)





# Compare two objects using __eq__().


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age

# u1 = User("Raushan", 21)
# u2 = User("Raushan", 21)
# u3 = User("Aman", 22)

# print(u1 == u2)
# print(u1 == u3)




# 🟡 Medium

# Overload + operator using __add__().


# class User:
#     def __init__(self, salary):
#         self.salary = salary
        
#     def __add__(self, other):
#         if not isinstance(other, User):
#             return NotImplemented
#         return self.salary + other.salary

# u1 = User(30000)
# u2 = User(45000)

# print(u1 + u2)



# Use __lt__() and __gt__() for comparisons.


# class User:
#     def __init__(self, salary):
#         self.salary = salary
        
#     def __lt__(self, other):
#         if not isinstance(other, User):
#             return NotImplemented
#         return self.salary < other.salary
        
#     def __gt__(self, other):
#         if not isinstance(other, User):
#             return NotImplemented
#         return self.salary > other.salary
        
#     def __repr__(self):
#         return f"User(salary={self.salary})"

# u1 = User(30000)
# u2 = User(45000)

# print(u1 < u2)
# print(u1 > u2)



# Implement __getitem__() in a class.

# class Student:
#     def __init__(self, marks):
#         self.marks = marks
        
#     def __getitem__(self, index):
#         return self.marks[index]

# s = Student([78, 85, 92])

# print(s[0])
# print(s[1])
# print(s[-1])


# Use __call__() to make object callable.

# class Greeter:
#     def __init__(self, name):
#         self.name = name
        
#     def __call__(self):
#         print(f"Hello, {self.name}!")

# g = Greeter("Raushan")

# g()   # object behaves like a function


# Create class behaving like a list or counter.

# class MyList:
#     def __init__(self, items):
#         self.items = items
        
#     def __getitem__(self, index):
#         return self.items[index]
        
#     def __len__(self):
#         return len(self.items)
        
#     def __repr__(self):
#         return f"MyList({self.items})"

# ml = MyList([10, 20, 30, 40])

# print(ml[0])
# print(ml[2])
# print(len(ml))
# print(ml)

# 🔴 Hard

# Build a custom numeric class with operators.

# class MyNumber:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         if not isinstance(other, MyNumber):
#             return NotImplemented
#         return MyNumber(self.value + other.value)

#     def __sub__(self, other):
#         if not isinstance(other, MyNumber):
#             return NotImplemented
#         return MyNumber(self.value - other.value)

#     def __mul__(self, other):
#         if not isinstance(other, MyNumber):
#             return NotImplemented
#         return MyNumber(self.value * other.value)

#     def __eq__(self, other):
#         return self.value == other.value

#     def __lt__(self, other):
#         return self.value < other.value

#     def __repr__(self):
#         return f"MyNumber({self.value})"

# a = MyNumber(10)
# b = MyNumber(5)

# print(a + b)
# print(a - b)
# print(a * b)

# print(a == b)
# print(a < b)




# Implement dunder methods in backend models.


# class User:
#     def __init__(self, user_id, name, email):
#         self.user_id = user_id
#         self.name = name
#         self.email = email

#     def __str__(self):
#         return f"{self.name} <{self.email}>"

#     def __repr__(self):
#         return f"User(id={self.user_id}, name='{self.name}', email='{self.email}')"

#     def __eq__(self, other):
#         if not isinstance(other, User):
#             return NotImplemented
#         return self.user_id == other.user_id

#     def __lt__(self, other):
#         return self.user_id < other.user_id

#     def __len__(self):
#         return len(self.name)

#     def __hash__(self):
#         return hash(self.user_id)

# u1 = User(1, "Raushan", "raushan@gmail.com")
# u2 = User(2, "Aman", "aman@gmail.com")
# u3 = User(1, "Raushan", "raushan@gmail.com")

# print(u1)            # __str__
# print(repr(u1))      # __repr__
# print(u1 == u3)      # __eq__
# print(len(u1))       # __len__

# users = [u2, u1]
# print(sorted(users)) # __lt__

# user_set = {u1, u3}
# print(user_set)      # __hash__




# Create a dataset class with custom behaviors.

# class Dataset:
#     def __init__(self, data, name="Dataset"):
#         self.data = data
#         self.name = name

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, index):
#         return self.data[index]

#     def __iter__(self):
#         return iter(self.data)

#     def __str__(self):
#         return f"{self.name} with {len(self)} records"

#     def __repr__(self):
#         return f"Dataset(name='{self.name}', size={len(self)})"

#     def __call__(self):
#         return {
#             "name": self.name,
#             "size": len(self),
#             "preview": self.data[:3]
#         }


# data = [10, 20, 30, 40, 50]
# ds = Dataset(data, name="Training Data")

# print(ds)              # __str__
# print(repr(ds))        # __repr__
# print(len(ds))         # __len__
# print(ds[2])           # __getitem__

# for item in ds:        # __iter__
#     print(item)

# print(ds())            # __call__




# Design clean printable objects for logs.


# class LoggableUser:
#     def __init__(self, user_id, name, role):
#         self.user_id = user_id
#         self.name = name
#         self.role = role

#     def __str__(self):
#         return f"User[{self.user_id}] {self.name} ({self.role})"

#     def __repr__(self):
#         return (
#             f"LoggableUser(user_id={self.user_id}, "
#             f"name='{self.name}', role='{self.role}')"
#         )

# user = LoggableUser(101, "Raushan", "Admin")

# print(user)          # production-style log
# print(repr(user))    # debug log


# Combine multiple dunder methods in one class.

class User:
    def __init__(self, user_id, name, salary):
        self.user_id = user_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}', salary={self.salary})"

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id

    def __lt__(self, other):
        return self.salary < other.salary

    def __add__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return User(self.user_id, self.name, self.salary + other.salary)

    def __call__(self):
        return f"User {self.name} earns ₹{self.salary}"

u1 = User(1, "Raushan", 30000)
u2 = User(2, "Aman", 45000)

print(u1)              # __str__
print(repr(u1))        # __repr__

print(len(u1))         # __len__

print(u1 == u2)        # __eq__
print(u1 < u2)         # __lt__

u3 = u1 + u2           # __add__
print(u3)

print(u1())            # __call__
