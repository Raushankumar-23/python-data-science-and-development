# Duck Typing

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
#     obj.fly()
    
    
# airplane=Airoplane()
# owl=Owl()
# person=Person()

# canfly(owl)
# canfly(airplane)
# # #canfly(person)  #create error



#method overriding

# class Animal:
#     def eat(self):
#         print("The animal can eat in generall")  
#     def sleep(self):
#         print("The animal can sleep in generall")
#     def walk(self):
#         print("The animal can walk in generall")    
        
# class Lion(Animal):
#     def eat(self):  # redefined function
#         print("Lion can eat")

# lion=Lion()
# lion.eat()


#method overloading

# class Greeting:
#     def goodmorning(self):
#         print("Good Morning")
#     def goodmorning(self,name):
#         print(f"Goodmorning{name}")    
    
    
    
#operator overloading

class Book:
    def __init__(self,pages,price):
        self.pages=pages
        self.price=price
        
    def __add__(self,other):
        price=self.price+other.price
        pages=self.pages+other.pages
        return Book(pages,price)


bookl=Book(100,100)
book2=Book(200,150)
book3=bookl+book2
print(book3.pages)
print(book3.price)