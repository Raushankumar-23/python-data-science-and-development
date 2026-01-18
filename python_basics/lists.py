# Lists

# Create lists
# fruits=["Apple","banana","Mango"]
# print(fruits)
# print(fruits[1])
# print(fruits[1].title())

# update list
# fruits=["Apple","Banana","Mango"]
# fruits[1]="Orange"
# fruits[-1]="Grapes"
# print(fruits)
# print(fruits[-1])

#add items
# fruits=["Apple","Banana","Mango"]
# fruits.append("Orange")
# print(fruits)

#Remove items
# fruits=["Apple","Banana","Mango","Orange"]
# fruits.remove("Mango")
# fruits.pop(1)
# print(fruits)

# Slicing
# nums = [10,20,30,40,50]
# print(nums[1:3])

# for i in nums:
#     print(i)

# Clean city names
# raw = ["mUMbai"," Delhi","Pune"]
# clean=[]
# for c in raw:
#     clean.append(c.strip().title())
# print(clean)

# Replace wrong spellings
wrong = ["Kolkatta","Bengluru"]
fixed = []
for c in wrong:
    c = c.replace("Kolkatta","Kolkata").replace("Bengluru","Bengaluru")
    fixed.append(c)
print(fixed)