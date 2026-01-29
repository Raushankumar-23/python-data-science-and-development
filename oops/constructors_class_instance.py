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