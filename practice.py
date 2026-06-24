# age = int(input("Enter Age: "))

# try:
#     if age > 18:
#         print("Adult")
#     else:
#         print("Minor")
# except:
#     print("Error!")


# Question 1 — Age Validator
# class NegativeAgeError(Exception):
#     pass

# age = int(input("Enter Age: "))

# if age != age:
#     print("Invalid input")
# elif age <= 0:
#     raise NegativeAgeError("Age cannot be negative")
# elif age >= 18:
#     print("Adult")
# else:
#     print("Minor")


# Question 2 — ATM Withdrawal
class InsufficientBalanceError(Exception):
    pass


initial_balance = 10000
print(f"Initial Balance: {initial_balance}")
print("\n1.Diposite Amount")
print("2.Withdrawal Amount")

option = int(input("\nEnter Option Number: "))

if option == 1:
    amount = int(input("Enter Amount: "))
    initial_balance += amount
    print(f"Initial Balance: {initial_balance}")
elif option == 2:
    amount = int(input("Enter Amount: "))
    initial_balance -= amount
    print(f"Remaining Balance: {initial_balance}")

    if amount > initial_balance:
        raise InsufficientBalanceError("Not enough balance")
else:
    print("Invalid Input!")