class PutMoney:
    def __init__(self, account_num, balance=0):
        self.account_num= account_num
        self.balance=balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'deposit of {amount} is successful \n new balance is: {self.balance}')


    def update_bal_in_db():
        update_query="UPDATE account SET balance=? WHERE account_number=?"
        var=(self.balance, self.account_number)
        cursor.execute(update_query, var)


