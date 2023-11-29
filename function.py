# unperametize function
# def addition ():
#     value1=int(input('enter first value: '))
#     value2=int(input('enter second value: '))
#     result= value1 + value2
#     print(f" ans: {result}")
# addition()

# parametrized function
# def addition ( value1, value2=10):
#     result= value1 + value2
#     print(f" ans: {result}")

# addition(value1=int(input("enter the first value:  ")), value2=int(input("enter the second value:  ")))

# def addition ( value1:int, value2=10):
#     result= value1 + value2
#     print(f" ans: {result}")

# addition(value1=int(input("enter the first value:  ")), value2=int(input("enter the second value:  ")))

# we have global and local varable

# unparametize function
# using a global varable
# val1=12

# def addition (val3):
#     # or make the value a global variable inside the function
#     global val2
#     val2=10
#     result= val1 + val2 +val3
#     print(f" ans: {result}")
#     subtraction()

# def subtraction():
#     result= val1 + val2 
#     print(f" ans: {result}")
# addition(int(input('enter value 3: ')))

# CALCULATOR
# def landing_page():
#     print("""
#     my calculator
#         1.addition
#         2.subtraction
#         3.division
#         4.exit
# """)
#     user=input("select an option: ")
#     if user=='1':
#         addition()
#     elif user=='2':
#         subtraction() 
#     elif user=='3':
#         division() 
#     elif user=='4':
#         exit() 
#     else:
#         print("invalid input")

# def addition():
#         value1=int(input("enter value one: "))
#         value2=int(input("enter value two: "))
#         result= value1 + value2 
#         print(f" ans: {result}")
#         # addition()

# def subtraction():
#         value1=int(input("enter value one: "))
#         value2=int(input("enter value two: "))
#         result= value1 - value2 
#         print(f" ans: {result}")
#         # subtraction()

# def division():
#         value1=int(input("enter value one: "))
#         value2=int(input("enter value two: "))
#         result= value1 / value2 
#         print(f" ans: {result}")
#         # division()
# while True:
#     landing_page()

# def welcome(name):
#     #  note return is not visible
#      return f" welcome to SQI {name}."
# wel=welcome('grace')
# print(wel)


# def Ussd(code):
#     if code !='*312#':
#         print('invalid code')
#         Ussd(input("enter ussd code: "))
#     print("""
#         1.data plans 
#         2.get 3GB for #800
#         3.borrow credit/recharge
#         4. exit
#     """)
#     user=input("option: ")
#     if user=='1':
#         buy_data()
# def buy_data():
#     print("""
#             Dear customer,
#                     you dont have any active data bundle 
#                 please dial *312*1# to buy another data bundle.
#         """)
# def buy():
#     print("""
#             Dear customer,
#                     you dont have any active data bundle 
#                 please dial *312*1# to buy another data bundle.
#         """)
# Ussd(input("enter ussd code: "))



# landing_page
# Code ="*323#"
# user=input('enter ussd code: ')
# if user!=Code:
#     print('invalid ussd......')
#     if user==Code:
#         print("""
#             1.access plan balance
#             2.Business plan Balance
#             3.FBB balance
#             4. Balance check
#     """)
#         user=input('select an option: ')
#         if user=="1":
#                     print("""
#                 Dear customer,
#                         you dont have any active data bundle 
#                     please dial *312*1# to buy another data bundle.
#         """)
#         elif user=="2":
#             print("""
#             1.voice bundle
#             2.MSME learning bundles
#             99.Next
#             00. Main Manu
#     """)
#         elif user=="3":
#             print("""
#             Your data balance SME Beneficiary: 0.0
#                 sub now or we block your line
#     """)
#         elif user=="4":
#             print("""
#                 Dear customer, i have told you earlier
#                         you dont have any active data bundle 
#                     please dial *312*1# to buy another data bundle.
#         """)
# else:
#     print('enter an mtn ussd code')
#     exit()

# def landing_page():
#     print("""
#                 welcome, select one to go to the next page
#         1. sign up 
#         2. sign-in
#         3.exit
#         """)
#     user = input("specify:  ")
#     if user == "1":
#         print(f"sign_in".center(100))
#         sign_up()
#         sign_in()
       

#     elif user == "2":
#         print(f"ign_in")
#         sign_in()
#         front_page()
#     elif user == "3":
#         exit()

#     else: 
#         print ("select option within")
#         landing_page()




# # ASSIGNMENT
# def sign_up():
#     firstname = input('enter your first name: ')
#     lastname = input(' enter your last name: ')
#     G_mail = input(" email or username: ")      
#     password =input("enter a password: ")

#             # for G_mail in "name@gmail.com":

# def sign_in():
#     G_mail = input(" email or username: ")      
#     password =input("enter a password: ")
#             # for G_mail in "name@gmail.com":

# def front_page():
#     print(f" your acount registration is successful")
#     list_of_set=int(input('enter the number of set you want for operation: '))
#     set_list=[]
#     y=0
#     for each_set in range(1, list_of_set+1):
#         set_list.append(set())
#         number_of_value_in_each_set=int(input(f"enter total items in set {each_set}: "))
#         items=[]
#         x=1
#         for each_item in range( number_of_value_in_each_set):
#             item=int(input(f'{x}. enter item {x}: '))
#             items.append(item)
#             x+=1
#         set_list[y]=set((items))
#         y+=1
#         print(set_list)
# # while True:
# landing_page()


# FUNCTION EXAMPLE
import sys
func= ""
count=5
def login():
    global count
    user_name=input("enter your username >")
    password=input("enter your password >")
    if user_name.capitalize()=='bukunmi' and password.strip()=="1234":
        operation()
    else:
        count -=1
        if count == 0:
            return 0
        print(" one of the login details is not correct. try again," +str(count)+ "attempt left")
        login()

def operation():
    global func
    print("""Enter your operation
            1.Addition
            2.subtraction
            3.division
            4.quit""")
    option = input(">>> ")

    if option=="1":
        func="addition"
        addition()

    elif option=="2":
        func="subtract"
        subtract()

    elif option=="3":
        func="division"
        division()

    elif option=="4":
        sys.exit
    else:
        print("invalid input")
        operation()

def tryAgain():
    print("enter 1. perform operation again \n 2.go to menu")
    user= input(">>>")
    if user=="1":
        if func=="addition":
            addition()
        elif func=="subtract":
            subtract()
        elif func=="division":
            division()
    elif user=="2":
        operation()
    else:
        print('invalid input')


def addition():
    print("addition operation")
    val1=int(input('enter value 1 >'))
    val2=int(input('enter value 2 >'))
    print(val1+val2)
    tryAgain()

def subtract():
    print("subtraction operation")
    val1=int(input('enter value 1 >'))
    val2=int(input('enter value 2 >'))
    print(val1-val2)
    tryAgain()

def division():
    print("division operation")
    val1=int(input('enter value 1 >'))
    val2=int(input('enter value 2 >'))
    print(val1/val2)
    tryAgain()

login()

