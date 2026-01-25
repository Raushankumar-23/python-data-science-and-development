# how to create iterator

# l=[10,20,30,40]

# iter_obj=iter(l)
# print(iter_obj)
# print(type(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# for ele in iter_obj:
#     print(ele)

# data=[1,2,3,4,5,6,7]
# it=iter(data)
# while True:
#     try:
#         print(next(it))
#     except Exception as e:
#         break
    

# data=[1,2,3,4,5,6,7]
# ite=iter(data)
# print(ite.__next__())
# print(ite.__next__())
# print(ite.__next__())
# print(ite.__next__())


# string="Raushan Kumar"
# iterate=iter(string)

# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())

#create iterator

# class Fantastic_Five:
#     def __init__(self):
#         self.num=1
        
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num<=5:
#             value=self.num
#             self.num+=1
#             return value
#         else:
#             raise StopIteration
        
# FF=Fantastic_Five()

# print(FF)
# for i in FF:
#     print(i)
    



