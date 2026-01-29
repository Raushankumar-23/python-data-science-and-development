# 🔹 Day 15 – Classes & Objects (Job-Oriented Practice)
# 🟢 Easy (Foundation – All Roles)

# Create a User class with name and email and display details.

# class User:
#     def __init__(self,e,n):
#         self.name=n
#         self.email=e
        
        
#     def show_details(self):
#         print("Name : ",self.name,"\n","Email : ",self.email)
        
# details=User("Raushan","craushan781@gmail.com")
# details.show_details()




# Create a Product class and create multiple product objects.

# class Product:
#     def __init__(self,n):
#         self.name=n
        
#     def product_details(self,p):
#         self.price=p
#         print("Product Name : ",self.name,"\n","Price : ",self.price)
        
# prduct_det=Product("Laptop")
# prduct_det.product_details(55000)
# prduct_det=Product("Mobile")
# prduct_det.product_details(15000)
# prduct_det1=Product("LCD")
# prduct_det1.product_details(30000)




# Create a Student class and store marks, then print result.

# class Student:
#     def __init__(self, name, reg, marks):
#         self.name = name
#         self.reg_no = reg
#         self.marks = marks
        
#     def student_details(self):
#         print("Name:", self.name)
#         print("Registration No:", self.reg_no)

#         if self.marks >= 90:
#             print("Progress: Excellent")
#         elif self.marks >= 75:
#             print("Progress: Good")
#         elif self.marks >= 50:
#             print("Progress: Average")
#         elif self.marks >= 30:
#             print("Progress: Pass")
#         else:
#             print("Progress: Fail")

#         print("--------------------")
      
# s1 = Student("Raushan", 90, 85)
# s2 = Student("Rohit", 87, 60)
# s3 = Student("Aman", 75, 50)
# s4 = Student("Suresh", 78, 28)

# s1.student_details()
# s2.student_details()
# s3.student_details()
# s4.student_details()
      



# Create a class with one method that formats and returns data.

# class School:
#     def __init__(self, name, student, teacher):
#         self.name = name
#         self.no_of_student = student
#         self.no_of_teacher = teacher
        
#     def school_details(self):
#         return (
#             f"School Name: {self.name}\n"
#             f"Total Students: {self.no_of_student}\n"
#             f"Total Teachers: {self.no_of_teacher}"
#         )

# school1 = School("Gaya College Of Engineering", 1100, 65)
# print(school1.school_details())




# Create a class and update object data after creation.

# class Mobile:
#     def __init__(self):
#         self.model="Realme C11"
#         self.price=15000
        
        
#     def show_mobile(self):
#         print("Mobile : ",self.model)
#         print("Price : ",self.price)
        
# realme = Mobile()
# realme.show_mobile()

# # updating object data after creation
# realme.model = "Redmi 7s"
# realme.price = 20000

# realme.show_mobile()




# 🟡 Medium (Practical Use)

# Create an Employee class and calculate yearly salary.


# class Employee:
#     def __init__(self,name,post,salary):
#         self.name=name
#         self.post=post
#         self.monthly_salary=salary
        
        
#     def emmployee_details(self):
#         yearly_salary=self.monthly_salary*12
#         return (
#             f"Employee Name: {self.name}\n"
#             f"Employee Post : {self.post}\n"
#             f"Employee Yearly Salary : {yearly_salary}\n"
#         )
          
# Employee1=Employee("Raushan Kumar Chaurasiya","Data Scientist",56200)
# print(Employee1.emmployee_details())

  

# Create a BankAccount class with deposit and withdraw methods.

# class BankAccount:
#     def __init__(self, name, number):
#         self.name = name
#         self.account_number = number
#         self.current_balance = 10000
         
#     def deposit(self, amount):
#         self.current_balance += amount
#         return (
#             f"Customer Name: {self.name}\n"
#             f"Account Number: {self.account_number}\n"
#             f"{amount} Deposit Successful\n"
#             f"Current Balance: {self.current_balance}\n"
#         )
        
#     def withdraw(self, amount):
#         if self.current_balance >= amount:
#             self.current_balance -= amount
#             return (
#                 f"Customer Name: {self.name}\n"
#                 f"Account Number: {self.account_number}\n"
#                 f"{amount} Withdraw Successful\n"
#                 f"Current Balance: {self.current_balance}\n"
#             )
#         else:
#             return (
#                 f"Customer Name: {self.name}\n"
#                 f"Account Number: {self.account_number}\n"
#                 f"Insufficient Balance for {amount} withdrawal\n"
#                 f"Current Balance: {self.current_balance}\n"
#             )
 
# c1 = BankAccount("Raushan", 4013380441)
# print(c1.deposit(20000))

# c2 = BankAccount("Rohit", 4013390441)
# print(c2.deposit(10000))

# c3 = BankAccount("Raushan", 4013580441)
# print(c3.withdraw(20000))

# c4 = BankAccount("Rahul", 4018380441)
# print(c4.withdraw(10000))




# Create a class to store API test case details (for QA role).

# class APITestCase:
#     def __init__(self, test_id, api_name, method, expected_code, actual_code):
#         self.test_id = test_id
#         self.api_name = api_name
#         self.method = method
#         self.expected_code = expected_code
#         self.actual_code = actual_code

#     def test_result(self):
#         result = "PASS" if self.expected_code == self.actual_code else "FAIL"
#         return (
#             f"Test Case ID: {self.test_id}\n"
#             f"API Name: {self.api_name}\n"
#             f"HTTP Method: {self.method}\n"
#             f"Expected Status Code: {self.expected_code}\n"
#             f"Actual Status Code: {self.actual_code}\n"
#             f"Result: {result}\n"
#         )

# tc1 = APITestCase("TC_01", "/login", "POST", 200, 200)
# print(tc1.test_result())

# tc2 = APITestCase("TC_02", "/users", "GET", 200, 404)
# print(tc2.test_result())

        
    
    
    
# Create a class that stores dataset column info (for Data Analyst).

# class DatasetColumn:
#     def __init__(self, column_name, data_type, description, null_count, unique_count):
#         self.column_name = column_name
#         self.data_type = data_type
#         self.description = description
#         self.null_count = null_count
#         self.unique_count = unique_count

#     def column_info(self):
#         return (
#             f"Column Name: {self.column_name}\n"
#             f"Data Type: {self.data_type}\n"
#             f"Description: {self.description}\n"
#             f"Null Count: {self.null_count}\n"
#             f"Unique Count: {self.unique_count}\n"
#         )

# col1 = DatasetColumn("employee_name", "string", "Name of employee", 0, 120)
# col2 = DatasetColumn("salary", "float", "Monthly salary", 2, 95)

# print(col1.column_info())
# print(col2.column_info())



# Create a class and use one object’s data inside another object.

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Order:
#     def __init__(self, product):
#         self.product = product   # using another object

#     def show_order(self):
#         print("Product Name:", self.product.name)
#         print("Product Price:", self.product.price)


# p1 = Product("Laptop", 55000)
# order1 = Order(p1)

# order1.show_order()




# 🔴 Hard (Industry Thinking)



# Create a class to manage multiple users in a list.

# class UserManager:
#     def __init__(self):
#         self.users = []   # list to store multiple users

#     def add_user(self, name, email):
#         user = {
#             "name": name,
#             "email": email
#         }
#         self.users.append(user)

#     def show_users(self):
#         for user in self.users:
#             print("Name:", user["name"], "Email:", user["email"])

# manager = UserManager()

# manager.add_user("Raushan", "raushan@gmail.com")
# manager.add_user("Rohit", "rohit@gmail.com")
# manager.add_user("Aman", "aman@gmail.com")

# manager.show_users()





# Create a class that validates input data before storing.

# class Validation:
#     def __init__(self, age, email, marks):
#         if self.check_age(age) and self.check_email(email) and self.check_marks(marks):
#             self.age = age
#             self.email = email
#             self.marks = marks
#             print("All data is valid and stored")
#         else:
#             print("Invalid data. Not stored.")

#     def check_age(self, age):
#         return age > 0

#     def check_email(self, email):
#         return "@" in email

#     def check_marks(self, marks):
#         return 0 <= marks <= 100


# s1 = Validation(21, "rohit@gmail.com", 87)
# s1 = Validation(21, "rohit@gmail.com", -87)
# s1 = Validation(-21, "rohit@gmail.com", 87)
# s1 = Validation(21, "rohit#gmail.com", -87)

        
        
 
        
# Create a class that logs actions performed by objects.


# class ActionLogger:
#     def __init__(self):
#         self.logs = []   # list to store actions

#     def log_action(self, action):
#         self.logs.append(action)

#     def show_logs(self):
#         for log in self.logs:
#             print(log)

# logger = ActionLogger()

# logger.log_action("User created")
# logger.log_action("Amount deposited")
# logger.log_action("Amount withdrawn")

# logger.show_logs()




# Create a class representing a backend model (User / Order).

# class User:
#     def __init__(self, user_id, name, email, role):
#         self.user_id = user_id
#         self.name = name
#         self.email = email
#         self.role = role

#     def get_user_data(self):
#         return {
#             "id": self.user_id,
#             "name": self.name,
#             "email": self.email,
#             "role": self.role
#         }


# u1 = User(1, "Raushan", "raushan@gmail.com", "admin")
# u2 = User(2, "Rohit", "rohit@gmail.com", "user")

# print(u1.get_user_data())
# print(u2.get_user_data())

# exampe-1
# class Order:
#     def __init__(self, order_id, product_name, price):
#         self.order_id = order_id
#         self.product_name = product_name
#         self.price = price

#     def show_order(self):
#         print("Order ID:", self.order_id)
#         print("Product:", self.product_name)
#         print("Price:", self.price)

# o1 = Order(101, "Laptop", 55000)
# o1.show_order()




# Create a reusable class that can be used in different projects.

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def get_data(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email
        }

    def show_data(self):
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Email:", self.email)


u1 = User(1, "Raushan", "raushan@gmail.com")
u2 = User(2, "Rohit", "rohit@gmail.com")

u1.show_data()
u2.show_data()
