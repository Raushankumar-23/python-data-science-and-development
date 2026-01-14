# Python Input, Type Casting, and Basic Calculations

# input take by default string Data Type

# name=input("Enter your name : ")
# print("Welcome ",name)

# age=input("Enter your age : ")
# print("Your age is ",age)
# print(type(age))

# age=int(input("Enter your age : "))
# print("Your age is ",age)
# print(type(age))

# age=float(input("Enter your age : "))
# print("Your age is ",age)
# age+=4
# print("Your age is ",age)
# print(type(age))

# temperature=float(input("Enter today's temp : "))
# print(temperature,type(temperature))
# print(temperature,type(int(temperature)))
# print(temperature,type(str(temperature)))

# Total Sales Calculator
# product = input("Product Name: ")
# quantity = int(input("Enter quantity sold: "))
# price_per_unit = float(input("Enter price per unit: "))

# total_sales = quantity * price_per_unit

# print("Product:", product)
# print("Total Sales Amount =", total_sales)

#"Create a Python Program to Generate an Employee Salary Slip"
#Write a Python program that asks the user to enter:

Employee_name = input("Enter a Employee name : ")
Basic_Salary = float(input("Enter Basic Salary : "))
Bonus_Amount = float(input("Enter Bonus Amount : "))
Tax_Percentage = float(input("Enter Tax percentage : "))

#Your program should calculate:
Gross_Salary = Basic_Salary + Bonus_Amount
Tax_Amount = (Gross_Salary * Tax_Percentage) / 100
Net_Salary = Gross_Salary - Tax_Amount

# Finally, print a clean and clear Salary Slip showing all the values.
print("Employee Name : ",Employee_name)
print("Gross Salary : ",Gross_Salary)
print("Tax Cutting : ",Tax_Amount)
print("Net Salary",Net_Salary)
print(Employee_name,Net_Salary)