# 📅 Day 6 – Lists & Tuples (Assignment / Practice Questions)
# 🟢 Easy Level

# Write a program to create a list and display its elements.

# list=["Hello","Raushan","How","are","you"]
# print(list)
# for li in list:
#     print(li,end=" ")

# Write a program to find the length of a list without using len().

# words=["Hello","Raushan","How","are","you"]
# length=0
# for i in words:
#     length+=1
    
# print("The length of list is : ",length)

# Write a program to access the first and last element of a list.

# words=list(input("Enter list : ").split())
# if len(words)>0:
#     print("First element of list is ",words[0])
#     print("Last element of list is ",words[-1])

# else:
#     print("List is empty ")

# Write a program to convert a tuple into a list.

# fruits=("Apple","Banana","Mango")
# fruit=list(fruits)
# print(fruit)
# for i in fruit:
#     print(i)



# 🟡 Medium Level

# Write a program to find the maximum element in a list without using built-in functions.

# numbers = list(map(int, input("Enter numbers: ").split()))

# if not numbers:
#     print("List is empty")
# else:
#     def largest_element(list):
#         largest=list[0]
#         i=0
#         while i<len(list):
#             if list[i]>largest:
#                 largest=list[i]
#             i+=1
            
#         return largest
#     lar=largest_element(numbers)
#     print("Largest Element of list is : ",lar)
            
    
# Write a program to find the minimum element in a list without using built-in functions.

# numbers = list(map(int, input("Enter numbers: ").split()))

# if not numbers:
#     print("List is empty")
# else:
#     def smallest_element(list):
#         smallest=list[0]
#         i=0
#         while i<len(list):
#             if list[i]<smallest:
#                 smallest=list[i]
            
#             i+=1
#         return smallest
#     Minimum=smallest_element(numbers)
#     print("Minimum Element of list is : ",Minimum)

# Write a program to remove duplicate elements from a list.

#unorder
# words=list(input("Enter list : ").split()) 
# word=set(words) 
# print(word)

#same order

# words = input("Enter list: ").split()

# unique_words = []
# for w in words:
#     if w not in unique_words:
#         unique_words.append(w)

# print(unique_words)

# Write a program to count the occurrence of each element in a list.

# numbers = [1, 2, 1, 3, 2, 1]
# occurrence = {}

# for num in numbers:
#     if num in occurrence:
#         occurrence[num] += 1
#     else:
#         occurrence[num] = 1

# for num in occurrence:
#     print(num, ":", occurrence[num])


# 🔴 Hard Level

# Write a program to find the second largest element in a list.

# numbers = list(map(int, input("Enter numbers: ").split()))

# if len(numbers) < 2:
#     print("List must have at least two elements")
# else:
#     largest = numbers[0]
#     second_largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num != largest and num > second_largest:
#             second_largest = num

#     print("Second largest element is:", second_largest)

# Write a program to merge two lists without using built-in functions.

# words1 = input("Enter first list: ").split()
# words2 = input("Enter second list: ").split()

# merged_list = []

# for w in words1:
#     merged_list.append(w)

# for w in words2:
#     merged_list.append(w)

# print("Merged list:", merged_list)


# Write a program to check whether a list is a palindrome.

# [1, 2, 3, 2, 1]
# ['a', 'b', 'c', 'b', 'a']
# ['madam', 'is', 'madam']

# words1 = input("Enter string list: ").split()

# rev_list = []
# i = len(words1) - 1

# while i >= 0:
#     rev_list.append(words1[i])
#     i -= 1

# if words1 == rev_list:
#     print("List is palindrome")
# else:
#     print("List is not palindrome")


# Write a program to find common elements between two tuples.

# colours1=("Red","Blue","Green")
# colours2=("Red","White","Gray")

# t1=set(colours1)
# t2=set(colours2)
# print("Common element",t1 & t2)


#other methods

colours1 = ("Red", "Blue", "Green")
colours2 = ("Red", "White", "Gray")

common = []

for c in colours1:
    if c in colours2 and c not in common:
        common.append(c)

print("Common elements:", common)
