import mysql.connector as sql
# my_con = sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@')
# print(my_con) 
# my_cursor=my_con.cursor()
# my_cursor.execute("SHOW DATABASES")
# print(my_cursor)
# my_cursor.execute('CREATE DATABASE transaction_db')
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
    # print(db)
my_con = sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@',   database='transaction_db')
my_cursor=my_con.cursor()
# my_cursor.execute("CREATE TABLE customer_table (ctm_id INT(4), Full_name VARCHAR(40), Address VARCHAR(50), Phone_num VARCHAR(11))")
# my_cursor.execute("SHOW DATABASES")
# print(my_cursor)
# my_cursor.execute("ALTER TABLE customers_table CHANGE ctm_id customer_id INT(3) PRIMARY KEY AUTO_INCREMENT;")
# my_cursor.execute("ALTER TABLE customers_table ADD UNIQUE(phone_num);")
# my_cursor.execute("ALTER TABLE customers_table ADD UNIQUE(phone);")
# my_cursor.execute("SHOW DATABASES")
# print(my_cursor)
sql="DROP DATABASE transaction_db"
my_cursor.execute(sql)



    

