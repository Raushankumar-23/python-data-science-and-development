
# 🔹 01 Feb 2026 – Polymorphism & Method Overriding
# 🟢 Easy

# Create two classes with same method name.

# class Owl:
#     def fly(self):
#         print("The owl can fly")
        
# class Airoplane:
#     def fly(self):
#         print("The Airoplane can fly")
        
# class Person:
#     def code(self):
#         print("The person cannot fly, but can code!")
        
        
# def canfly(obj):
#     if hasattr(obj, 'fly'):
#         obj.fly()
#     else:
#         print("This object cannot fly")

    
    
# airplane=Airoplane()
# owl=Owl()
# person=Person()

# canfly(owl)
# canfly(airplane)
# #canfly(person)  #create error





# Call same method on different objects.

# class Owl:
#     def fly(self):
#         print("Owl flies silently")

# class Airplane:
#     def fly(self):
#         print("Airplane flies with engines")

# def canfly(obj):
#     obj.fly()   # same method name

# owl = Owl()
# plane = Airplane()

# canfly(owl)
# canfly(plane)





# Override a parent method in child class.


# class Animal:
#     def eat(self):
#         print("Animal can eat in general")
#     def sleep(self):
#         print("Animal can sleep in general")
#     def walk(self):
#         print("Animal can Walk in general")
   
# class Lion(Animal):
#     def eat(self):
#         print("Lion can eat in general")
        
# lion=Lion()
# lion.eat()    





# Show different outputs using same method name.

# class Animal:
#     def eat(self):
#         print("Animal can eat in general")

# class Lion(Animal):
#     def eat(self):
#         print("Lion can eat in general")

# lion = Lion()
# lion.eat()
# animal = Animal()
# animal.eat()






# # Create polymorphism using function arguments.

# class Dog:
#     def speak(self):
#         print("Dog barks")

# class Cat:
#     def speak(self):
#         print("Cat meows")

# class Cow:
#     def speak(self):
#         print("Cow moos")

# def animal_sound(animal):
#     animal.speak()   # same function, different objects

# dog = Dog()
# cat = Cat()
# cow = Cow()

# animal_sound(dog)
# animal_sound(cat)
# animal_sound(cow)





# 🟡 Medium


# Create a class hierarchy with overridden methods.

# class LivingThing:
#     def eat(self):
#         print("Living things eat")

# class Animal(LivingThing):
#     def eat(self):
#         print("Animals eat food")

# class Human(LivingThing):
#     def eat(self):
#         print("Humans eat meals")

# class Cyborg(Animal, Human):
#     def eat(self):
#         print("Cyborg eats energy and food")


# l = LivingThing()
# a = Animal()
# h = Human()
# c = Cyborg()

# l.eat()
# a.eat()
# h.eat()
# c.eat()




# Use polymorphism to process different data types.

# class User:
#     def put_data(self):
#         self.id = int(input("Enter user id : "))
#         self.name = input("Enter your name : ")
#         self.salary = float(input("Enter your salary : "))
        
#     def display_data(self):
#         print("\nUser data")
#         print("User id :", self.id)
#         print("User name :", self.name)
#         print("User salary :", self.salary)


# class VIP_user(User):
#     def display_data(self):
#         print("\nVIP User data")
#         print("User id :", self.id)
#         print("User name :", self.name)
#         print("User salary :", self.salary)

# def show_details(user):
#     user.display_data()   # same method, different object

# u1 = User()
# u1.put_data()

# v1 = VIP_user()
# v1.put_data()

# show_details(u1)
# show_details(v1)




# Create a report generator with polymorphic methods.

# class Report:
#     def generate_report(self):
#         print("Generating generic report")


# class SalesReport(Report):
#     def generate_report(self):
#         print("Generating sales report with revenue details")


# class StudentReport(Report):
#     def generate_report(self):
#         print("Generating student performance report")


# class EmployeeReport(Report):
#     def generate_report(self):
#         print("Generating employee attendance report")


# def create_report(report):
#     report.generate_report()   # same method name


# r1 = SalesReport()
# r2 = StudentReport()
# r3 = EmployeeReport()

# create_report(r1)
# create_report(r2)
# create_report(r3)


# Implement polymorphism in API response classes.

# class APIResponse:
#     def build_response(self, data):
#         return {
#             "status": "success",
#             "data": data
#         }


# class JSONResponse(APIResponse):
#     def build_response(self, data):
#         return {
#             "status": "success",
#             "format": "json",
#             "payload": data
#         }


# class ErrorResponse(APIResponse):
#     def build_response(self, data):
#         return {
#             "status": "error",
#             "message": data
#         }

# def send_response(response_obj, data):
#     return response_obj.build_response(data)

# json_resp = JSONResponse()
# error_resp = ErrorResponse()

# print(send_response(json_resp, {"id": 1, "name": "Rohit"}))
# print(send_response(error_resp, "Invalid user id"))



# Compare behavior of overridden methods.

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# animal = Animal()
# dog = Dog()

# animal.speak()
# dog.speak()




# 🔴 Hard


# Design a polymorphic data processor.

# class DataProcessor:
#     def process(self, data):
#         raise NotImplementedError("Subclasses must implement this method")

# class NumberProcessor(DataProcessor):
#     def process(self, data):
#         return f"Sum of numbers = {sum(data)}"

# class StringProcessor(DataProcessor):
#     def process(self, data):
#         return f"Combined string = {' '.join(data)}"

# class DictProcessor(DataProcessor):
#     def process(self, data):
#         return f"Total keys = {len(data)}"

# def run_processor(processor, data):
#     return processor.process(data)

# num_p = NumberProcessor()
# str_p = StringProcessor()
# dict_p = DictProcessor()

# print(run_processor(num_p, [10, 20, 30]))
# print(run_processor(str_p, ["Hello", "World"]))
# print(run_processor(dict_p, {"id": 1, "name": "Rohit"}))



# Create polymorphic logger classes.

# class Logger:
#     def log(self, message):
#         raise NotImplementedError("Subclasses must implement log()")

# class ConsoleLogger(Logger):
#     def log(self, message):
#         print(f"[CONSOLE] {message}")

# class FileLogger(Logger):
#     def log(self, message):
#         with open("app.log", "a") as file:
#             file.write(f"[FILE] {message}\n")

# class DatabaseLogger(Logger):
#     def log(self, message):
#         print(f"[DATABASE] Saved log: {message}")

# def write_log(logger, message):
#     logger.log(message)   # same method call

# console = ConsoleLogger()
# file = FileLogger()
# db = DatabaseLogger()

# write_log(console, "Application started")
# write_log(file, "User logged in")
# write_log(db, "Transaction completed")


# Implement runtime polymorphism in backend logic.

# class PaymentProcessor:
#     def process(self, amount):
#         raise NotImplementedError("Subclasses must implement process()")

# class UPIPayment(PaymentProcessor):
#     def process(self, amount):
#         print(f"Processing ₹{amount} via UPI")
        
# class CardPayment(PaymentProcessor):
#     def process(self, amount):
#         print(f"Processing ₹{amount} via Credit/Debit Card")

# class CashPayment(PaymentProcessor):
#     def process(self, amount):
#         print(f"Processing ₹{amount} in Cash")

# def make_payment(processor, amount):
#     processor.process(amount)   # runtime decision

# p1 = UPIPayment()
# p2 = CardPayment()
# p3 = CashPayment()

# make_payment(p1, 500)
# make_payment(p2, 1200)
# make_payment(p3, 300)


# Build ML model evaluator with polymorphic score method.

# class ModelEvaluator:
#     def score(self, y_true, y_pred):
#         raise NotImplementedError("Subclasses must implement score()")

# class AccuracyEvaluator(ModelEvaluator):
#     def score(self, y_true, y_pred):
#         correct = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
#         return correct / len(y_true)

# class MSEEvaluator(ModelEvaluator):
#     def score(self, y_true, y_pred):
#         return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)

# class MAEEvaluator(ModelEvaluator):
#     def score(self, y_true, y_pred):
#         return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / len(y_true)

# def evaluate_model(evaluator, y_true, y_pred):
#     return evaluator.score(y_true, y_pred)

# y_true = [1, 0, 1, 1, 0]
# y_pred = [1, 0, 0, 1, 0]

# acc = AccuracyEvaluator()
# mse = MSEEvaluator()
# mae = MAEEvaluator()

# print("Accuracy:", evaluate_model(acc, y_true, y_pred))
# print("MSE:", evaluate_model(mse, y_true, y_pred))
# print("MAE:", evaluate_model(mae, y_true, y_pred))




# Design extensible system using polymorphism.

class Notification:
    def send(self, message):
        raise NotImplementedError("Subclasses must implement send()")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Push notification sent: {message}")

def notify_user(notification, message):
    notification.send(message)   # polymorphic call

email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

notify_user(email, "Welcome!")
notify_user(sms, "OTP: 1234")
notify_user(push, "New message received")
