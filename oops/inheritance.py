# inheritance ->  one class make into another class
#typpe of inheritance(Single,Multilevel,Multiple ....)


#Single inheritance -> when there is one parent class, and one child class, we say that there is single inheritance
#Single inheritance

# class Parent:
#     def cansing(self):
#         print("parent can sing")
        
        
# class Child(Parent):
#     print("child can sing")


#Multilevel inhertance -> we have a parent class ,from which, we create a child, 
#and then again from the child class, we create another child class
#Multilevel inhertance

# class GrandFather:
#     def cansing(self):
#         print("The grandfather can sing")
    
    
# class Father(GrandFather):
#     def candance(self):
#         print("The father can sing")
    
    
    
# class Child(Father):
#     def candraw(self):
#         print("The child can sing")
        
        
# child=Child()
# child.cansing()


#Multiple

# # Parent class 1
# class Employee:
#     def __init__(self, name):
#         self.name = name


# # Parent class 2
# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance


# # Child class (Multiple Inheritance)
# class DanceEmployee(Employee, Dancer):
#     def __init__(self, name, dance):
#         Employee.__init__(self, name)
#         Dancer.__init__(self, dance)


# # Object creation
# o = DanceEmployee("Shivani", "Kathak")

# print(o.name)
# print(o.dance)



# Hybride class

# class BaseClass:
#     pass

# class Derived1(BaseClass):
#     pass

# class Derived2(BaseClass):
#     pass

# class Derived3(Derived1,Derived2):
#     pass


#example
# class BaseClass:
#     def show_base(self):
#         print("This is BaseClass")


# class Derived1(BaseClass):
#     def show_d1(self):
#         print("This is Derived1")


# class Derived2(BaseClass):
#     def show_d2(self):
#         print("This is Derived2")


# class Derived3(Derived1, Derived2):
#     def show_d3(self):
#         print("This is Derived3")


# obj = Derived3()

# obj.show_base()
# obj.show_d1()
# obj.show_d2()
# obj.show_d3()



#herarchy

# Parent class
class Animal:
    def eat(self):
        print("Animal can eat")


# Child class 1
class Dog(Animal):
    def bark(self):
        print("Dog can bark")


# Child class 2
class Cat(Animal):
    def meow(self):
        print("Cat can meow")


# Creating objects
d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()
