# File handling

#write data
# age=input("Enter you age :")
# f=open("data.txt","w")
# f.write(age)
# f.close

#read /open data
# f=open("data.txt","r")
# data=f.read()
# print(data)
# f.close()

#create file and write data
# file=open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\masti.txt","w")
# file.write("Hello word\n")
# file.write("Welcome\n")
# file.write("welcome to ws")
# file.writelines(["Welcome raushan\n","Hello Raushan\n","Welcome to IIP\n"]) #multiple lines
# file.close()

#automatic close
# with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\masti.txt","r") as file:
#     # print(file.read())
#     print(file.readline())

file=open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\masti.txt","r")
data=file.read()
print(data)


# All read operation

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\mast.txt","r")
# data=fh.read()
# print(data)

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\mast.txt","r")
# ln = fh.readline()#only one line read
# print(ln)
# ln = fh.readline()
# print(ln)
# ln = fh.readline()
# print(ln)
# ln = fh.readline(110)
# print(ln)

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\mast.txt","r")
# ls = fh.readlines()
# for ln in ls:
#     print(ln)

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\mast.txt","r")
# data = fh.read()
# print(data,len(data)) # count char

#cound lines
# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\mast.txt","r")
# ls = fh.readlines()
# print(f"no of lines = {len(ls)}")

#no of words
# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\mast.txt","r")
# data = fh.read()
# ls = data.split(" ")
# sum = 0
# for s in ls:
#     sum += 1
# print(ls, "no of words ", sum)

#count alphabet char digit
# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\python_basics\mast.txt","r")
# data=fh.read()
# a,d,s,sc=0,0,0,0
# for ch in data:
#     if ch.isalpha():
#         a +=1
#     elif ch.isdecimal():
#         d +=1
#     else:
#         sc +=1
        
# print("Alphabets = ",a)
# print("Digits = ",d)
# print("Spaces = ",s)
# print("Special char = ",sc)