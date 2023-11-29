import mysql.connector as sql
# my_con=sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@')
# my_cursor=my_con.cursor()
# my_cursor.execute("CREATE DATABASE studentRecord_db")
my_con=sql.connect(host='127.0.0.1', user='root', passwd='olasunkanmi60@',database='studentRecord_db')
my_cursor=my_con.cursor()
# my_cursor.execute("CREATE TABLE examination_result (student_id INT(5) PRIMARY KEY AUTO_INCREMENT, full_name VARCHAR(50) UNIQUE, level VARCHAR(4), department VARCHAR (50), score INT(2) )")
# my_cursor.execute("CREATE TABLE  student_position (std_id INT(5) PRIMARY KEY AUTO_INCREMENT, full_name VARCHAR (50), score INT(2), position VARCHAR(40))")
# my_query='INSERT INTO examination_result (full_name, level, department, score) VALUES (%s, %s, %s, %s)' #two or more table can be in a single database

# full_name=input('enter your first name >>>').upper()
# level=input('enter your level >>>')
# department=input('enter your department >>>')
# score=input('what did you score >>>')
# val =(full_name, level, department, score)
# my_cursor.execute(my_query,val)
# my_con.commit()

# def login():
#     student=input('enter your full name >>>').upper()
#     result=input('what did you score >>>')

#     query="SELECT full_name, score FROM examination_result WHERE full_name=%s AND score=%s"
#     val=(student, result)
#     my_cursor.execute(query, val)
#     student_pass=my_cursor.fetchone()
#     if student_pass:
#         print('access granted')
#     else:
#         print('access denied')
#         login()
# login()

