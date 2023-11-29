# python database (mysal)
# to download mysql connector user: pip install mysql-connector if you use xamp
        # or
# pip install mysql-connector-python #if use are using mysql workbench

# import mysql.connector as sql     #note it not compulsory you use the "as sql" statement but it good to use it to avoid repetition of mysql.connector
# 
# my_con = sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@')  #this connection password must be the password you use to open your database(if the data is in your pc)(if it not inside your pc, the owner of the pc will give you the username of the pc for user and you will use the pc ip address in your host), but in an organization, it is the  admin that will give you  privileges to access the database and he\she will be the one to generate the user and password that will be used. also if the database is hosted on the cloud, you will copy the IP address of the hosting platform into host  NOTE THE VARIABLE NAME OF YOUR CONNECTION SHOULD BE 'mycon or my_con' e.g i used my_connection as variable name but it did not work it throw an error indicating wrong syntax 

# print(my_con) #note you can only run this once to check if you are connected. after checking if you are connected, comment it out

# CREATE A CURSOR WHICH WILL SERVE AS A MESSENGER BETWEEN YOUR PC AND THE DATABASE
# my_cursor = my_con.cursor()

# my_cursor.execute("SHOW DATABASES")
# note: you are only allow to run a created database once else it will throw error that the database  exist (do not run a newly created table twice)
# print(my_cursor)

# for db in my_cursor:
    # print(db)

# after connecting to the database, you will need to create a table
# HOW TO CREATE A TABLE IN THE DATABASE

# my_cursor.execute('CREATE DATABASE bankApp_db') #after creating it, and your table is successful, at the prompt, it will not show anything but if it not successful it will throw error
# my_cursor.execute("SHOW DATABASE")
# for db in my_cursor:
    # print(db)

# after creating the table, you will need to connect to the table created as follow👇
# my_con=sql.connect(host='localhost', user='root',passwd='olasunkanmi60@', database='bankApp_db')
# my_cursor=my_con.cursor()
# my_cursor.execute("CREATE TABLE customers_table (ctm_db INT(4), full_name VARCHAR(40),address VARCHAR(50),password VARCHAR(20))" )
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table)

# my_cursor.execute("ALTER TABLE customers_table CHANGE ctm_db customer_id INT(5)PRIMARY KEY AUTO_INCREMENT")
# my_cursor.execute("ALTER TABLE customers_table ADD UNIQUE(phone);")
# my_cursor.execute("ALTER TABLE customers_table ADD UNIQUE(username);")

my_query="INSERT INTO customers_table (full_name,address,phone,username,password) VALUES(%s,%s,%s,%s,%s)"
val=[("timi adedigba","Apake","09087676545","tboy","1234")]
# my_cursor.execute(my_query,val)
# my_con.commit()
# print(my_cursor.rowcount,"records inserted successfully")
# my_con.close()

# Full_name=input("enter your full name >>>")
# address=input("enter your address >>>")
# Phone_num=input("enter your phone number >>>")
# email=input("enter your email address  >>>")
# password=input("enter your password  >>>")
# username=input("enter your username  >>>")
# next_of_kin=input("enter name of next of kin  >>>")
# next_of_kin_phone_num=input("enter name of next of kin phone number >>>")
# my_query = 'INSERT INTO customers_table (Full_name, Address, Phone_num, email, password, username,next_0f_kin, next_0f_kin_Phon_num) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s )'
#     val= (Full_name, address, Phone_num, email,password, username,next_of_kin, next_of_kin_phone_num)
#     my_cursor.execute(my_query, val)
#     my_con.commit()


# val=[("timi adedigba","Apake","09087676545","tboy","1234"),("rose abas","general","09080636245","rosibaby","2020")]  #note you can pass millions of data here assuming the data you want to work with is collected from a place where there is no network, all you just need to do is to collect the data inside a tuple and append it inside an empty list then you will put everything here and then put it inside the database 
# my_cursor.execute(my_query,val)
# my_con.commit()
# print(my_cursor.rowcount,"records inserted successfully")
# my_con.close()

# query ="SELECT * FROM customers_table"     #this * means 'all'
# my_cursor.execute(query)
# output=my_cursor.fetchall()
# print(output)
# for info in output:
#     print(info)

# output=my_cursor.fetchone()
# print(output)

# query ="SELECT * FROM customers_table WHERE Address=%s" 
# val=('Apake',)
# my_cursor.execute(query, val)
# myreg=my_cursor.fetchall()
# myreg=my_cursor.fetchone()
# print(myreg)

# query ="SELECT * FROM customers_table WHERE full_name LIKE '%Ade%'" 
# my_cursor.execute(query)
# myreg=my_cursor.fetchall()
# print(myreg)

# query ="SELECT full_name, phone FROM customers_table" 
# my_cursor.execute(query)
# myreg=my_cursor.fetchall()
# print(myreg)

# query ="SELECT full_name, phone FROM customers_table WHERE Address=%s"
# val=(apake) 
# my_cursor.execute(query,val)
# myreg=my_cursor.fetchall()
# # myreg=my_cursor.fetchone()
# print(myreg)

# query ="SELECT full_name, phone FROM customers_table WHERE full_name LIKE 'adedigba%s'" 
# my_cursor.execute(query)
# myreg=my_cursor.fetchall()
# print(myreg)

# TO SELECT ALL ON A TABLE
# query ="SELECT * FROM customers_table ORDER BY customer_id DESC" #DESC (you can replace DESC with ASC meaning ascending order) means descending order i.e it should print all the information on the customer-table in descending order of their id number.
# my_cursor.execute(query)
# myreg=my_cursor.fetchall()
# print(myreg)


# TO UPDATE A DATA ON A TABLE IN THE DATA BASE
# sql= "UPDATE customers_table SET username='tade' WHERE username=%s" #TADE IS THE NEW USERNAME I WANT TO CHANGE TO
# # val=("tyt",)   # 'tyt', is the old one on the database that i am changing to
# # my_cursor.execute(sql,val)
# my_con.commit()
# print(my_cursor.rowcount, "record update successfully")

# TO UPDATE MORE THAN ONE FIELDS (phone numbers, password etc) using a unique details or most prefer is a primary key note: you must indicate the username you want to change in a variable name so you wont go and change all the username that users have input inside the database. 
# sql= "UPDATE customers_table SET password='2020', phone='09078765654' WHERE username=%s"
# val=("tyt",)
# my_cursor.execute(sql,val)
# my_con.commit()
# print(my_cursor.rowcount, "record update successfully")

# HOW TO DELETE FROM THE DATA BASE
# sql= "DELETE FROM customers_table  WHERE username=%s"
# val=("tyt",)
# my_cursor.execute(sql,val)
#  my_con.commit()
#  print(my_cursor.rowcount, "record deleted successfully")

# HOW TO DELETE A TABLE FROM THE DATA BASE
# sql= "DROP DATABASE  bankapp_db"
# my_cursor.execute(sql) # deleted


# TO CHECK IF A  LOGIN DETAILS IS CORRECT
# user = input("enter your username >>>")
# password=input('enter your  password >>>')
# query="SELECT username, password FROM customers_table WHERE username=% AND password"
# val=(user, password)
# my_cursor.execute(query, val)
# myreg= my_cursor.fetchone()
# if myreg: #can also be written as 'if myreg True:'
    # print("access granted")
# else:
#     print("access denied")


# THIS SECTION IS ON RESET PASSWORD i.e USER CAN CHANGE THEIR PASS WORD BY PROVIDING THE OLD ONE THEY USED
# user = input("enter old username >> ")
# new_username=input("enter new username >>>")
# pin= input("enter old password >>")
# new_pin=input("enter new pin >>>")
# sql= f"UPDATE  customers_table SET username=%s password=%s WHERE username={new_username}AND password={new_pin}"
# val=(user, new_username, pin, new_pin)
# my_cursor.execute(sql, val)
# my_con.commit()
# print(my_cursor.rowcount, "record update successfully")

    
# TO CHANGE PASSWORD IN A CASE WHERE THE USER CANNOT REMEMBER HIS\HER PASSWORD (FORGOT PASSWORD)
# user = input("enter your username >>>")
# password=input('enter your new password >>>')
# sql= "UPDATE customers_table SET password=%s WHERE username=%s"
# val=(password, user)
# my_cursor.execute(sql,val)
# my_con.commit()
# print(my_cursor.rowcount,'record updated successfully')




































