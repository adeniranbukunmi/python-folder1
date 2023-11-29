# FILE HANDLING
# myfile = open("filename", mode='r', 'a', 'w', 'x', encoding='t', 'b')
# "r" read only and it is the default for open function. Raise error if file does not exist
# 'a' append new content to an existing file. Create new file with the specified name if file does not exist.
# 'w' Open file for writing. Create new file with the specified name  if  file does not exist
# 'x' To create new file. Raise error if file already exist

# myfile.close()

# with open ("filename", mode="rt") as myfile: #the filename is the name of the file you want to openz

# myfile = open("C:\\Users\\Lenovo\\Desktop\\MY letter of proficiency 3.pdf", 'rb') #note this will open but it will open it in byte and you will not be able to read what it displays. in  order to read it, you will install a pdf reader for python and import it before you can read it. go to chrome and type how to open a pdf file in python
# print(myfile.read())
# print(myfile.read(20)) #read the first 20 character
# print(myfile.readline())
# for i in range (20):
#     print(myfile.readline())

#     for text in myfile:
#         print(text)
#     myfile.close()

# using with open function
with open("note.txt", mode="rt") as myfile: #with open is use to open a file that is accessible inside the folder you are working with eg note.txt is inside python-works2 folder
    print(myfile.read())

# myfile= open("infile2.txt", 'rt') 
# print(myfile.read())
# myfile.close()
# 
# myfile= open("infile2.txt", 'a')
# myfile.write("\n this is to append a new content to the file")
# print("text appended successfully")
# myfile.close()

# content=[]
# we can also say
# myfile= open("infile2.txt", 'rt')
# content.append(myfile.read())
# print(content[0].split('\n))
# print(myfile.read())
# myfile.close()

# content=""
# myfile = open("infile2.txt", 'rt')
# content += myfile.read()
# myfile.close()
# content = content.replace("this is to append a new content to the file", "")
# # myfile= open("infile2.txt", 'rt')
# myfile= open("infile2.txt", 'wt')
# myfile.write(content)
# print(content)
# myfile = open("infile.txt", 'w')
# myfile.write("this is a new python class")
# print(myfile.read())
# myfile.close()

# myfile = open("infile.txt", 'w')
# user_statement=input("enter your statement: ")
# myfile.write(user_statement                                            )



# myfile= open("infile.txt", 'w')
# # print(myfile.read())
# myfile.write('this is a weekend class')
# myfile.close()

# myfile= open("infile.txt", 'rt')
# print(myfile.read())
# myfile.close()

# myfile =open("infile3.txt", "xt")
# print("file created successfully")

