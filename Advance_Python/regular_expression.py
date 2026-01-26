# \ → escape character
# [ ] → character set
# ^ → start of string
# $ → end of string
# . → any character
# | → OR
# ? → zero or one

# \ → Used to drop the special meaning of the character following it.
# [ ] → Represent a character class.
# ^ →Matches the beginning.
# $→Matches the end.
# . any character except newline.
# |→Means OR (matches with any of the characters/patterns separated by it).
# ?→Matches zero or one occurrence.
# *-> Matches any number of occurrences (zero or more).
#+ → Matches one or more occurrences.
#{ } → Indicates the number of occurrences (exact or range).
#( ) → Encloses a group of regular expressions (grouping).


# import re
# a="charlie chaplin coa and the chacolate fac1"
# b="raushan.engineer@gmail.com"
# c="hello"
# d="xyz,yz,xyzz,xyyz,xxzzy,zyz,xxyyzz"

# match=re.search(r"\.",b)
# print(match)

# match=re.findall(r"\.",b)
# print(match)

# match=re.search(r"[@]",b)
# print(match)

# match=re.findall(r"[x]",d)
# print(match)

# match=re.search(r"^h",c)
# print(match)
# match=re.search(r"^e",c)
# print(match)
# match=re.search(r"^rau",b)
# print(match)

# match=re.search(r"com$",c)
# print(match)

# match=re.search(r"o$",c)
# print(match)

# match=re.search(r"c.a",a)
# print(match)

# match=re.findall(r"c.a",a)
# print(match)


# match=re.search(r"cha|fac",a) #atleast one match
# print(match)

# match=re.findall(r"cha|fac",a)
# print(match)

# match=re.search(r"chr?a",a)
# print(match)

# match=re.findall(r"chr?a",a) # 0 or 1 time occur
# print(match)

# match=re.search(r"ch*a",a)
# print(match)
# match=re.findall(r"ch*a",a)
# print(match)

# match=re.search(r"xy+z",d)
# print(match)
# match=re.findall(r"xy+z",d)
# print(match)


# match=re.search(r"x{2,4}",d)
# print(match)
# match=re.findall(r"x{2,4}",d)
# print(match)
#match=re.findall(r"y{2,4}",d)
#print(match)

# match=re.findall(r"(x|z)yz",d) # start x or z
# print(match)


# \A → Matches the start of the string
# \b → Matches a word boundary
# \B → Matches not a word boundary
# \d → Matches any digit (0–9)
# \D → Matches any non-digit character
# \s → Matches any whitespace character
# \S → Matches any non-whitespace character
# \w → Matches any alphanumeric character (letters, digits, underscore)
# \W → Matches any non-alphanumeric character
# \Z → Matches the end of the string

import re

a="harry1 potter23 4@5"

# match=re.search(r"\Ahar",a)
# print(match)
# match=re.findall(r"\Ahar",a)
# print(match)
# match=re.findall(r"\Ah",a)
# print(match)
# match=re.findall(r"\Apot",a)
# print(match)

# match=re.findall(r"p\b",a)
# print(match)
# match=re.findall(r"\bpo",a)
# print(match)

# match=re.search(r"ha\B",a)
# print(match)
# match=re.search(r"\Ber",a)
# print(match)

# \d extract digit

# match=re.search(r"\d",a)
# print(match)
# match=re.findall(r"\d",a)
# print(match)

#\D  without number

# match=re.search(r"\D",a)
# print(match)
# match=re.findall(r"\D",a)
# print(match)

#\s find spaces

# match=re.search(r"\s",a)
# print(match)
# match=re.findall(r"\s",a)
# print(match)


#\S except spaces

# match=re.search(r"\S",a)
# print(match)
# match=re.findall(r"\S",a)
# print(match)

#\w except spaces number and char

# match=re.search(r"\W",a)
# print(match)
# match=re.findall(r"\W",a)
# print(match)

#\Z 

# match=re.search(r"5\Z",a)
# print(match)
# match=re.findall(r"@5\Z",a)
# print(match)


# [atx] → Matches any one character that is a, t, or x
# [a-h] → Matches any lowercase letter from a to h
# [^atx] → Matches any character except a, t, and x
# [0123] → Matches any one digit from 0, 1, 2, or 3
# [0-9] → Matches any digit from 0 to 9
# [0-7][0-9] → Matches any two-digit number from 00 to 79
# [a-zA-Z] → Matches any alphabet (lowercase or uppercase)
# [+] → Inside a character set, + has no special meaning and matches the literal + character



# import re

# a="charlie and the chocolate factory"
# b="12hi3join#$@^67HELLO739&"

# match=re.findall("[atx]",a)
# print(match)
# match=re.findall("[^atx]",a) #excwept axt
# print(match)

# match=re.findall("[a-t]",a) # alphabet between a to z
# print(match)
# match=re.findall("[1234]",b) 
# match=re.findall("[0-9]",b) 
# print(match)

# match=re.findall("[0-9][0-7]",b) 
# print(match)
# match=re.findall("[a-zA-Z]",b)
# print(match)

# match=re.findall("[$]",b)
# print(match)



# functions in RegEx

import re

a = """John has scored 89 marks
# Lisa has scored 90 marks
# Divid has scored 70 marks"""

# b="fantastis  5 turtle"

# print(re.findall(r"\d+", a))
# print(re.findall(r"[A-Z][a-z]*", a))


# p=re.compile("[a-d]")
# print(re.findall(p,a))

# p=re.compile("\d+")
# print(re.findall(p,a))

# p1=re.compile("[0-9]")
# print(re.findall(p1,a))

#  split

# print(re.split(r"\d+",a))
# print(re.split(r"\d+",b))

print(re.sub(r"\s","",a))
print(re.sub(r"\s","",a))

# print(re.escape(a))

# print(re.search("\d+",a))




import re

a = "John has scored 89 marks"
# # Lisa has scored 90 marks
# # Divid has scored 70 marks"""


# match=re.search(r"\d+",a)
# print(match)
# print(match.re)
# print(match.string)
# print(match.start())
# print(match.end())
# print(match.span())
# print(match.group())

# match1=re.search(r"\w{2} s",a)
# print(match1)
# print(match1.group())


# verify phone number

# import re

# phn = "225-444-8787"

# if re.fullmatch(r"\d{3}-\d{3}-\d{4}", phn):
#     print("it is verified number")
# else:
#     print("incorrect number")



#verify email
# import re

# email="rohit781@gmail.com  rohit@.com raushan.98@yahoo.com"

# print(re.findall(r"[\w._]{0,20}@[\w-].[A-Za-z]{2,3}",email))

# print(len(re.findall(r"[\w._]{0,20}@[\w-].[A-Za-z]{2,3}",email)))

