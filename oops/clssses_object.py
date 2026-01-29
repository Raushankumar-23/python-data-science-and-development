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
   
   
class Mobile:
    def __init__(self,m):
        self.model=m
        
        
    def show_model(self,p):
        self.price=p
        print("Modle :",self.model,"\n","Price:",self.price)
        
        
#object
realme=Mobile("RealMe X")
realme.show_model(1000)
print(id(realme))
print()
redmi=Mobile("Redmi 7s")
redmi.show_model(2000)
print(id(redmi))
print()
geek=Mobile("Python")
geek.show_model(49)
print(id(geek))