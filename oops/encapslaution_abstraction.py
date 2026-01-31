#Encapsulation & Abstraction

# class Finance:
#     def __init__(self):
#         self.revanue=100000
#         self.nuber_of_eployee=114

# f1=Finance()
# print(f1.__dict__)

# class HR:
#     def __init__(self):
#         self.number_of_emp=32
#         f1.revanue=1
        
        
# h1=HR()
# print(f1.__dict__)



# private


# class Finance:
#     def __init__(self):
#         self.__revanue=100000 # private
#         self._nuber_of_eployee=114 # protected

# f1=Finance()
# print(f1.__dict__)

# class HR:
#     def __init__(self):
#         self.number_of_emp=32
#         f1.__revanue=0
        
        
# h1=HR()
# print(f1.__dict__)



# access private data

class Finance:
    def __init__(self):
        self.__revanue=100000 # private
        self.__nuber_of_eployee=114 # private
        
    def display(self):
        print