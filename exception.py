# try:
#     num=int(input())
#     print(10/num)

# except:
#     print("error")

# except Exception as e:
#     print("Error Occured:",e)

# except ValueError:
#     print("error")

# except ZeroDivisionError:
#     print("error")

# else:
#     print("success")

# finally:
#     print("pogram finished")

# print("we handled error")

class Pranav(Exception):
    pass

age=int(input("Enter: age: "))

if age < 18:
    raise Pranav("Not eligible")#raise our own error
