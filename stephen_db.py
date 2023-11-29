# import mysql.connector as sql
# my_con = sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@')
# my_cursor=my_con.cursor()
# my_cursor.execute("CREATE DATABASE transaction_db")
# my_con = sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@', database="transaction_db")
# my_cursor= my_con.cursor()
# my_cursor.execute("CREATE TABLE customers_table (ctm_id INT(3), Full_name VARCHAR(50), Address VARCHAR(100),Phone_num INT(11))")
# my_cursor.execute("ALTER TABLE customers_table CHANGE ctm_id customer_id INT(4) PRIMARY KEY AUTO_INCREMENT;")
# my_cursor.execute("ALTER TABLE customers_table ADD email VARCHAR(20) UNIQUE")
# my_cursor.execute("ALTER TABLE customers_table ADD password VARCHAR(20)")
# my_cursor.execute("ALTER TABLE customers_table ADD username VARCHAR(50)")
# my_cursor.execute("ALTER TABLE customers_table ADD next_0f_kin VARCHAR(50)")
# my_cursor.execute("ALTER TABLE customers_table ADD next_0f_kin_Phon_num VARCHAR(50)")


# def registration():
#     Full_name=input("enter your full name >>>")
#     address=input("enter your address >>>")
#     Phone_num=input("enter your phone number >>>")
#     email=input("enter your email address  >>>")
#     password=input("enter your password  >>>")
#     username=input("enter your username  >>>")
#     next_of_kin=input("enter name of next of kin  >>>")
#     next_of_kin_phone_num=input("enter name of next of kin phone number >>>")

    my_query = 'INSERT INTO customers_table (Full_name, Address, Phone_num, email, password, username,next_0f_kin, next_0f_kin_Phon_num) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s )'
#     val= (Full_name, address, Phone_num, email,password, username,next_of_kin, next_of_kin_phone_num)
#     my_cursor.execute(my_query, val)
#     my_con.commit()

#     print(my_cursor.rowcount,"records inserted successfully")

# x = 0
# while True:
#     print('I am happy')
#     if x == 10:
#         break
#     x +=1

# def landing_page():
#     print('1. register\n2. Login')
#     user = input('option: ')
#     if user == '1':
#         registration()
#     elif user == '2':
#         print('login'.center(50,'_'))
#     else:
#         print('Invalid  Input')
#         landing_page()

# landing_page()
