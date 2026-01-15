# Function

# def greet():
#     print("Hello python learners")
    
# greet()
# greet()

# def welcome(name):
#     print("Welcome",name)
    
# welcome("Raushan")

# def sum(a,b):
#     print("Sum is ",a+b)
    
# sum(5,6)

# def sum(a,b):
#     return a+b

# total=sum(5,6)
# print(total)

# def sum(a,b):
#     return a+b

# def multiply(x):
#     return x*2

# result=multiply(sum(5,8))
# print(result)

# def fix_city(city):
#     city=city.lower().strip()
#     city=city.replace("mombai","mumbai")
#     city=city.replace("kolkatta","kolkata")
#     return city.title()

# print(fix_city(" mombai"))

# def is_valid_email(email):
#     return "@" in email and "." in email


# print(is_valid_email("test@gmail.com"))

# def clean_list(values):
#     cleaned=[]
#     for v in values:
#         cleaned.append(v.strip().title())
#     return cleaned
    
# print(clean_list(["delhi","mumbai","pune"]))


def check_prime(n):
    if n<=1:
        print(n,"is not a prime number")
        return
    
    i=2
    while i<n:
        if n%i==0:
            print(n,"is not a prime number ")
            return
        i=i+1
        
    print(n,"is prime number ")
        
        
num=int(input("Enter a number "))
check_prime(num)
        