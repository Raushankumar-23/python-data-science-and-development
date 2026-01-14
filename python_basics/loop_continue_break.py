#Loops in python
# (for & while)

# 1 Basic Loop

# for i in range(5):
#     print(i)
# print("Complete")

# for i in range(1,11):
#     print(i)
    
# 2 print Characters
# p="Python"
# for char in p:
#     print(char)

# for i in range(1,100,10):
#     print(i)
# print("Done!")

# 3 Loop through list
# items=["Pen","Book","Laptop"]
# for i in items:
#     print(i)
# print("Done")

# 4 Even num 1 to 20

# for i in range(0,21,2):
#     print(i)
# print("Done!")

# total calculation
# marks=[78,82,70,34,90]
# total=0
# for i in marks:
#     total+=i
# print(total)

# 6 clean cities
# cities=["  MUMBAI","delhi","Patna"]
# for i in cities:
#     print(i.strip().title())
# print("clean cities")

# cities=["  MUMBAI","delhi","Patna"]
# cleaned = []
# for i in cities:
#     cleaned.append(i.strip().title())
# print(cleaned)

# loop with if condition
# nums=[5,12,3,18,7]
# for n in nums:
#     if n>10:
#         print(n)
        
# print("Done!")

# 9 Extract last digits from IDs
# ids = ["EMP-001122","EMP-889900"]
# for last4 in ids:
#     print(last4[-4:])

# while loop
# i=1
# while i<=5:
#     print(i)
#     i+=1
# print("Don!")

# n=10
# while n>0:
#     print(n)
#     n-=1
# print("Done!")

# 3 Ask user valid input
# num=""
# while not num.isnumeric():
#     num=input("Enter any value : ")

# print("Number accepted : ",num)

# items = ["Apple","Banana","Grapes"]
# i=0
# while i< len(items):
#     print(items[i])
#     i+=1
# print("Done!")

# continue
# print number upto 10 except 5
# i = 1
# while i <= 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1

# print("Done!")

# x=1
# while x <= 10:
#     print(x)
#     if x==5:
#         break
#     x+=1
    
# print("Done!")

# print odd num
# y=0
# while y < 10:
#     y +=1
#     if y%2==0:
#         continue
#     print(y)
    
# print("Done!")

# password=""
# attempt=0

# while password != "admin123" and attempt < 3:
#     password = input("Enter password : ")
#     attempt +=1
#     if password == "admin123":
#         print("Login successful")
#     else:
#         print("Wrong password Try again, Attempt count : ",attempt)
#     if attempt==3:
#         print("3 Attempt Expired")
        