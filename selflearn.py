import mysql.connector as sql
# my_con=sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@')
# print(my_con)
# my_cursor=my_con.cursor()
# print(my_cursor)
# my_cursor.execute('CREATE DATABASE learning_db')

my_con=sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@',db='learning_db')
my_cursor=my_con.cursor()
# my_cursor.execute('CREATE TABLE transaction_table (customer_id INT(5) UNIQUE AUTO_INCREMENT, fname VARCHAR(40), lastname VARCHAR(40), email VARCHAR(50) UNIQUE)')
# my_cursor.execute('CREATE TABLE history_table (customer_id INT(5) UNIQUE AUTO_INCREMENT, price VARCHAR(40), amount_sold VARCHAR(40), cost VARCHAR(50) )')
sql='SHOW TABLE'
my_cursor.execute(sql)
# for tb in sql:
    # print(tb)