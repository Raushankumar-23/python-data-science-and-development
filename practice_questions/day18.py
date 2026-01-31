# 🔹 Day 16 – Constructors, Instance vs Class Variables (Job-Oriented)
# 🟢 Easy

# Create a class using constructor to initialize user data.

# class User:
#     def __init__(self):
#         self.id=int(input("Enter user id : "))
#         self.name=input("Enter your name : ")
#         self.salary=float(input("Enter your salary : "))
        
        
#     def display_data(self):
#         print("User data")
#         print("User id : ",self.id)
#         print("User name : ",self.name)
#         print("User Salary : ",self.salary)
        
        
# a=User()
# a.display_data()




# Create a class with default and parameterized constructor.

# class User:
#     def __init__(self, id=None, name=None, salary=None):
#         if id is None and name is None and salary is None:
#             # Default constructor behavior
#             self.id = int(input("Enter user id : "))
#             self.name = input("Enter your name : ")
#             self.salary = float(input("Enter your salary : "))
#         else:
#             # Parameterized constructor behavior
#             self.id = id
#             self.name = name
#             self.salary = salary

#     def display_data(self):
#         print("\nUser data")
#         print("User id :", self.id)
#         print("User name :", self.name)
#         print("User salary :", self.salary)


# #object for default 
# u1 = User()
# u1.display_data()
# #object for parametrised
# u2 = User(121, "Raushan", 95000)
# u2.display_data()



# Create multiple objects and print their constructor values.

# class User:
#     def __init__(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary
        
        
#     def display_data(self):
#         print("\nUser data")
#         print("User id : ",self.id)
#         print("User name : ",self.name)
#         print("User Salary : ",self.salary)
        
        
# a1 = User(121, "Raushan", 95000)
# a2 = User(122, "Amit", 72000)
# a3 = User(123, "Rohit", 68000)

# a1.display_data()
# a2.display_data()
# a3.display_data()




# Create a class where constructor prints a welcome message.

# class Greeting:
#     def __init__(self, name):
#         self.name = name
#         print(f"Welcome {self.name}")


# m1 = Greeting("Raushan")




# Initialize object values dynamically using constructor.

# class User:
#     def __init__(self):
#         self.id=int(input("Enter user id : "))
#         self.name=input("Enter your name : ")
#         self.salary=float(input("Enter your salary : "))
        
        
#     def display_data(self):
#         print("User data")
#         print("User id : ",self.id)
#         print("User name : ",self.name)
#         print("User Salary : ",self.salary)
        
        
# a=User()
# a.display_data()






# 🟡 Medium

# Create a class to track total number of users using class variable.

# class User:
#     total_users = 0   # class variable

#     def __init__(self, name):
#         self.name = name
#         User.total_users += 1   # increment when object is created

#     def display(self):
#         print("User name:", self.name)


# # Creating objects
# u1 = User("Raushan")
# u2 = User("Amit")
# u3 = User("Rohit")

# # Access class variable
# print("Total users:", User.total_users)





# Create a class where instance variables differ per object.

# class Student:
#     def __init__(self, roll_no, name):
#         self.roll_no = roll_no   # instance variable
#         self.name = name        # instance variable

#     def display(self):
#         print("Roll No:", self.roll_no, "| Name:", self.name)


# # Creating multiple objects
# s1 = Student(101, "Raushan")
# s2 = Student(102, "Amit")
# s3 = Student(103, "Rohit")

# s1.display()
# s2.display()
# s3.display()





# Create a class where class variable is shared across all objects.


# class University:
#     university_name = "AKU University"   # class variable (shared)

#     def __init__(self, college, course):
#         self.college_name = college       # instance variable
#         self.no_of_course = course        # instance variable

#     def show(self):
#         print("University:", University.university_name)
#         print("College:", self.college_name)
#         print("Total courses:", self.no_of_course)
#         print()


# c1 = University("Gaya College of Engineering", 8)
# c2 = University("Government College Jahanabad", 6)

# c1.show()
# c2.show()





# Modify instance variable of one object and check others.


# class User:
#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary   # instance variable

#     def display_data(self):
#         print("User id:", self.id)
#         print("User name:", self.name)
#         print("User salary:", self.salary)
#         print()


# u1 = User(121, "Raushan", 20000)
# u2 = User(122, "Amit", 15000)

# u1.salary = 30000   # modifying only u1

# u1.display_data()
# u2.display_data()




# Modify class variable and observe change in all objects.

# class Company:
#     company_name = "ABC Pvt Ltd"   # class variable

#     def __init__(self, emp_id, name):
#         self.emp_id = emp_id       # instance variable
#         self.name = name

#     def display(self):
#         print("Employee ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Company:", Company.company_name)
#         print()


# e1 = Company(101, "Raushan")
# e2 = Company(102, "Amit")
# #modify class
# Company.company_name = "XYZ Technologies"

# e1.display()
# e2.display()




# 🔴 Hard (Real-World)

# Create an APIRequest class that counts total requests made.

# class APIRequest:
#     total_requests = 0   # class variable (shared)

#     def __init__(self, endpoint):
#         self.endpoint = endpoint
#         APIRequest.total_requests += 1   # count every request

#     def show(self):
#         print("Endpoint:", self.endpoint)
#         print("Total requests so far:", APIRequest.total_requests)
#         print()


# r1 = APIRequest("/login")
# r2 = APIRequest("/get-user")
# r3 = APIRequest("/update-profile")

# r1.show()
# r2.show()
# r3.show()




# Create a Dataset class that tracks number of datasets loaded.

# class Dataset:
#     total_datasets = 0   # class variable (shared)

#     def __init__(self, name):
#         self.name = name
#         Dataset.total_datasets += 1   # increment on load

#     def show(self):
#         print("Dataset name:", self.name)
#         print("Total datasets loaded:", Dataset.total_datasets)
#         print()


# d1 = Dataset("users.csv")
# d2 = Dataset("sales.csv")
# d3 = Dataset("logs.csv")

# d1.show()
# d2.show()
# d3.show()



# Create a TestCase class where each object has unique ID but shared status.

# class TestCase:
#     status = "NOT RUN"   # class variable (shared by all objects)

#     def __init__(self, test_id):
#         self.test_id = test_id   # instance variable (unique)

#     def show(self):
#         print("Test ID:", self.test_id)
#         print("Status:", TestCase.status)
#         print()


# t1 = TestCase("TC_01")
# t2 = TestCase("TC_02")
# t3 = TestCase("TC_03")

# t1.show()
# t2.show()
# t3.show()
# #change status
# TestCase.status = "PASSED"

# t1.show()
# t2.show()
# t3.show()


# Create a backend-style model using constructor + class variables.

# class UserModel:
#     total_users = 0          # class variable (shared)
#     platform = "WebApp"      # class variable (shared)

#     def __init__(self, user_id, username, email):
#         self.user_id = user_id     # instance variable
#         self.username = username
#         self.email = email
#         UserModel.total_users += 1

#     def display(self):
#         print("User ID:", self.user_id)
#         print("Username:", self.username)
#         print("Email:", self.email)
#         print("Platform:", UserModel.platform)
#         print()

# u1 = UserModel(1, "raushan", "raushan@gmail.com")
# u2 = UserModel(2, "amit", "amit@gmail.com")
# u3 = UserModel(3, "rohit", "rohit@gmail.com")

# u1.display()
# u2.display()
# u3.display()

# print("Total users:", UserModel.total_users)



# Create a class that logs how many objects were created and destroyed.

class Logger:
    created_count = 0    # class variable
    destroyed_count = 0  # class variable

    def __init__(self):
        Logger.created_count += 1
        print("Object created")
        print("Total created:", Logger.created_count)

    def __del__(self):
        Logger.destroyed_count += 1
        print("Object destroyed")
        print("Total destroyed:", Logger.destroyed_count)


o1 = Logger()
o2 = Logger()
o3 = Logger()
#destoy object
del o1
del o2
del o3
