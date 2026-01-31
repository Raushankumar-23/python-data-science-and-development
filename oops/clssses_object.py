# Classes & objects

#example-1
# class Myclass(object):
#     def show(self):
#         print("I am a method")
        
        
        
# x=Myclass()
# x.show()

#example-2
# class Myclass:
#     def show(self):
#         print("I am a method")
        
        
        
# x=Myclass()
# x.show()


#Example-3

# class Mobile:
#     def __init__(self):
#         self.model="RealMeX"
        
        
#     def show_model(self):
#         print("Modle :",self.model)
        
        
# #object
# realme=Mobile()


# #function call

# realme.show_model() 

# #access variable outside class

# print(realme.model) 

# #reassign value

# realme.model="RealMe X"
# print(realme.model)
# realme.show_model()


#example-4
   
   
# class Mobile:
#     def __init__(self,m):
#         self.model=m
        
        
#     def show_model(self,p):
#         self.price=p
#         print("Modle :",self.model,"\n","Price:",self.price)
        
        
# #object
# realme=Mobile("RealMe X")
# realme.show_model(1000)
# print(id(realme))
# print()
# redmi=Mobile("Redmi 7s")
# redmi.show_model(2000)
# print(id(redmi))
# print()
# geek=Mobile("Python")
# geek.show_model(49)
# print(id(geek))


class User:
    def put_data(self):
        self.id=int(input("Enter user id : "))
        self.name=input("Enter your name : ")
        self.salary=float(input("Enter your salary : "))
        
        
    def display_data(self):
        print("User data")
        print("User id : ",self.id)
        print("User name : ",self.name)
        print("User Salary : ",self.salary)
        
        
a=User()
a.put_data()
a.display_data()
