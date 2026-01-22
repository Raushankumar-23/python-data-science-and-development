# nums=[1,2,3,4,5,6]
# string=["intro","to","list","comps","Raushan","Kumar"]

# results = []
# for i in nums:
#     i=i*2
#     print("i",i)
#     results.append(i)
    
#results=[i*3 for i in nums] #list comprehension

# results = []
# for i in string:
#     i=i.upper()
#     print("i",i)
#     results.append(i)
    
# results = [ i.upper() for i in string] #list comprehension
# results = [ i.upper()+"hi" for i in string] #list comprehension

# print("results!!",results)


# nums=[1,2,3,4,5,6]
# string=["intro","to","list","comps","Raushan","Kumar"]

# def timesFive(num):
#     return num*5

#traditiona method
# result = []
# for i in nums:
#     i = timesFive(i)
#     print("i",i)

# new_nums = [timesFive(i) for i in nums]

# result = [timesFive(i) for i in nums] #list comprehension

# print("results w function",result)

# nums=[1,2,3,4,5,6]
# string=["intro","to","list","comps","Raushan","Kumar"]
# dicts = [{"name":"Raushan"},{"name":"Rohit"}]

# #grab names from dict
# result= []
# for i in dicts:
#     result.append(i["name"])

# #list comprehension
# results = [i["name"] for i in dicts]

# print("results",result,results)

# list commmprehension  if-else

# list1=[1,2,3,4,5,6]

# results = [i*5 if i==3 else i for i in list1]
# result = [i*5 if i>2 else i for i in list1]
# resultes = [i*5 for i in list1 if i>4]

# print("results",results)
# print("result",result)
# print("resultes",resultes)

# Nested if else

# result = [i for i in range(0, 40) if i % 2 == 0 if  i % 3 == 0]
# print(result)

# Nested list comprehension

list = [[i*j for j in range(4,7)] for i in range(6,8)]
print(list)
