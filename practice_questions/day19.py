# 🔹 31 Jan 2026 – Inheritance (Practice Questions)
# 🟢 Easy



# Create a parent class and a child class using single inheritance.

# # Parent class
# class Parent:
#     def cansing(self):
#         print("Parent can sing")


# # Child class (single inheritance)
# class Child(Parent):
#     def candance(self):
#         print("Child can dance")


# # Creating object of Child class
# c = Child()

# # Accessing parent class method
# c.cansing()

# # Accessing child class method
# c.candance()

   
   
   
    
# Create a base class Person and child class Student.

# # Base class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Child class
# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no


# # Creating Student object
# man = Student("Raushan", 21, 90)

# print(man.name)
# print(man.age)
# print(man.roll_no)



# Access parent class methods from child class.

# class Parent:
#     def __init__(self,parent_name,parent_age):
#         self.parent_name=parent_name
#         self.parent_age=parent_age
        
        
# class Child(Parent):
#     def __init__(self, parent_name, parent_age,child_name,child_age):
#         super().__init__(parent_name, parent_age)
#         self.child_name=child_name
#         self.child_age=child_age
        

# person=Child("Praod Bhagat",50,"Raushan Kumar",21)
# print(person.parent_name)
# print(person.parent_age)
# print(person.child_name)
# print(person.child_age)

        


# Use super() to call parent constructor.

#  # Base class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Child class
# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no


# # Creating Student object
# man = Student("Raushan", 21, 90)

# print(man.name)
# print(man.age)
# print(man.roll_no)





# Create a child class that adds new attributes.

# class Parent:
#     def __init__(self,parent_name,parent_age):
#         self.parent_name=parent_name
#         self.parent_age=parent_age
        
        
# class Child(Parent):
#     def __init__(self, parent_name, parent_age,child_name,child_age,child_college):
#         super().__init__(parent_name, parent_age)
#         self.child_name=child_name
#         self.child_age=child_age
#         self.child_college=child_college
        

# person=Child("Praod Bhagat",50,"Raushan Kumar",21,"GCE Gaya")
# print(person.parent_name)
# print(person.parent_age)
# print(person.child_name)
# print(person.child_age)
# print(person.child_college)





# 🟡 Medium


# Create multilevel inheritance (A → B → C).

# Multilevel inheritance (A → B → C)

# class GrandFather:
#     def cansing(self):
#         print("The grandfather can sing")


# class Father(GrandFather):
#     def candance(self):
#         print("The father can dance")


# class Child(Father):
#     def candraw(self):
#         print("The child can draw")


# child = Child()

# child.cansing()     # from GrandFather
# child.candance()    # from Father
# child.candraw()     # from Child




# Create an Employee base class and Developer child class.

# class Employee:
#     def __init__(self,name):
#         self.employee_name=name
        
        
# class Developer(Employee):
#     def __init__(self, name,department):
#         super().__init__(name)
#         self.department=department

# person=Developer("Raushan","Software Developmernt")
# print(person.employee_name)
# print(person.department)





# Override a method from parent class.

# class Animal:
#     def eat(self):
#         print("Animal can eat ")
#     def sleep(self):
#         print("Animal can sleep ")
#     def walk(self):
#         print("Animal can walk")
        
# class Lion(Animal):
#     def eat(self): # redefined function
#         print("Lion can eat")
   
# lion=Lion()
# lion.eat()





# Use inheritance to reuse validation logic.

# class General_Validation:
#     def check_age(self, age):
#         return age > 0

#     def check_email(self, email):
#         return "@" in email

#     def check_marks(self, marks):
#         return 0 <= marks <= 100


# class Check_validation(General_Validation):
#     def __init__(self, age, email, marks):
#         if self.check_age(age) and self.check_email(email) and self.check_marks(marks):
#             self.age = age
#             self.email = email
#             self.marks = marks
#             print("All data is valid and stored")
#         else:
#             print("Invalid data. Not stored.")


# #  Correct object creation (child class)
# s1 = Check_validation(21, "rohit@gmail.com", 87)
# s2 = Check_validation(21, "rohit@gmail.com", -87)
# s3 = Check_validation(-21, "rohit@gmail.com", 87)
# s4 = Check_validation(21, "rohit#gmail.com", 87)

        




# Create a QA-style base class and automation test child class.

# class Quality_assurance:
#     def check_email(self, email):
#         return "@" in email

#     def check_age(self, age):
#         return age > 18


# class Test_allowed(Quality_assurance):
#     def __init__(self, email, age):
#         if self.check_email(email) and self.check_age(age):
#             print("Allowed on all social media platforms")
#         elif self.check_email(email) and age <= 18:
#             print("Allowed only on YouTube and WhatsApp")
#         else:
#             print("Not allowed")


# #  Correct object creation
# person1 = Test_allowed("rohit@gmail.com", 20)
# person2 = Test_allowed("rohit@gmail.com", 15)
# person3 = Test_allowed("rohitgmail.com", 25)





# 🔴 Hard

# Create a backend-style model using inheritance.


# # Base model
# class BaseModel:
#     def __init__(self, id, created_at, updated_at):
#         self.id = id
#         self.created_at = created_at
#         self.updated_at = updated_at


# # User model
# class User(BaseModel):
#     def __init__(self, id, created_at, updated_at, username, email):
#         super().__init__(id, created_at, updated_at)
#         self.username = username
#         self.email = email


# # Product model
# class Product(BaseModel):
#     def __init__(self, id, created_at, updated_at, name, price):
#         super().__init__(id, created_at, updated_at)
#         self.name = name
#         self.price = price


# # Order model
# class Order(BaseModel):
#     def __init__(self, id, created_at, updated_at, user_id, total_amount):
#         super().__init__(id, created_at, updated_at)
#         self.user_id = user_id
#         self.total_amount = total_amount


# #  Object creation
# user1 = User(1, "2025-01-01", "2025-01-10", "rohit", "rohit@gmail.com")
# product1 = Product(101, "2025-01-02", "2025-01-12", "Laptop", 55000)
# order1 = Order(5001, "2025-01-05", "2025-01-15", user1.id, 55000)

# # Accessing object data
# print(user1.username, user1.email)
# print(product1.name, product1.price)
# print(order1.user_id, order1.total_amount)





# Create a base Account class and child SavingsAccount.

# class Account:
#     def __init__(self, account_number, account_holder_name, balance):
#         self.account_number = account_number
#         self.account_holder_name = account_holder_name
#         self.balance = balance


# class Saving_account(Account):
#     def __init__(self, account_number, account_holder_name, balance):
#         super().__init__(account_number, account_holder_name, balance)
#         self.minimum_balance = 1000
#         self.interest_rate = 6.8   # percentage

#     def calculate_interest(self):
#         time = 1  # year
#         if self.balance >= self.minimum_balance:
#             interest = (self.balance * self.interest_rate * time) / 100
#             print("Hi",self.account_holder_name)
#             print(f"Your interest is: {interest}")
#         else:
#             print("Hi",self.account_holder_name)
#             print(f"Please maintain minimum balance: {self.minimum_balance}")
#             print("Otherwise monthly fine: ₹100")

# c1=Saving_account(5647832919,"Raushan",4500)
# c1.calculate_interest()
# c2=Saving_account(5649832919,"Rohit",500)
# c2.calculate_interest()




# Override methods and compare parent vs child behavior.


# class Account:
#     def __init__(self, account_number, account_holder_name, balance, account_type):
#         self.account_number = account_number
#         self.account_holder_name = account_holder_name
#         self.balance = balance
#         self.account_type = account_type

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. Balance left: {self.balance}")
#         else:
#             print("Insufficient balance")


# class SavingsAccount(Account):
#     def __init__(self, account_number, account_holder_name, balance, account_type):
#         super().__init__(account_number, account_holder_name, balance, account_type)
#         self.minimum_balance = 1000
#         self.penalty_fee = 100

#     def withdraw(self, amount):   # overridden method
#         if self.balance - amount >= self.minimum_balance:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. Balance left: {self.balance}")
#         else:
#             self.balance -= self.penalty_fee
#             print(f"Minimum balance violated! Penalty charged: {self.penalty_fee}")
#             print(f"Current balance: {self.balance}")


# acc1 = Account(101, "Rohit", 2000, "General")
# acc1.withdraw(1500)

# acc2 = SavingsAccount(102, "Rohit", 2000, "Savings")
# acc2.withdraw(1500)

        



# Create inheritance chain for data pipeline classes.

# # Base pipeline class
# class DataPipeline:
#     def start(self):
#         print("Pipeline started")

#     def validate(self):
#         print("Validating data")

#     def stop(self):
#         print("Pipeline stopped")


# # Intermediate ETL pipeline
# class ETLPipeline(DataPipeline):
#     def extract(self):
#         print("Extracting data")

#     def transform(self):
#         print("Transforming data")

#     def load(self):
#         print("Loading data")


# # Child pipeline: CSV data
# class CSVETLPipeline(ETLPipeline):
#     def extract(self):
#         print("Extracting data from CSV file")

#     def load(self):
#         print("Loading data into database")


# # Child pipeline: API data
# class APIETLPipeline(ETLPipeline):
#     def extract(self):
#         print("Extracting data from API")

#     def load(self):
#         print("Loading data into data warehouse")


# # 🔹 Usage
# csv_pipeline = CSVETLPipeline()
# csv_pipeline.start()
# csv_pipeline.validate()
# csv_pipeline.extract()
# csv_pipeline.transform()
# csv_pipeline.load()
# csv_pipeline.stop()





# Design reusable parent class for multiple child classes.


# Reusable parent class
class Notification:
    def send(self, message):
        print(f"Sending message: {message}")


# Child class 1
class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")


# Child class 2
class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")


# Child class 3
class PushNotification(Notification):
    def send(self, message):
        print(f"Push notification sent: {message}")


# Example usage
n1 = EmailNotification()
n2 = SMSNotification()
n3 = PushNotification()

n1.send("Hello User")
n2.send("Hello User")
n3.send("Hello User")
