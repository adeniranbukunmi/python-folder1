# Python Error Handling
# Two types of error in programming:
# .compile time error
# .run time error

# try and except, finally 

# def simpleCal():
#     for i in range(5):
#         a = int(input("enter quotient value"))
#         b = int(input("enter divisor value"))
#         print(a/b)

# simpleCal()

# def cal():
#     for i in range(5):
#         a = int(input("enter quotient value"))
#         b = int(input("enter divisor value"))
#         try:
#             print(a/b)
#         except:
#             print("divisor can not be zero")
# cal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             print(a/b)
#         except:
#             print("divisor can not be zero")
# cal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except ValueError:
#             print("Your value must not be letter or decimal")
# cal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except ValueError:
#             print("Your value must not be letter")
#         except:
#             pass
#         else: # execute if no error was raised
#             print("no error was raised")
#         finally: # execute either there is error or not
#             print("the execution was successful")

# cal()

# import re
# a = input("enter quotient value")
# b = input("enter divisor value")
# if re.search(r'[a-zA-Z]', a) or re.search(r'[a-zA-Z]', b):
#     raise TypeError("first value or second value cannot contain letters")
# else:
#     print(int(a)/int(b))
