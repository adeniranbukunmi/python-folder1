Q_and_A={'c':'1.What is the primary function of the Central Processing Unit (CPU) in a computer?\n A) Storage of dat B) Display of graphics C) Execution of instructions D) Network connectivity',
    'c':'2.Which programming language is known for its use in web development and can be executed in a web browser?\n A) PythonB) Java C) HTML D) C++',
    "a":"3.What does RAM stand for in computer terms?\n A) Random Access Memory B) Read-Only Memory C) Real-time Algorithm Machine D) Remote Access Method",

    'c':'4.What does the acronym "URL" stand for in the context of the internet?\n A) Universal Resource Locator  B) Uniform Resource Locator C) Unifying Resource Location D) Universal Routing Language',
       "b" :'4.What does the acronym "URL" stand for in the context of the internet? \n A) universal resource locator B) Uniform Resource Locator C) Unifying Resource Location D) Universal Routing Language',
    'c':'5.Which of the following is not an operating system? \n A) Windows B) Android C) Adobe Photoshop D) Linux',

    'b':'6.What does CPU cache memory primarily aim to do? \n A) Store user files B) Speed up data access by the CPU C) Display graphical content D) Manage network connections',
    'c':'7.What is the purpose of the BIOS (Basic Input/Output System) in a computer? A) To perform complex mathematical calculations B) To provide the user interface C) To control hardware initialization and booting D) To manage network settings',
 
 'd':'8.Which data storage unit is the largest? A) Kilobyte B) Megabyte C) Gigabyte D) Terabyte',
 "c":'9.In computer security, what does "Phishing" refer to? A) A technique to improve Wi-Fi signal strength B) A type of computer virus C) A social engineering attack to steal personal information D) A method to reduce energy consumption in computers'
        }
# principal_list=[]
# x=0
invigilator=int(input('''welcome principal
            how many student is writing test
            enter an option here: '''))
no_of_question=int(input('''how many question: '''))


students=[]
for each_student in range(1, invigilator+1):
    students.append(list())
for each_student in range(1, invigilator+1):
    Fname=input('enter your first name: ')
    Lname=input("enter your last name:  ")
    registration_No=int(input('enter your registration number: '))
    students[each_student-1].append(Fname)
    students[each_student-1].append(Lname)
    students[each_student-1].append(registration_No)

for pupil in range(1, invigilator+1):
    score=0
    print(f'exam for {students [pupil-1] [0]} {students [pupil-1] [1]}')
    y=1
    for ans, ques in Q_and_A.items():
        if y>no_of_question:
            break
        print(ques)
        student_answer=input('answer: ').strip().capitalize()
        if student_answer==ans.capitalize():
            score+=1
        y+=1
    students[pupil-1].append((score/no_of_question)*100)
print(students)



# print(students)
# principal_list[x]=list((students))
# principal_list.append(list())
# print(principal_list)
        
# x+=1
# print(principal_list)
# registration=input({
#         'student':' ',
#         "reg_no":' '})
# print(reg)

# using dictionary
# invigilator={'question1':'how many student do you want to register','question2':'how many student are you registering'}
# principal=[]
# for ques in invigilator.items():
#     prin

# student_list=[]
# x=0
# principal_list=int(input("enter the number of student you want to register: "))
# for x in range(1,principal_list+1):
#     student_list.append([])
# for x in range(1, principal_list+1):
#     names=input(f"enter the name of student {x} : ")
#     mat_no=int(input(f"enter the mat num of student {x} : "))
#     student_list[x-1].append(names)
#     student_list[x-1].append(mat_no)
#     # print(f"the name of student {x} is {names} \n the mat number of student {x} is {mat_no}")
# for x in range(1,):