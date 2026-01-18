# 📅 Day 5 – Strings (Assignment / Practice Questions)
# 🟢 Easy Level

# Write a program to input a string and display it.

# str=input("Enter a string : ")
# print(str)

# Write a program to find the length of a string without using len().

# str=input("Enter a string : ")
# count=0
# for i in str:
#     count+=1
    
# print("Length of String : ",count)
    
# Write a program to convert a string to uppercase and lowercase.

# text=input("Enter a string : ")
# print("Upper Case of String : ",text.upper())
# print("Upper Case of String : ",text.lower())
# print("Upper Case of String : ",text.title())


# Write a program to print the first and last character of a string.

# text=input("Enter a string : ")
# if len(text)>0:
#     print("first character of string : ",text[0])
#     print("last character of string : ",text[-1])
# else:
#     print("String is Empty ")

# 🟡 Medium Level

# Write a program to reverse a string.

# text=input("Enter a string : ")
# i=len(text)-1
# while i>=0:
#     print(text[i],end="")
#     i-=1


# Write a program to check whether a string is a palindrome.

# text=input("Enter a string : ")
# rev=""
# i=len(text)-1
# while i>=0:
#     rev=rev+text[i]
#     i-=1
    
# if text.lower()==rev.lower():
#     print("Palindrome string")
    
# else:
#     print("Not a Palindrom string")

# Write a program to count the number of vowels and consonants in a string.

# text=input("Enter a string : ")
# vowel=0
# cons=0
# for ch in text:
#     if ch.lower() in "aeiou":
#         vowel+=1
#     else:
#         cons+=1
        
# print("no of vowel ",vowel)
# print("no of consonate ",cons)
        

# Write a program to count the number of words in a string.

# text = input("Enter a string: ")

# count = 0
# in_word = False

# for ch in text:
#     if ch.isalpha():
#         if not in_word:
#             count += 1
#             in_word = True
#     else:
#         in_word = False

# print("Number of words:", count)

# text = input("Enter a string: ")

# words = text.split()
# print("Number of words:", len(words))


# 🔴 Hard Level

# Write a program to find the frequency of each character in a string.

# text = input("Enter a string: ")
# uniq=set(text.lower())
# for char in uniq:
#     if char != " ":
#         print("frequency", char, text.lower().count(char))

    
# Write a program to find the frequency of each word in a string.

# text = input("Enter a string: ").lower()

# words = text.split()
# freq = {}

# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# for word in freq:
#     print(word, ":", freq[word])

# Write a program to find the most frequent word in a string.

# text = input("Enter a string: ").lower()

# words = text.split()   # words की list
# freq = {}              # empty dictionary

# # count each word
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# # find most frequent word
# max_word = ""
# max_count = 0

# for word in freq:
#     if freq[word] > max_count:
#         max_count = freq[word]
#         max_word = word

# print("Most frequent word:", max_word)
# print("Frequency:", max_count)



# Write a program to remove duplicate words from a string.

text = input("Enter a string: ").lower()

words = text.split()
text1=set(words)
for i in text1:
    print(i,end=" ")
    
    
    
text = input("Enter a string: ").lower()

words = text.split()
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

for word in unique_words:
    print(word, end=" ")
