# # Dictionary

# student={"name":"Raushan","age":21,"city":"Patna"}
# # print(student)

# # Accessing values
# # print(student["name"])
# # print(student["age"])

# # adding and updating
# # student["marks"]=85
# # student["city"]="Mumbai"
# # print(student)

# # Dictionary methods
# # print(student.keys())
# # print(student.values())
# # print(student.items())
# # print(student.get("name"))

# #Looping
# # for dict in student:
# #     print(dict,student[dict])

# Nested dictionary
# employees={
#     "E101":{"name":"Rohit","city":"Patna"},
#     "E102":{"name":"Raushan","city":"Gaya"},
    
# }
# print(employees["E102"]["name"])

# # Mapping wrong -> correct
# mapper={
#     "mombai":"Mumbai",
#     "kolkatta":"Kolkata"
# }
# print(mapper["mombai"])



# ✅ Method 1: Fixed keys (Best for beginners)
# student = {}

# student["name"] = input("Enter name: ")
# student["roll"] = int(input("Enter roll number: "))
# student["marks"] = int(input("Enter marks: "))

# print(student)

# ✅ Method 2: Multiple students (using loop)
# students = {}
# n = int(input("How many students? "))

# for i in range(n):
#     name = input("Enter name: ")
#     marks = int(input("Enter marks: "))
#     students[name] = marks

# print(students)

# ✅ Method 3: User-defined keys & values
# data = {}
# n = int(input("How many items? "))

# for i in range(n):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     data[key] = value

# print(data)

n = int(input("How many students "))
m = int(input("How many keys "))
data = dict(input("Enter keys"))
for i in (1,n+1):
    for j in data:
        j=input("Enter data of ",i,"student")