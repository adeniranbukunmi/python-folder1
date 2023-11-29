# print("welcome")

# commenting
# we have single and multiline comment
# eg single comment
# print("welcome")

# multiline commit eg
# print("""
#         welcome to opay
#     1. transfer
#     2.change password    

# """)

# python variable

# name = "grace"
# print(name)
# name = input("Enter your name: ")
# how to join variable and string
# print(name, 'is a python developer')

# value1 = input('enter first value: ')
# value2 = input('Second value: ')
# print(value1, value2)
# print(value1 + value2)

# concartination
# print("let me" + "join two" + "strings together")

# ASSIGNMENT
# calculator
# value1 =int(input("enter your first value: "))
# value2 =int(input("enter your first value: "))
# addition= (value1 + value2)
# subtraction= (value1 - value2)
# modulus= (value1 % value2)
# division=(value1 / value2)
# power=(value1 ** value2)


# print(f'the addition of {value1} and {value2} is', addition )
# print('your answer is', subtraction)
# print('your answer is', modulus)
# print('your answer is', division)
# print('your answer is', power)

# print(f"""
#             the addition of {value1} and {value2} is  {addition} 
#             the subtraction of {value1} and {value2} is  {subtraction} 
#             the modulus of {value1} and {value2} is  {modulus} 
#             the division of {value1} and {value2} is  {division} 
#             the power of {value1} and {value2} is  {power} 
# """)

# VARIABLES
# the variable must be descriptive
# variables can be in different forms
# 1. pascal : 
# 2. camel casing
# 3.snake case

# mood =input("enter your mood: ")
# print("i am", mood)

# CLASS WORK
# Fname = input('Enter your first name: ')
# Lname = input(' Enter your Last name: ')
# print('my name is', Fname , Lname)

# print(type(59)): int
# print(type(59.56)):float
# print(type('45''flora')):string
# print(type(2+3j)) complex no


# ASSIGNMENT 2
# what are the different concatenating method that we have
# 1.the use off plus sign (+)
# 2. the use of += sign
# 3.the useof extend to join list
# Fname="grace"

# print("""
#                         BioData
#         my name is  
#         i am from oyo 
#         i leave in ogbomoso
#         i am the last born of my family
#         i love cooking and i am a pro amebo nothing going on in the area that i am not a part of but you will never no i am part of it because of my gentle look.
#         i  am a graduate of chemistry in lautech.
#         currently a data scientist atSQi college of ict ogbomosho


# """)

# 05\10\2023
# FirstName =input('enter first name: ')
# LastName= input('enter last name: ')
# Location= input('location: ')
# Age = int(input('age: '))
# Account_Bal=float(input('account balance: '))

# different concatenation method
# 1. using comma ','
# print('my name is', FirstName, LastName, 'i stay in', Location, 'i am ', Age, 'years old', 'i have', Account_Bal, 'in my acc')

# 2. using plus "+" plus cannot concatenate integer and float it will throw error so you need to convert the integer and float to string by adding parenthesis()
# print('my name is '+ FirstName+ ' '+ LastName+ ', i stay in '+ Location+ ', i am '+ str(Age)+ 'years old'+ ', i have '+ str( Account_Bal)+ ' in my acc.')

#3. using of f-string
# print(f"my name is {FirstName} {LastName}, i stay in {Location}, i am {Age} year old i have {Account_Bal} in my acc.")

# DATA types
# SEQUENCE Type
# A) tuple
# basket ='mango', "orange", 'cashew', 'pawpaw'
# print(type(basket)) at default python see items without a bracket as tuple
# basket =('mango', "orange", 'cashew', 'pawpaw')
# print(type(basket)) with parenthesis python see the item as tuple

# how to convert tuple list
# basket =list(('mango', "orange", 'cashew', 'pawpaw'))
# print(type(basket))

# B) list
# basket =['mango', "orange", 'cashew', 'pawpaw']
# print(type(basket))

# 3.) Range
# for loop function
# basket =['mango', "orange", 'cashew', 'pawpaw']
# for each in basket:
#         print(each)


# ASSIGNMENT 1
# val=range(1, 13)
# val2=range(1,13)
# for x in val:
#     print(f'multiplication {x}')
#     for each in val2:
#      result= x * each
#      print(f"{each} * {x} = {result}")

# ASSIGNMENT 2
# Fname=input('enter your first name: ')
# Lastname=input('enter you last name: ')  
# var=(range(1,100,2))
# var2=(range(1,100,3))
# user=int(input('enter any number within hundred: '))
# if user in var:
#         print("the number you entered is an odd number")
# elif user in var2:
#         print("the number you entered is an even number")
# else:
#         print('enter a number')  

# operators
# >
# <
# ==
# >=
# <=
# !=
# in  (membership operator)
# var1=range(1, 6)
# var2=range(1, 4)
# for all in var1:
#     print(f'multiplication table {all}' )
#     for each in var2:
#      result=each * all
#      print(f"{all} * {each} = {result}")

# correction
# user=int(input('input a number: '))
# remainder= user%2
# # print(remainder)
# if remainder == 0:
#         print(f"{user} is an even number")
# else:
#         print(f"{user} is an odd number")

#you can also do it without putting user in a variable 
# user=int(input('input a number: '))
# if user%2 == 0:
#         print(f"{user} is an even number")
# else:
#         print(f"{user} is an odd number")


# correction2
# number=range(1,13)
# user = int(input('enter a number: '))
# for each in number:
#   result=user * each
#   print(f'{user} x  {each} = {result}')

# for each in range(1,13):
#         print() 
#         print(f'{each} times tables \n')
#         for x in range(1,13):
#                 result= x * each
#                 print(f'{x} x {each} = {result}')

# data types

# 10/10/2023
# correction of assignment1
# student=['rice', 'beans', 'yam']
# print(len(student))
# # adding to a list
# student.append('semo')
# print('list of food after adding semo', student)
# # removing item in a list
# student.remove("yam")
# print('list of food after removing semo', student)

# data type
# bytes type
# var=b'hello'
# print(type(var))
# var2=bytes(50)
# print(var2)
# x=bytearray(5)
# print(memoryview(x))

# conversion
# to check the type of data use, call the function type()
# val = bytes(50)
# val2 = str(val)
# print(val2)
# val2= val.decode()
# print(val2)

# assignment 10\10\2023

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
# 11\10\2023
# ASCII:
# var=chr(65)
# print(var)
# var='opeyemi'
# print(var[2])
# basket=['yam','rice','beans']
# print(len(basket))
# basket=['yam','rice','beans']
# print(basket[0][0])
# print(basket[1][3])
# var=b'hello'
# print(var[1])
# var=chr(101)
# print(var)
# num=bytes(10)
# print(num)
# for each in num:
#     print(str(each))

# PYTHON STRINGS
# name='bukunmi'
# indexing
# print(name[-2])
# slicing
# print(name[0:5])
# print(name[-5:])
# basket=['yam','rice','beans']
# print(basket[:2])

# functions that strings can perform
# text is a python class
# user=input('enter first name: ')
# print(user.capitalize())

# De_good=['bread', 'yam', 'beans','rice',]
# food1=input('first food: ')
# food2=input('second food: ')
# if (food1.capitalize() == 'bread' or food1.capitalize() =='beans') and  (food2.capitalize() ==  'beans' or food2.capitalize() =='bread') :
#         print('i will eat bread and beans')
# else:
#     print("i will not buy anything")

# water=input('do you have water \n yes or no: ')
# money=input('do you have money \n yes or no: ')
# if water.capitalize().strip() == 'yes' and money.capitalize().strip() =='yes':
#         print("i am coming to school")
# elif water.capitalize().strip()=='yes' and money.capitalize().strip() !='yes':
#         print('i dont have money for transport')
# elif water.capitalize().strip()!='yes' and money.capitalize().strip()=='yes':
#         print('i dont have water to  bath')
# else:
#         print('what next')
#         #upper not working
        # all  not working

        # assignment 
# print(""" 
#             Hello!
#                 Welcome to SQI college if ICT
#                 1. are you a student
#                 2.Staff
#                 3.Visitor
# """)
# user=input("chose an option: ")
# if user.strip()=="1":
#     fullname=input('what is your full name: ')
#     department=input('enter your department: ')
#     id_num=input('enter your id number: ')

#     print(f"""
#             dear {fullname}
#         1.have you paid
#         a) yes b)no
# """) 
#     user=input("chose an option: ")
#     if user.strip()=="yes":
#         print("""
#             1.full payment
#             2.part payment 
#             """)
#         user=input("chose an option: ")
#         if user.strip()=="1":
#             print(f'{fullname} with {id_num} in {department} you may go inside your class')
#         elif user == '2':
#             print(f' {fullname}, kindly wait at the front desk to complete your payment')
#     elif user != 'yes':
#         print("""
#             1.would you like to pay now
#                 a)yes b)no
#             """)
#         if user.strip()=="yes":
#             print(f'{fullname} with {id_num} in {department} wait atthe front desk to make payment')
#         elif user == 'no':
#             print(f' {fullname}, payment validate entry, go home')
#     else:
#         print('you cant be on the fence ......pay or leave our school ')            
        
# elif user.strip()=="2":
#     fullname=input('your name sir\Ma: ')
#     print(f"""
#             Hello!! instructor {fullname}
#         you can go in 
#         """) 
# elif user=='3':
#     fullname=input('what your name: ')
#     print("""
#         what are you here for
#         1.pay a visit
#         2.to make enquiry
#         3.others""")  
#     user=input('select an option: ') 
#     if user.strip()=="1":
        
#         print(f'Dear {fullname} we are happy to have you around \n for more enquiries visit our page on social media')
#     elif user == '2':
#             print(f' {fullname}, kindly wait at the front desk to make enquiries or visit our social media page' )
#     elif user == '3':
#             print(f' {fullname}, thanks for coming' )
#     else:
#         print('select an option......or get out ')            
                
# else:
#     print('select an option.......you are not a ghost ')            


# class work
# TEST QUESTION CLASS WORK
# score=0
# answer=['bukunmi', 'rice','2']
# que1=input("""what is your name: 
#             a.bukunmi
#             b.rice
#             c.2
#         """)
# if que1=='a':
#     score+=5
#     print(score)
# elif que1!='a':
#     score=0
# else:
#     print('choose one......')
# que2=input("""what is your name: 
#             a.bukunmi
#             b.rice
#             c.2
#         """)
# if que2=='a':
#     score+=5
#     print(score)
# elif que2!='a':
#     score=0
# else:
#     print('choose one......')
# que3=input("""what is your name: 
#             a.bukunmi
#             b.rice
#             c.2
#         """)
# if que3=='a':
#     score+=5
#     print(score)
# else:
#     print('choose one......')
# que4=input("""what is your name: 
#             a.bukunmi
#             b.rice
#             c.2
#         """)
# if que4=='a':
#     score+=5
#     print(score)
# else:
#     print('choose one......')
# que5=input("""what is your name: 
#             a.bukunmi
#             b.rice
#             c.2
#         """)
# if que5=='a':
#     score+=5
#     print(score)
# else:
#     print('choose one......')


# FUNCTIONS IN PYTHON
# FUNCTION STRIP()

# commented="""my name is diamond from lagos i here to suffocate you....."""
# print(commented.strip().capitalize())
# function replace() mostly use when handling file
# commented="""my name is diamond from lagos. i am here to suffocate you....."""
# new_sentence=commented.replace('diamond', 'gold')
# print(new_sentence)
# print(commented.split()) at defult it split with space if you dont specify what it will you to split it
# print(commented.split("."))
# FUNCTION JOIN()
# word_split= commented.split()
# print(word_split)
# print(" ".join(word_split))
# print(" + ".join(word_split))
# function center()
# name="mercy"
# print(name.center(100))
# function count()
# commented="""my name is diamond from lagos. i am here to suffocate you....."""
# print(commented.count(" diamond "))
# FUNCTION ENCODE()
# name="mercy"
# print(name.encode())
# print(type(name.encode()))

# FUNCTION startwith()
# FUNCTION endwith()

# file_path= r"C:\python-works"
# file= open(file_path,'rt')
# print(file.read())

# scoreA=range(70,101)
# scoreB=
# scoreC=
# scoreD=
# scoreE=

# user=int(input('enter your score: '))
# user=(input('enter your score: '))
# splitted_input=user.split()
# int_input=int(''.join(splitted_input))
# if int_input in range(70,101):
#     print('excellent \n you have done well')
# elif int_input in range(60,70):
#     print('very-good  \n you have done well')
# elif  int_input in range(50,60):
#     print('credit  \n you can do more')
# elif int_input in range(45,50):
#     print('pass  \n put in more effort')
# elif int_input in range(40,45):
#     print('fail  \n o n fi owo daddy e jona')
# elif int_input in range(1,40):
#     print('fail  \n o ti fi owo daddy e jona')
# else:
#     print('you did not write test and you want to see result...dey play ')

    # function find()

# python collection(Array)
# list [] or list() .....orderd, changeable, allows duplicate value,and it can be indexed and you can slice too(becau of the index)
# my_list=list(('shade', 'tola', True, False 12 2.3 'food', 'food'))
# print(len(my_list))
# # slicing
# print(my_list[::3])
# print(my_list[-1])
# print(my_list[::-1])
# print(my_list[-5:-1])
# print(my_list[-5:0])
# print(my_list[-5:])
# my_list[0]='tikristi'
# my_list[:4]=['tikristi', 'noah','grace'] you can increase the index to your desire
# my_list2=['dare', 'ajoke','sule'] 
# #  functions of list
# my_list.append('aderonke')
# my_list.append(my_list2)
# print(my_list)

# print (my_list.index('food'))
# print (my_list)
# my_list.clear()
# print (my_list)
# my_list.('aderonke')
# my_list.insert(3, 'david')
# my_list.extend(my_list2)
# print(my_list)
# my_list.pop()
# my_list.pop(4)
# my_list.remove('shade')
# print(my_list)

# # del my_list
# # print(my_list)

# turple () 
# set {}
# dictionary {key:value}

# name=['student1','student2','student3','student4','student5']
# score=("30", "40", "70", "80", "90")
# name.append(score)
# print(name)
# for student  in name:
#     # print('hello student ')
#     for marks in score:
#         print('student1 your score is',score)


        # corretion
studentScore=[
    [30, 30, 70, 30, 70],
    [20, 60, 10, 80, 90],
    [40, 60, 60, 30, 10],
    [50, 50, 70, 90, 90],
    [10, 20, 70, 80, 70],
]
# x=1
# studentAvgScore=[]
# # # this below is just to print the score in an orderly manner
# for studentScore in studentScore:
#     #  for Score in studentScore:
#     print(f'student{x} score list {studentScore}')
#     x+=1 
    # it end here

# for studentScore in studentScore:
#     Sum = 0
#     length_of_studentScore=len(studentScore)
#     for Score in studentScore:
#         Sum += Score
#         average_score= Sum/length_of_studentScore
#     # print(f'student{x} total score {Sum}\n\n student total course is { length_of_studentScore} \n student{x} average score is {average_score}\n')
#       
#  this below will work without the print above
#     studentAvgScore.append(f'student{x}: average score is {average_score}')
#     x+=1
# print(studentAvgScore)


# assignment one
# studentScore=[
#     [30, 30, 70, 30, 70],
#     [20, 60, 10, 80, 90],
#     [40, 60, 60, 30, 10],
#     [50, 50, 70, 90, 90],
#     [10, 20, 70, 80, 70],
# ]
# list_for_all=[]
# x=1
# for each in studentScore:
#     adding_each =sum(each)
#     total_num_of_student=len(studentScore)
#     average= adding_each/total_num_of_student 
#     # print(f'{x} the sum of individual student is {adding_each} with this { average}')
# #   this below will work without the print above
#     list_for_all.append(f'student{x}:{average}')
#     x+=1
# print( list_for_all)


#  assignment 2
# TO-DO LIST
# user=input('what is you name: ')
# user1=input( f' {user} do you want to add to your to_list ? Yes or No: ')
# todo_list=[]
# while user1.capitalize().strip()=='Yes':
#     todo_list.append(input(f' {user} what do you want to do : '))
#     print(todo_list)
#     user1=input('do you want to add to your list ? Yes or No: ')

#     print('do you want to add to you list ? Yes or No: ')

#  OPTIMIZE TO-DO LIST
# name=input('what is your name: ')
# print(f"""
# welcome  {name}, i am sure you want to have a day fulfilled
#     what and what are you doing today
#     1.create a todo-list
#     2.exit
# """.center(200))
# todo_list=[]
# user=input('select an option: ')
# if user=='1':
#     for each  in range(500):
#         print(f"""
#         what and what are you doing today
#             1.add to a list
#             2.view list
#             3.remove from a list
#             4.del
#             """.center(1000))
#         user=input('select an option: ')
#         if user.capitalize().strip()=='1':
#             todo_list.append(input('pen down what you want to do : '))
#             # user1=list(todo_list)
#             # user1.append(user1)
#             print(todo_list)
#         elif user=='2':
#             # print(input("do you have a list? yes or no : "))
#             if (len(todo_list)>0):
#                     print(todo_list)
#             else:
#                 print(f'{name} kindly select add to a list')
        
#         elif user=='3':
#                 todo_list.pop(int(input('enter the list to remove: '))-1)
#                 print(todo_list)
#         elif user=='4':
#             del(todo_list)
            # delete_for_me=[]
            # print(input('are you sure you want to delete all the list? yes or no: '))
            # if user=='yes':
            #     delete_for_me.append(todo_list)
            # del(delete_for_me)

# correction of todo list
# while True:
#     print('my todo application'.center(100))
#     user=input("""
#             1. create a todo list
#             2.exit 

#                 chose an option: """)
#     todo_list=[]
#     if user =='1':
#         while True:
#             # todo_list=[] this wont work here, you have to put it before the if statement or at the beginning of the code
#             todo_option=input("""
#             1. add to list
#             2.edit an item
#             3.remove an item
#             4.delete list
#             5.view todo list  
#             6.exit
            
#                 chose an option: """)
#             if todo_option=="1":
#                 add_list=input("""
#                 Add to list:  """)
#                 todo_list.append(add_list)
#             elif todo_option =="2":
#                 user=int(input('''enter the number of the item you would like to edit 
#                 HERE: '''))
#                 if user:
#                     todo_list[user-1]=input(f'editing ({todo_list[user-1]}) to what: ')
#                     numbering=1
#                 for each_list in todo_list:
#                     print(f"""
#                     {numbering}.{each_list}
#                 """)
#                     numbering +=1
#                 else:
#                     print('invalid option')
#             elif todo_option=="3":
                
#                     numbering=1
#                     for each_list in todo_list:
#                         print(f"""
#                     {numbering}.{each_list}""")
#                         numbering +=1

#                     todo_list.pop(int(input('enter the list to remove: '))-1)
#                     numbering=1
#                     for each_list in todo_list:
#                         print(f"""
#                     {numbering}.{each_list}""")
#                         numbering +=1
#             elif todo_option=="4":
#                 del(todo_list)
#                 break
#             elif todo_option=="5":
#                 numbering=1
#                 for each_list in todo_list:
#                     print(f"""
#                     {numbering}.{each_list}""")
                
#                     numbering +=1
#             elif todo_option=="6":
#                 print(8)
#                 exit()
#     elif user=='2':
#         exit()
#     else:
#         print('invalid')

# TUPLE
# tuple Is a collection that is orderd indexed 
# class work
# Jss2_student=[
#     ('tolu', 50, 'c'),
#     ('kunle', 10, 'f'),
#     ('grace', 80, 'A'),
#     ('daniel', 20, 'f'),
#     ('mich', 30, 'f'),
#     ('kike', 70, 'A'),
#     ('stifini', 40, 'E')
# ]
# Total_Score=[]
# names=[]
# for name, score, grade  in Jss2_student:
#     names.append(name)
#     Total_Score.append(score)
# score_total=sum(Total_Score )
# Avg_score= score_total/len(Total_Score)
# min_score=min(Total_Score)
# print(Avg_score)
# print(min_score)
# min_score_index=Total_Score.index(min_score)
# # names[min_score_index]
# print(names[min_score_index])
# # print(Total_Score)

# while loop


# SET is unordered, unchangeable and does mot allow duplicate value; unless you convert it to another data type before you can change it
# eg
name={'dupe', 'kike', 'kike','rolake'}
surname=('titi','dolapo','mubarak')
# newname=list(name)
# newname[1]='tunji'
# print(newname)
# print(type(name))
# print(name)
# functions of set
# name.add('kunle')
# name.update(surname)
# print(name)
# family_name=name.union(surname)
# print(family_name)
# name.remove('titi')
# name.pop()
# name.clear()
# name.discard()

set1={1, 2, 3, 4, 5, 6, 7, 8}
set2={ 9,10,11}
set3={1,  5, 7, 8}
set4=set1 - set2
# set4=set1.union( set2)
set4=set1.intersection( set2)
# intercept=set1.intersection( set2).intersection(set)
# print(set4)
set1.intersection_update( set2)

# print(set1)
# set1.intersection_update( set2)
set4=set1.symmetric_difference_update( set2)
# print(set4)
# print(set2.isdisjoint(set1)) this will be false because there is a value common betwen them
# print(set1.issuperset(set2))

# user=input('''
#         how many set do you want to work with: ''')
# for x in user:
#     adding_set=sum(x)
# user_set = set()  
# while True:
#     user_input = input("enter set items : ")
#     # for each in user_input:

#     user_set.add(user_input)
#     # user_set.union(user_input)

#     print("User set:", user_set)

# number_of_set=int(input("enter the number of set you want to perform: "))
# list_of_set=[]
# y=0
# for each in range(1, number_of_set+1):
#     list_of_set.append(set())
#     number_of_item_in_set=int(input(f'enter all the items in set {each} : '))
#     items=[]
#     x=1
#     for all in range(number_of_item_in_set):
#         item=input(f'item {x}: ')
#         converted_item=int(item)
#         items.append(converted_item)
#         x+=1

#     list_of_set[y]=set((items))
#     y+=1
# # print(type(converted_item))
#     print((list_of_set))
#     x=1
#     for all in list_of_set:
#         difference= list_of_set - all
#         print(f'the {difference} of set {x} is')
#         x+=1


# user=int(input('enter numbers of set for operation: '))
# set_list=[]
# y=0
# for each in range(1, user+1):
#     set_list.append(set())
#     items_in_set=int(input(f'enter the number of items in set {each}: '))
#     items=[]
#     x=1
#     for all in range(items_in_set):
#         item=int(input(f'enter item {x}: '))
#         converted_item=int(item)
#         items.append(converted_item)
#         x+=1
#         set_list[y]=set((items))
#     # x=1
#     # individual_set=[]
#     # for set in set_list:
#     #         individual_set.append(set)
#     #         print(f'set {x}  is {individual_set}')
#     #         x+=1
#     print(set_list)
#     y+=1

    # Collect sets from the user
# user_set1 = set(input("Enter the first set (comma-separated): ").split(','))
# user_set2 = set(input("Enter the second set (comma-separated): ").split(','))

# # Perform a set operation
# result = user_set1.union(user_set2)
# print("Result:", result)


set_list=int(input('enter number of set for operation: '))
sets=[]
y=0
for each in range(1,set_list+1):
    sets.append(set())
    num_of_set_item=int(input(f"enter number of  value in set {each}: "))
    items=[]
    x=1
    for all in range(num_of_set_item):
        item=int(input(f" enter items in set {x}:  "))
        # convert_item=int(item)
        items.append(item)
        x+=1
    sets[y]=set((items))
    y+=1
    print(sets)
z=1
for each_set in sets:
    print(f'''
        set{z}: {each_set}
        ''')
    z+=1
    print("""
    1. union
    2.intersection
""")
    user=input('select the operation you want to perform: ')
    q=1
    if user =='1':
        print('set(?) union set(?)')
        setA=int(input('select the number at which the set you want to work with is: '))
        setB=int(input('select the number at which the set you want to work with is: '))
        setA=set(sets[setA-1])
        setB=set(sets[setB-1])
        print(f'{setA} union {setB} = {setA.union(setB)}')
    elif user =='2':
        print('set(?) intersection set(?)')
        setA=int(input('select the number at which the set you want to work with is: '))
        setB=int(input('select the number at which the set you want to work with is: '))
        setA=set(sets[setA-1])
        setB=set(sets[setB-1])
        print(f'{setA} intersection {setB} = {setA.intersection(setB)}')
    q+=1
else:
    print('invalid operation')



# DICTIONARY
# DICTIONARY IS ORDED, CHANGEABLE,IT DOSE NOT ALLOW DUPLICATE VALUE AND IT IS UNINDEXED
# IT IS WRITTEN USING {KEY:VALUE} OR DICT(KEY=VALUE)

Vehicle={'name':'toyota',
        'model':'highlander',
        'color':'black',
        'year':2022,
        'new':True,
        'status':{
            'brand new':True,
            'fairly used':False,
            'hand to hand':True
        }
        }
# we dont say at the index in dictionary we use key
# Vehicle['year']=2023
# Vehicle['status'] ['brand new']=False
# print(Vehicle) 
# print(Vehicle.items()) 
# print(Vehicle['status'].keys()) 

# for each in Vehicle.values():
# for each in Vehicle['status'].values():
# for x, y in Vehicle.items():
    # print(f'{x}:{y}')

# duplicate=Vehicle.copy()
# duplicate['year']=2012
# print(duplicate)
# print(Vehicle)

# print(Vehicle.get('year'))
# Vehicle.popitem()
# print(Vehicle)
# Vehicle.pop('year')
# print(Vehicle)
# Vehicle.update({'transmission':'automatic'})
# print(Vehicle)

# class work

# test question
# Q_and_A={
#         'b':'what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'c':'what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'd':'what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'a':'what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'b':'what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         }
# score=0
# x=1
# for ans,ques in Q_and_A.items():
#     print(f'{x}.', ques,'\n')
#     user=input('ans: ')
#     if user.strip().upper()== ans: 
# #         print('correct')
#         score+=5
#     x+=1
#     else:
#         print('incorrect')
# print('your score is', score)


