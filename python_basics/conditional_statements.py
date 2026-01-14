# Logical Conditions
# if else 

# age=float(input("Enter your age : "))
# if age>=18:
#     print("You are eliglible for voting")
# else:
#     print("Not eliglible for voting")

# Discount cheaker
# amount=float(input("Enter your purches amount : "))
# if amount >=1000:
#     print("You get a discount")
# else:
#     print("No discount")

# marks = int(input("Enter your Marks : "))
# if marks >=90:
#     print("A grade")
# elif marks >=60:
#     print("B grade")
# elif marks >=35:
#     print("C grade")
# else:
#     print("Fail")

# password=input("Enter your password : ")
# if password=="Admin@1":
#     print("Login sucessful")
# else:
#     print("Wrong password")

#Email Validation
# email = "user@example.com"
# if "@" in email and "." in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")
    
#Advance : Missing Data Check
# value = "sdf"
# if value =="":
#     print("Missing Data Found")
# else:
#     print("Data available")

security_code = int(input("Enter a security code : "))

if security_code == 5566:
    department = input("Enter your department : ")

    if department == "Finance":
        access_level = int(input("Enter your access level : "))

        if access_level >= 5:
            print("Access Granted : Welcome to the meeting room")
        else:
            print("Insufficient access level")
    else:
        print("Access denied : Department not allowed")
else:
    print("Invalid Security Code")

    
# reg_number = int(input("Enter your registration number : "))

# if reg_number == 1221:
#     exam_subject = input("Enter exam subject : ")

#     if exam_subject.title() == "Python":
#         password = int(input("Enter password : "))

#         if password == 8888:
#             print("Login Successful! Start your exam")
#         else:
#             print("Wrong password")
#     else:
#         print("Subject not available")
# else:
#     print("Registration failed")
