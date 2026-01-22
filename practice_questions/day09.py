# 📁 File Handling – Assignment / Practice Questions
# 🟢 Easy Level

# Write a program to create a file and write some text into it.

# file = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\masti.txt", "w")
# file.write("Hello Raushan\n")
# file.write("How are you?\n")
# file.write("What to do learn?\n")
# file.close()
# print("File created and data written successfully")

# Write a program to read the contents of a file and display it.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\masti.txt", "r")
# print(fh.read())
# print("read sucessful")
# fh.close()

# Write a program to append data to an existing file.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\masti.txt", "a")
# fh.write("This is new appended line\n")
# fh.close()
# print("append sucessful")

# Write a program to count the number of lines in a file.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")
# lines = fh.readlines()
# print("No of lines =", len(lines))

# fh.close()
# print("Line count successful")


# Write a program to count the number of characters in a file.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")
# char=fh.read()
# print("The no of character is : ",len(char))
        
# fh.close()
# print("count of character is successful")

# 🟡 Medium Level

# Write a program to count the number of words in a file.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")
# words=fh.read().split()
# sum=0
# for word in words:
#     sum+=1
    
# print("The number of words in file is : ",sum)
# fh.close()

# print("count of words is sucessful")


# Write a program to copy contents from one file to another.

# Copy contents from masti.txt to hello.txt

# with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\masti.txt", "r") as src:
#     data = src.read()

# with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "w") as dest:
#     dest.write(data)

# print("Copy successful")

# Write a program to search a word in a file.

# Write a program to search a word in a file.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")

# content = fh.read()
# word = "Python"

# if word in content:
#     print("Searching element is present")
# else:
#     print("Searching element is not present")

# fh.close()
# print("Read successful")

# Write a program to replace a word in a file.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")
# content = fh.read()
# fh.close()

# content = content.replace("Python", "Java")

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "w")
# fh.write(content)
# fh.close()

# print("Word replaced successfully")

# Write a program to read a file line by line using a loop.

# fh = open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")
# for line in fh:
#     print(line,end=" ")
    
# fh.close()

# print("print successfully")


# 🔴 Hard Level

# Write a program to find the frequency of each word in a file.

# word_freq = {}
# with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")as f:
#     words = f.read().split()
#     for word in words:
#         word_freq[word] = word_freq.get(word, 0) + 1

# print("\nWord Frequency:")
# for word, count in word_freq.items():
#     print(word, ":", count)

# Write a program to find the longest word in a file.

# with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")as f:
#     words = f.read().split()

# longest_word = max(words, key=len)
# print("\nLongest word:", longest_word)


# Write a program to remove blank lines from a file.

# with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")as f:
#     lines = f.readlines()

# with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "w")as f:
    
#     for line in lines:
#         if line.strip():
#             f.write(line)

# print("Blank lines removed.\n")

# Write a program to handle FileNotFoundError using exception handling.

# try:
#     with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hepllo.txt", "r")as f:
#         print(f.read())
# except FileNotFoundError:
#     print("Error: File not found.\n")

# Write a program to store and retrieve student records from a file.

with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "w")as f:
    f.write("101,Rahul,85\n")
    f.write("102,Amit,90\n")
    f.write("103,Neha,88\n")

print("Student Records:")
with open(r"C:\Users\Raushan Kumar\OneDrive\Desktop\python-data-science-and-development\practice_questions\hello.txt", "r")as f:
    for line in f:
        roll, name, marks = line.strip().split(",")
        print("Roll:", roll, "Name:", name, "Marks:", marks)

print("\n=== Day 09 Practice Completed ===")