class account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
    def debit(self, amount):
        self.balance += amount
        print(f"{self.account_no} debited: {amount}\ntotal balance: {self.balance}")
    def credit(self, amount):
        self.balance -= amount
        print(f"{self.account_no} credited: {amount}\ntotal balance: {self.balance}")

acc = input("enter account no: ")
balance = float(input("enter balance: "))
acc1 = account(acc, balance)
while True:
    choice = input("enter debit or credit or exit: ").lower()
    if choice == "debit":
        money = float(input("enter money: "))
        acc1.debit(money)
    elif choice == "credit":
        money = float(input("enter money: "))
        acc1.credit(money)
    elif choice == "exit":
        print("Thank you for using Bank Account")
        break