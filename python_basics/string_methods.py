# String Method 

#text1="     hello python learnears     "
# print(text1)
# print("Remove space : ",text1.strip())

# # convertt to capital letter
# print("Capital Letters : ",text1.upper()
#                                  .strip())

# # convertt to proper
# print("Capital Letters : ",text1.title()
#                                  .strip())

# #convertt to lower
# print("Capital Letters : ",text1.lower().strip())

# Replace
# print("Replace Python word with SQL : ",text1.replace("Python","SQL").strip())

#Countn occurrences of letter of word
# print("Count of o : ",text1.count("o"))

# # Check if text start with something
# print("Start with hello ?",text1.strip().startswith("hello"))

# # Check if only numbers are presents in data
# mobile="9876543210"
# print("Is numeric : ",mobile.isnumeric())


# msg="Welcome to Python Course"

# #Split string into list of words
# words=msg.split()
# print("word list : ",words)

# # J?oin back with hyphen
# joined_text="-".join(words)
# print("Joined text :", joined_text)

msg="Welcome to Python Course"
print("Index of P :",msg.find("P"))

#Extract domain
email="student@example.com"
domain=email[email.find("@")+1:]
print("Domain :", domain)