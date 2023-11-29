import time
import winsound as wn
import random
import mysql.connector as sql
my_con=sql.connect(host="127.0.0.1", user="root", passwd='olasunkanmi60@', database='onyxbank_db')
my_cursor=my_con.cursor()
# my_cursor.execute("CREATE DATABASE onyxbank_db")
# my_cursor.execute("CREATE TABLE customer_table (customer_id INT(5) PRIMARY KEY AUTO_INCREMENT, fname VARCHAR(20), lname VARCHAR(20), email VARCHAR(50) UNIQUE, password VARCHAR(30), phone_num INT(11),  account_number INT(10) )")
# my_cursor.execute("ALTER TABLE customer_table MODIFY account_number VARCHAR (10)")
# my_cursor.execute("ALTER TABLE customer_table MODIFY account_number VARCHAR (10)")
# my_cursor.execute("ALTER TABLE customer_table ADD account_bal VARCHAR (10)")

class bank:
    def __init__(self):
        # self.all_account_num=[]
        self.name="onyx plc"
        self.location="oyo state"
        self.founder="Adeniran Bukunmi"
        self.year= "2023"
        
        
        
        self.landing_Page()

    def landing_Page(self):
        print(""" welcome to ONYX bank 
            1.Open account 
            2.login 
            3.exit """)
        user=int(input("select an option >>>"))
        if user==1:
            time.sleep(2)
            print("fill the form below".center(100))
            self.sign_Up()
        elif user==2:
            time.sleep(2)
            print("LOGIN".center(50,'-'))
            self.login()
        else:
            exit()
        
    def sign_Up(self):
        # customerDetails=[]
        
        fname=input("enter your first name >>> ")
        lname= input("enter your Lname name >>> ")
        email= input("enter email address >>> ")
        Password= input("enter password >>>")
        phone_num=int(input("enter a valid phone number >>> "))
        
        # info=[fname, lname, email, Password,  phone_num]
        # customerDetails.append(info)
        account_num = self.generate_account()
        account_bal= 0
        my_query="INSERT INTO customer_table (fname, lname, email, password, phone_num, account_number, account_bal ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val=(fname, lname, email, Password, phone_num, account_num, account_bal)
        my_cursor.execute(my_query, val)
        my_con.commit()

        print(f"dear {fname} {lname}, your account number is {account_num} \n you ")

    
    def generate_account(self):
        acct = '20' + str(random.randint(10000000, 99999999))
        return acct
        # account_num=['2','0']
        # for i in range(10-len(account_num)):
        #     account_num.append(str(random.randint(0,9)))
        # account="".join(account_num)
        # if account  in self.all_account_num:
        #     self.generate_account()
        # else:
            # return account
        
    def login(self):
        email=input('enter your email >>>')
        password=input('enter your password >>>')

        query="SELECT email, password FROM customer_table WHERE email=%s AND password=%s"
        val=(email, password)
        my_cursor.execute(query, val)
        login_request=my_cursor.fetchone()
        if login_request:
            print('access granted')
            wn.Beep(10000,2)
        else:
            print('access denied')
            self.landing_Page()

            
    def account_balance():
        account_bal=0
        deposit_amount=int(input("enter the amount you want to deposit >>>"))
        account_bal += deposit_amount
        print(account_bal)


onyx=bank()