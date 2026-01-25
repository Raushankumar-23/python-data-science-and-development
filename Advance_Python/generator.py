# generator

# def disp(a,b):
#     yield a
#     yield b
    
# result=disp(10,20)
# print(type(result))
# lst=list(result)
# print(lst)
# print(type(lst))    

# def disp(a,b):
#     yield a
#     yield b
    
# result=disp(10,20)
# print(result)
# print(type(result))
# print(next(result))
# print(next(result))


# def show(a,b):
#     while a<=b:
#         yield a
#         a+=1
        
# result=show(1,5)
# print(result)
# print(type(result))
# print(next(result))
# print(next(result))
# for i in result:
#     print(i)

# fibonacci

def fibona(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
        
        
fibo=fibona(10)
print(fibo)
print(type(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))

