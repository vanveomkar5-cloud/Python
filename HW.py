# Pattern Printing

# t = 1# firts No.
# for i in range(1,5):# row
#     for j in range(1, i+1):# cloumn, decides how many numbers go in each row.
#         print(t,end=" ")# python add new line after print statement, so it cancle new line and add space, so now new line cancle so next value come up
#         t+=1# increases value of t
#     print()#start new row after inner loop complete mean after completeing each line


# Calculater

# def sum(a,b):
#     return "=",a+b

# def sub(a,b):
#     return "=",a-b

# def mul(a,b):
#     return "=",a*b

# def div(a,b):
#     if b == 0:
#         print("Can't Divide By Zero.")
#     return "=",a/b

# while True:
#     print()
#     print("+ => Addition")
#     print("- => Subtraction")
#     print("* => Multiplication")
#     print("/ => Division")
#     # a=int(input("Enter No.: "))
#     # op=input("Enter Operator: ")
#     # b=int(input("Enter No.: "))

#     a,op,b=input().split()
#     a=int(a)
#     b=int(b)

#     match op:
#         case '+':
#             print(sum(a,b))
#         case '-':
#             print(sub(a,b))
#         case '*':
#             print(mul(a,b))
#         case '/':
#             print(div(a,b))


#1: functions of list , tuple , dict 
#2: write meaningful code using all these fun
products = [
    ("SmartPhone", "iPhone-16pro", 70000, "Apple"),
    ("SmartPhone", "S26-Ultra", 120000, "Samsung"),
    ("HeadPhone", "Rockerz411", 2000, "boAt"),
    ("Mouse", "M612-RGB", 1000, "REDRAGON"),
]

# show products
print(f"{'Sr':^5}|{'Category':<14}|{'Name':<16}|{'Price':<10}|{'Brand'}")
print("-"*60)

for i, (category, name, price, brand) in enumerate(products, start=1):
    print(f"{i:<5}|{category:<14}|{name:<16}|₹{price:<10}|{brand}")

cart = {}

# input loop
while True:
    choose = input("\nEnter Item Sr No. or type 'na': ")

    if choose.lower() == "na":
        break

    choose = int(choose) #convert string to integer
    
    if choose < 1 or choose > 4:
        print("Invalid Input!")
        continue

    qty = int(input("Enter Quantity: "))

    product = products[choose -1] #seperate each tuple"()"

    if product[1] in cart: # if in cart
        cart[product[1]] += qty
        print(cart) #if phone already exist, add again because user want 2 phone
    else:
        cart[product[1]] = qty
        print(cart) #else add in cart


# bill function
def generate_bill(cart):
    total = 0

    print("\n------ BILL ------")

    for item_name, qty in cart.items(): #get item info from cart: name,qty

        for category, name, price, brand in products: #get item info from products: category, name, price, brand
            if name == item_name:

                amount = price * qty
                print(f"{name} x {qty} = ₹{amount}")

                total += amount #total is 0, then amount store, then loop run again and new value add in total

    print("------------------")
    print("Total = ₹", total)

generate_bill(cart)
