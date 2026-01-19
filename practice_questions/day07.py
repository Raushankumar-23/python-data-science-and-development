# 📅 Day 8 – Nested Lists, Dictionaries & Sets
# 📝 Assignment / Practice Questions
# 🟢 Easy Level

# 1. Create a nested list and print all its elements using loops.

# fruints=["Apple","Mango","Orange",["Banana","Grapes"]]
# print(fruints)
# for i in fruints:
#     if type(i)==list:
#         for j in i:
#             print(j)
            
#     else:
#         print(i)
    
    
# 2. Write a program to access an element from a nested list.

# fruints=["Apple","Mango","Orange",["Banana","Grapes"]]
# print(fruints[3][0])
# print(fruints[3][1])


# 3. Create a dictionary with student details (name, roll number, marks) and display it.

# student={
#     "name":"Raushan",
#     "roll_number":90,
#     "marks":90   
# }
# print(student)
# print(student["name"])
# print(student["roll_number"])
# print(student["marks"])


# 4. Write a program to print all keys and values of a dictionary.

# student={
#     "name":"Raushan",
#     "roll_number":90,
#     "marks":90   
    
# }
# print(student.keys())
# print(student.values())

# print("Keys of dictionary ")
# for i in student:
#     print(i,student[i])

# 5. Create a set and print all its elements.

# fruits={"Apple","Banana","Mango","Orange"}
# print(fruits)
# print(type(fruits))
# print("Element of Sets is : ")
# for i in fruits:
#     print(i)


# 🟡 Medium Level

# 6. Write a program to find the sum of elements in a nested list.

# fruints=["Apple","Mango","Orange",[5,29,90,23,56]]
# sum=0
# for i in fruints:
#     if type(i)==list:
#         for j in i:
#             if type(j)==int:
#                 sum+=j
            
# print("sum of elements in a nested list is :",sum)


# 7. Write a program to count the total number of elements in a nested list.

# fruints=["Apple","Mango","Orange",[5,29,90,23,56]]
# total=0
# for i in fruints:
#     if type(i)==list:
#         for j in i:
#             total+=1

# print("the total number of elements in a nested list :",total)

# 8. Write a program to update the value of a key in a dictionary.

# student={
#     "name":"Raushan",
#     "roll_number":90,
#     "marks":90   
# }
# print(student.values())

# student["name"]="Rohit"
# student["marks"]=85
# print("Udate value : ",student.values())


# 9. Write a program to merge two dictionaries.
#student={
#     "name":"Raushan",
#     "roll_number":90,
#     "marks":90   
# }


# employees = {
#     "name": "Raushan",
#     "city": "Patna"
# }

# merged = {}

# for key in student1:
#     merged[key] = student1[key]

# for key in employees:
#     merged[key] = employees[key]

# print(merged)


# 10. Write a program to remove duplicate elements from a list using a set.

# fruints=["Apple","Mango","Orange","Banana","Grapes","Orange"]
# unique_element=set(fruints)
# print("After remove duplicate : ",unique_element)


# 11. Write a program to find common elements between two sets.

# a={1,2,3,8}
# b={3,4,5,8}
# print("Common element is : ",a&b)

# 12. Write a program to count the frequency of each element in a list using a dictionary.

# fruints=["Apple","Mango","Orange","Banana","Grapes","Orange"]
# for i in set(fruints):
#     freq=0
#     for j in fruints:
#         if i==j:
#             freq=freq+1
            
#     print("Freq of ",i,"is",freq)
            



# 🔴 Hard Level

# 13. Write a program to find the maximum element from a nested list.

# fruits = ["Apple","Mango","Orange",[5,29,90,23,56],[100,78]]

# largest = None
# for i in fruits:
#     if type(i) == list:
#         for j in i:
#             if largest is None or j > largest:
#                 largest = j

# print("Maximum element is:", largest)


# 14. Write a program to find the student with the highest marks using a dictionary.

# student name : marks
# students = {
#     "Raushan": 85,
#     "Rohit": 92,
#     "Amit": 78,
#     "Neha": 90
# }

# top_student = None
# highest_marks = 0

# for name in students:
#     if students[name] > highest_marks:
#         highest_marks = students[name]
#         top_student = name

# print("Student with highest marks:", top_student)
# print("Marks:", highest_marks)


# 15. Write a program to store and display multiple student records using a nested dictionary.

# students = {
#     "student1": {
#         "name": "Raushan",
#         "roll_number": 90,
#         "marks": 90
#     },
#     "student2": {
#         "name": "Rohit",
#         "roll_number": 80,
#         "marks": 85
#     },
#     "student3": {
#         "name": "Amit",
#         "roll_number": 70,
#         "marks": 88
#     }
# }

# print(students)
# print(students["student1"]["name"])
# print(students["student2"]["marks"])


# 16. Write a program to perform union, intersection, and difference operations on sets.

# a={1,2,3,8}
# b={3,4,5,8}
# print("union : ",a|b)
# print("intersection : ",a&b)
# print("Difference a-b : ",a-b)
# print("Difference b-a : ",b-a)

# 17. Write a program to find unique elements from a nested list.

# fruits = ["Apple", "Mango", "Orange", [5, 29, 90, 23, 90, 56], [100, 78, 100, 105]]

# unique_elements = set()

# for i in fruits:
#     if type(i) == list:
#         for j in i:
#             unique_elements.add(j)

# print("Unique elements from nested list:", unique_elements)


# 18. Write a program to sort dictionary elements based on values.

students = {
    "Raushan": 85,
    "Rohit": 92,
    "Amit": 78,
    "Neha": 90
}

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]))

print(sorted_students)
