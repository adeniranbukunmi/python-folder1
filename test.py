z=1
Q_and_A=  {'c':'1.What is the primary function of the Central Processing Unit (CPU) ina computer?  \n A) Storage of dat B) Display of graphics C) Execution of                   instructions D) Network connectivity',
    'c':'2.Which programming language is known for its use in web development and can be executed in a web browser?\n A) PythonB) Java C) HTML D) C++',
    "a":"What does RAM stand for in computer terms?\n A) Random Access Memory B) Read-Only Memory C) Real-time Algorithm Machine D) Remote Access Method",

    'c':'3.What does the acronym "URL" stand for in the context of the internet?\n A) Universal  Resource Locator  B) Uniform Resource Locator C) Unifying Resource Location D) Universal Routing Language',
    "b" :'4.What does the acronym "URL" stand for in the context of the internet? \n A) universal resource locator B) Uniform Resource Locator C) Unifying Resource Location D) Universal Routing Language',
    'c':'5.Which of the following is not an operating system? \n A) Windows B) Android C) Adobe Photoshop D) Linux',
   
    'b':'6.What does CPU cache memory primarily aim to do? \n A) Store user files B) Speed up data access by the CPU C) Display graphical content D) Manage network connections',
    'c':'7.What is the purpose of the BIOS (Basic Input/Output System) in a computer? A) To perform complex mathematical calculations B) To provide the user interface C) To control hardware initialization and booting D) To manage network settings',
 
    'd':'8.Which data storage unit is the largest? A) Kilobyte B) Megabyte C) Gigabyte D) Terabyte',
    "c":'9.In computer security, what does "Phishing" refer to? A) A technique to improve Wi-Fi signal strength B) A type of computer virus C) A social engineering attack to steal personal information D) A method to reduce energy consumption in computers'
    
}
z+=1

score=0
x=1
for ans, question in Q_and_A.items():
    print(f'{x}. {question} \n')
    user=input('enter your answer: ')
    if user.strip().upper() == ans:
        score+=10
    x+=1
