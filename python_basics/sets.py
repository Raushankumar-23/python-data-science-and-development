# Not accepet duplicates
fruits={"Apple","Banana","Apple","Mango"}
print(fruits)
for i in fruits:
    print(i)

# Add items
# fruits.add("Orange")
# print(fruits)

# Remove item
# fruits.discard("Banana")
# print(fruits)

# Set operations
# a={1,2,3}
# b={3,4,5}
# print("Union : ",a|b)
# print("Intersaction : ",a&b)
# print("Difference : ",a-b)
# print("Difference : ",b-a)
# print("Symmetric Difference:",a^b)

# Remove duplicates
# cities=["Mumbai","Pune","Delhi","Mumbai"]
# unique=set(cities)
# print("Unique Cities :",unique)

# Missiing values
# list1 = {"SQL","Excel","Power BI"}
# list2 = {"SQL","Power BI"}
# missing=list1-list2
# print("Missing : ",missing)

# Common skills
deptA={"SQL","Excel","Python"}
deptB={"Excel","Python","Power BI"}
print("Common skills : ",deptA & deptB)