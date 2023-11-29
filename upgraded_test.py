# def landing_page():
#     print("""
#                 welcome, select one to go to the next page
#         1. Register for test 
#         2. log-in
#         3.exit
#         """)
#     user = input("specify:  ")
#     if user == "1":
#         print(f"mid term test".center(100))
#         register_for_test()
#     elif user =="2":
#         log_in()
#         test()


# def register_for_test():
#     Fullname = input('enter your full name: ')
#     student_id = input(' enter your student ID: ')
#     G_mail = input(" email or username: ")      
#     password =input("enter a password: ")

# def log_in():
#     G_mail = input(" student ID: ")      
#     password =input("enter a password: ")

# def test():
#     Q_and_A={
#         'b':'1.what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'c':'2.what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'd':'3.what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'a':'4.what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         'b':'5.what is your name \n a.) bukunmi b)tolu c)daniel d)bolu',
#         }
#     score=0
#     # x=1
#     for ans,ques in Q_and_A.items():
#         print(f'{x}.', ques,'\n')
#         user=input('ans: ')
#     if user.strip().upper()== ans: 
#     #         print('correct')
#         score+=5
#         # x+=1
#     else:
#     # print('incorrect')
#         print('your score is', score)
# landing_page()



