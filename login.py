# import
import mysql.connector as sql
my_con=sql.connect(host="127.0.0.1", user="root", passwd='olasunkanmi60@', database='onyxbank_db')
my_cursor=my_con.cursor()

def login(self):
        email=input('enter your email >>>')
        password=input('enter your password >>>')
        query="SELECT email, password FROM customer_table WHERE email=%s AND password=%s"
        val=(email, password)
        my_cursor.execute(query, val)
        login_request=my_cursor.fetchone()
        # print(login_request)
        self.email_in_db = login_request[0]
        # print(self.email_in_db)
        if login_request:
            print('access granted')
            wn.Beep(10000,2)
            self.transaction()
        else:
            print('access denied')
            self.landing_Page()