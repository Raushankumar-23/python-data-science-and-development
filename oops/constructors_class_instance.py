#types of constractor -> constractor is a special method, used for object initialization.
#Different type of constractor -> defualt,non- parametrizes,parametrize
# default constractor -> if we have not written any constractor in the class, then python adds one.

# class Person:
#     def sayHi(self):
#         print("Hi")
        
        
# peson1=Person()
# peson2=Person()
# peson3=Person()

# peson1.sayHi()
# peson2.sayHi()
# peson2.sayHi()



#non parametrised

# class Person:
#     def __init__(self):
#         self.name="Raushan"
#         self.age=21

        
#     def sayHi(self):
#         print("Hi")
        
# peson1=Person()
# peson2=Person()
# peson2=Person()


# print(peson1.name)
# print(peson2.name)
# print(peson2.name)




#paramerised constractor

# class Person:
#     def __init__(self,name,age):
#         self.name="Raushan"
#         self.age=21

        
#     def sayHi(self):
#         print("Hi")
        
# peson1=Person("Rohit",22)
# peson2=Person("Rahul",20)

# print(peson1.name)
# print(peson2.name)





# class Test:
#     def __init__(self):
#         print("Constructor executed")
        
# obj1=Test()

# #valid call
# obj1.__init__()
# obj1.__init__()
# obj1.__init__()
# obj1.__init__()


#without constractor
# valid

# class Test:
#     def m1(self):
#         print("m1 method executed")
        
        
# obj1=Test()

class Test:
    def __init__(self):
        print("No arg constructor")
        
    def __init__(self,x): #take last wala
        print("One arg pass")
        
 #so one arg pass
#obj1=Test() #error
obj2=Test(10)