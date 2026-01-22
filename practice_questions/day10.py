# 📘 List Comprehensions – Assignment / Practice Questions
# 🟢 Easy Level

# 1. Create a list of numbers from 1 to 10 using list comprehension.

# results = [i for i in range(1,11)]
# print("list=",results)

# 2. Create a list of squares of numbers from 1 to 10.

# results = [i*i for i in range(1,11)]
# print("list=",results)

# 3. Create a list of even numbers from 1 to 20.

# results = [i for i in range(1,21) if i%2==0]
# print("Even no of 1 to 20 =",results)

# 4. Create a list of characters from a given string.

# text="Hello Raushan How are you"
# results = [i for i in text]
# print("list=",results)


# 5. Convert all elements of a list to uppercase using list comprehension.

# string=["intro","to","list","comps","Raushan","Kumar"]
# results = [i.upper() for i in string]
# print("list=",results)


# 🟡 Medium Level

# 6. Create a list of odd numbers from a given list.

# nums=[1,2,3,4,5,6,7,8,9,12,45,33,67,89,57,60,40]
# results=[i for i in nums if i%2!=0]
# print("Odd no  =",results)

# 7. Create a list of numbers greater than 50 from a list.

# nums=[1,2,3,4,5,6,7,8,9,12,45,33,67,89,57,60,40,99,231,564,4,785]
# results=[i for i in nums if i>50]
# print("Grater than 50  =",results)

# 8.  Create a list of lengths of words from a list of strings.

# words = ["Hello", "Python", "List", "Comprehension"]
# results=[len(i) for i in words]
# print(results)

# 9. Create a list by removing vowels from a string.

# text = "Hello Raushan How are you"
# results = [i for i in text if i.lower() not in ["a","e","i","o","u"]]
# print("List without vowels:", results)

# 10. Create a list of numbers divisible by both 3 and 5 between 1 and 100.

# results=[i for i in range(1,101) if i%3==0 if i%5==0]
# print("List divisible both 3 and 5",results)

# 🔴 Hard Level

# 11. Create a list of unique elements from a list using list comprehension.

# nums = [1,2,3,4,5,2,3,6,7,8,9,12,45,33,67,9,10,89,57,60,40,99,231,564,4,785]
# results = []
# [results.append(i) for i in nums if i not in results]
# print("Unique elements of list is:", results)


# 12. Create a list of tuples (number, square) for numbers from 1 to 10.

# nums = [1,2,3,4,5,6,7,8,9,10]
# results=[(i,i*i) for i in nums ]
# print("list of tuples is ",results)

# 13. Flatten a nested list using list comprehension.

# Input: nested list
# nested = [[1, 2], [3, 4], [5, 6]]

# # Flattening using list comprehension
# flat = [item for sublist in nested for item in sublist]

# print("Flattened list:", flat)

# 14. Create a list of common elements between two lists using list comprehension.

# num1 = [1,2,3,4,5,6,8,9,10]
# num2 = [1,2,4,5,6,7,8,10]

# result=[i for i in num1 and num2]
# print("common elements",result)

# 15. Create a list of prime numbers from a given list using list comprehension.

# Create a list of prime numbers from a given list using list comprehension.

# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,29]

# results = [i for i in nums if i > 1 and all(i % j != 0 for j in range(2, i))]
# print("Prime numbers:", results)
