class BankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"\nAmount ₹{amount} deposited successfully.")
        self.display_account_details()

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"\nAmount ₹{amount} withdrawn successfully.")
            self.display_account_details()
        else:
            print("\nInsufficient balance.")

    def display_account_details(self):
        print("\nAccount Details:")
        print(f"Account number : {self.account_number}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance: ₹{self.balance}")

#Creating an instance of the BankAccount
account=BankAccount("XXXXXXXX","SRI")

#deposit money
account.deposit(10000)

account.withdraw(4000)
