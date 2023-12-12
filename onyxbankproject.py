import time 
import datetime as dt
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
# sql= "UPDATE customer_table SET account_bal='0.00'"
# val=("tyt",)
# my_cursor.execute(sql)
# my_con.commit()
# print(my_cursor.rowcount, "record update successfully")


class bank:
    total_withdrawal=0
    total_deposit=0
    balance=0


    def __init__(self):
        # self.all_account_num=[]
        self.name="OnyxBank plc"
        self.location="oyo state"
        self.founder="Adeniran Bukunmi"
        self.year= "2023"

        self.landing_Page()

    def landing_Page(self):
        print(f""" welcome to {self.name} 
            1.Open account 
            2.login 
            3.forget password
            4.exit """)
        user=int(input("select an option >>>"))
        if user==1:
            time.sleep(2)
            print("fill the form below".center(100))
            self.sign_Up()
        elif user==2:
            time.sleep(2)
            print("LOGIN".center(150,'-'))
            self.login()
        elif user == 3:
            self.forget_password()
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

            
    def deposit_into_acct(self):
        query="SELECT account_bal FROM  customer_table WHERE email=%s"
        var = (self.email_in_db, )
        my_cursor.execute(query, var)
        balance = my_cursor.fetchone()
        balance = float(balance[0]) 
        print(balance)
        
        amount=float(input("enter the amount you would like to deposit >>> "))
        new_balance = balance + amount

        sql="UPDATE customer_table SET account_bal=%s WHERE email=%s"
        var=( new_balance, self.email_in_db)
        my_cursor.execute(sql,var)
        my_con.commit()

        print (f"your account balance has been credited with {amount} \n your new balance is: ", (round(new_balance, 2)) )

        self.transaction()


    def withdraw_from_acct(self):
        query="SELECT account_bal FROM  customer_table WHERE email=%s"
        var = (self.email_in_db, )
        my_cursor.execute(query, var)
        balance = my_cursor.fetchone()
        balance = float(balance[0])
        print(balance)
        withdraw=float(input("enter the amount you would like to withdraw >>> "))
        self.balance_after_withdraw = balance - withdraw

        sql="UPDATE customer_table SET account_bal=%s WHERE email=%s"
        var=( self.balance_after_withdraw, self.email_in_db)
        my_cursor.execute(sql,var)
        my_con.commit()
        print (f"your account balance has been debited with {withdraw} \n your new balance is: ",(round(self.balance_after_withdraw, 2)) )
        self.transaction()

    def check_bal(self):
        detail=[]
        query= "SELECT fname, lname, account_number, account_bal FROM customer_table WHERE email=%s "
        var = (self.email_in_db,)
        my_cursor.execute(query, var)
        for all in my_cursor:
            detail.append(all)
        print(all)
        # current_time=dt.datetime.now()
        # content=(f'fname', 'lname', 'account_number', 'account balance')
        # history = my_cursor.fetchall()

        # converted_history=list(history)
        my_con.commit()
        # print(f'date>>>{current_time}')
        # for all in converted_history:
        #     for each in content:
        #         print(f'{each}>>>{all}')
                
        # self.check_bal()

    def forget_password(self):
        email=input("enter your email >>>")
        pin= input("enter old password >>")
        new_pin=input("enter new pin >>>")
        sql= "UPDATE  customer_table SET password=%s WHERE email=%s AND password=%s"
        val=(new_pin, email, pin)
        my_cursor.execute(sql, val)
        my_con.commit()
        print(my_cursor.rowcount, "password successfully changed")

    def transaction(self):
        print(" onyxBank plc \n 1.check account balance \n 2.deposit \n 3.withdraw \n 4.buy airtime \n 5.exit".center(150))
        user=int(input("select an option >>>"))
        if user ==1:
            self.check_bal()
        elif user ==2:
            self.deposit_into_acct()
        elif user ==3:
            self.withdraw_from_acct()
        elif user ==4:
            pass
        elif user ==5:
            pass






onyx=bank()