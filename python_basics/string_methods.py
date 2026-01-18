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

# msg="Welcome to Python Course"
# print("Index of P :",msg.find("P"))

# #Extract domain
# email="student@example.com"
# domain=email[email.find("@")+1:]
# print("Domain :", domain)

# num_list = "0123456789"
# print(num_list[:])
# print(num_list[3:])

# text="xbjsbjsj"
# print(text.count("j"))
# print(text.count("j",3,6)) # 3 say 6 tak j kitne bar aa raha hai

# list=["Chowmien","Roll","Munchurian","Masala Dosa"]
# print("-".join(list))

# s="Pushpa PushRaj Jhukega nai"
# print(s.startswith("Pushpa"))
# print(s.startswith("pushpa"))

# s="Pushpa123Raj"
# print(s.isalnum())
# print(s.isalpha)
# s="123"
# print(s.isdigit())

# s="PushpaRaj"
# print(s.isupper())
# print(s.islower())

# s="Pushpa Push Raj Jhukega Nai"
# print(s.istitle())

# s="Pushpa Raj"
# print(s.isspace())

# text="My Name is Pushpa"
# print(text)
# print(text.find("is")) #provide ist index of sub string
# print(text.find("n"))# if not present give -1

# text="My Pushpa is Pushpa"
# # print(text.find("Pushpa"))
# print(text.index("Pushpa"))
# print(text.index("na"))

text="My Pushpa is Pushpa"
print(text.rfind("Pushpa"))

