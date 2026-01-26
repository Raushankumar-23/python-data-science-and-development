# 📅 Regular Expressions (Regex) – Assignment / Practice Questions
# 🟢 Easy Level (Programs)

# Write a program to check whether a string starts with a specific word using regex.

# import re

# a = "charlie chaplin coa and the chacolate factory"

# if re.search(r"^charlie", a):
#     print("String starts with the word 'charlie'")
# else:
#     print("String does not start with the word 'charlie'")


# Write a program to check whether a string ends with a specific word using regex.

# import re

# a = "charlie chaplin coa and the chacolate factory"

# if re.search(r"factory$", a):
#     print("String end with the word 'factory'")
# else:
#     print("String does not end with the word 'factory'")

# Write a program to find all digits in a given string using regex.

# import re
# b="raushan.engineer235@gmail.com"

# match=re.search(r"\d",b)
# print(match)
# match=re.findall(r"\d",b)
# print(match)


# Write a program to find all lowercase letters in a string using regex.

# import re
# b = "Charlie chaplin Coa And the chacolate Factory"

# match=re.search(r"[a-z]",b)
# print(match)
# match=re.findall(r"[a-z]",b)
# print(match)

# Write a program to replace all spaces with underscores using regex.

# import re
# b = "Charlie chaplin Coa And the chacolate Factory"

# result = re.sub(r"\s", "_", b)
# print(result)


# 🟡 Medium Level (Programs)

# Write a program to validate an email address using regex.

# import re

# email = "rohit781@gmail.com  rohit@.com raushan.98@yahoo.com"

# pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}"

# valid_emails = re.findall(pattern, email)

# print(valid_emails)
# print(len(valid_emails))


# Write a program to validate a 10-digit mobile number using regex.

# import re

# phn = "222-444-8967"

# if re.fullmatch(r"\d{3}-\d{3}-\d{4}", phn):
#     print("Valid 10-digit mobile number")
# else:
#     print("Invalid mobile number")


# Write a program to find all words with length greater than or equal to 5 using regex.

# import re

# a = "charlie chaplin coa and the chacolate factory"

# words = re.findall(r"\b\w{5,}\b", a)
# print(words)

# Write a program to extract all numbers from a string using regex.

# import re
# a = "charlie chaplin 34coa and the 89chacolate factory2"
# match=re.findall(r"\d+",a)
# print(match)

# Write a program to remove special characters from a string using regex.

# import re

# a = "$charlie ^chaplin 34@coa and the #89chacolate factory2!"

# result = re.sub(r"[^a-zA-Z0-9\s]", "", a)
# print(result)


# 🔴 Hard Level (Programs)

# Write a program to validate a strong password using regex.

# import re

# password = "Strong@123"

# if re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}", password):
#     print("Strong password")
# else:
#     print("Weak password")



# Write a program to extract dates (DD-MM-YYYY format) from a text using regex.

# import re

# text = "My DOB is 02-12-2004 and my brother was born on 15-08-1998."

# match=re.findall(r"\d{2}-\d{2}-\d{4}",text)
# print(match)

# Write a program to find duplicate words in a string using regex.

# import re

# a = "charlie chaplin coa and the chacolate and factory"

# duplicates = re.findall(r"\b(\w+)\b(?=.*\b\1\b)", a)
# print(duplicates)

# Explanation (simple & exam-ready)
# \b(\w+)\b → captures a word
# () → grouping (stores the word)
# \1 → backreference (same word again)
# (?=.*\b\1\b) → checks if the word appears again later
#re.findall() → returns duplicate words

# Write a program to split a string using multiple delimiters with regex.

# import re

# text = "apple,banana;orange|grapes mango"

# result = re.split(r"[,\;|\s]+", text)
# print(result)

# Write a program to validate a URL using regex.

import re

url = "https://www.example.com"

pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

if re.fullmatch(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")
