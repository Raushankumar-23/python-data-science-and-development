# decroator 

# def decor(func):
#     def inner():
#         func() # existing functionality
#         #add new functionality
#         print("welcome")
#     return inner

# def printer():
#     print("welcome")
#     print("welcome")

# printer=decor(printer)
# printer()
    
    
#example


# def decor(addition):
#     def inner():
#         result=addition() #existing functionality
#         num3=float(input("Enter first number : "))
#         result=result+num3
#         return result
#     return inner
# @decor   
    
# def addition():
#     num1=float(input("Enter first number : "))
#     num2=float(input("Enter second number :"))
#     result=num1+num2
#     return result

# #addition=decor(addition)
# print("addition is ",addition())

# multiple decorator

# def decor1(func):
#     def inner():
#         return func().upper()
#     return inner

# def decor2(func):
#     def inner():
#         return func().split()
#     return inner

# @decor2
# @decor1
# def get_name():
#     name=input("Enter first name : ")
#     sirname=input("Enter sirname : ")
#     full_name=name+" "+sirname
#     return full_name

# #get_name=decor2(decor1(get_name))
# print(get_name())


def decor(func):
    def inner(*args):#(0,10,5)
        for num in args[1:]:
            if num==0:
                return "cannot divide by zero"
            
        return func(*args)
    return inner

@decor
def div1(a,b):
    return a/b
@decor
def div2(a,b,c):
    return a/b/c

print(div1(10,5))
print(div1(10,0))
print(div2(10,0,5))
print(div2(10,20,0))
print(div2(0,10,5))
