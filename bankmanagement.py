class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))
        self.accounts[acc] = {"name": name, "balance": balance}
        print("✅ Account Created Successfully!")

    def deposit(self):
        acc = input("Enter Account Number: ")
        if acc in self.accounts:
            amount = float(input("Enter Amount to Deposit: "))
            self.accounts[acc]["balance"] += amount
            print("✅ Amount Deposited Successfully!")
        else:
            print("❌ Account Not Found!")

    def withdraw(self):
        acc = input("Enter Account Number: ")
        if acc in self.accounts:
            amount = float(input("Enter Amount to Withdraw: "))
            if self.accounts[acc]["balance"] >= amount:
                self.accounts[acc]["balance"] -= amount
                print("✅ Withdrawal Successful!")
            else:
                print("❌ Insufficient Balance!")
        else:
            print("❌ Account Not Found!")

    def check_balance(self):
        acc = input("Enter Account Number: ")
        if acc in self.accounts:
            print("\n----- Account Details -----")
            print("Name:", self.accounts[acc]["name"])
            print("Balance:", self.accounts[acc]["balance"])
        else:
            print("❌ Account Not Found!")

bank = Bank()

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        print("Thank You for Using Bank Management System!")
        break
    else:
        print("❌ Invalid Choice!")