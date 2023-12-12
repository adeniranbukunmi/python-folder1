import mysql.connector as sql
# my_con= sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@')
# my_cursor.execute("CREATE DATABASE precious_db")
my_con= sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@', db='precious_db')
my_cursor=my_con.cursor()
# my_cursor.execute('CREATE TABLE customer_table (ctm_id INT(4) UNIQUE AUTO_INCREMENT, fname VARCHAR(40), lname VARCHAR(40), password VARCHAR(20))')
# my_cursor.execute("ALTER TABLE customer_table ADD email VARCHAR(50) ")
# my_cursor.execute("ALTER TABLE customer_table CHANGE ctm_id customer_id INT(5) ")
# my_cursor.execute("ALTER TABLE customer_table CHANGE  customer_id ctm_id INT(4) UNIQUE AUTO_INCREMENT ")


# fname=input("enter your fname >>>")
# lname=input("enter your lname >>>")
# password=input("enter your password >>>")
# email=input("enter your email address  >>>")

# password=input("enter your password  >>>")
# username=input("enter your username  >>>")

# my_query="INSERT INTO customer_table (fname,lname,password ,email) VALUES(%s,%s,%s,%s)"
# my_reg=(fname, lname,password, email)
# my_cursor.execute(my_query,my_reg)
# my_con.commit()
# print(my_cursor.rowcount,"records inserted successfully")

# query ="SELECT * FROM customer_table ORDER BY ctm_id ASC"
# my_cursor.execute(query)
# my_reg=my_cursor.fetchall()
# for each in my_reg:
#     print(each)

# user = input("enter old username >> ")

email=input("enter your email >>>")
pin= input("enter old password >>")
new_pin=input("enter new pin >>>")
sql= "UPDATE  customer_table SET password=%s WHERE email=%s AND password=%s"
val=(new_pin, email, pin)
my_cursor.execute(sql, val)
my_con.commit()
print(my_cursor.rowcount, "password successfully changed")