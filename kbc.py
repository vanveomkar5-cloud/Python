questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", "None", 4],

    ["Who created Python?", "Guido van Rossum", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup", "None", 1],

    ["Which company developed Windows?", "Apple", "Google", "Microsoft", "IBM", "None", 3],

    ["What does CPU stand for?", "Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Control Processing Unit", "None", 1],

    ["Which keyword is used to define a function in Python?", "func", "define", "def", "function", "None", 3],

    ["Which data type is used to store text in Python?", "int", "float", "str", "list", "None", 3],

    ["What is the output of 5 + 3 * 2?", "16", "11", "10", "13", "None", 2],

    ["Which symbol is used for comments in Python?", "//", "#", "/* */", "--", "None", 2],

    ["Which loop is used when the number of iterations is known?", "while", "for", "do-while", "if", "None", 2],

    ["Which operator is used for exponentiation in Python?", "^", "*", "//", "**", "None", 4]
]

levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

money = 0

for  i in range(0, len(questions)):
    question = questions[i]

    print(f"\n\n{i+1}.Question for ₹ {levels[i]}\n")
    print("Question: ",question[0],"\n")
    print(f"1.{question[1]}\n2.{question[2]}\n3.{question[3]}\n4.{question[4]}\n5.{question[5]}")

    reply = int(input("\nEnter Option Number: "))

    if reply == question[-1]:
        print(f"Correct Answer🎉, You Won ₹ {levels[i]}")

        if i == 2:
            money=2000
            print(f"You have Won Money 🎉, Which is ₹ {money}")
        elif i==4:
            money=4000
            print(f"You have Won Money 🎉, Which is ₹ {money}")
        elif i==6:
            money=6000
            print(f"You have Won Money 🎉, Which is ₹ {money}")
        elif i==8:
            money=8000
            print(f"You have Won Money 🎉, Which is ₹ {money}")
        elif i==9:
            money=10000
            print(f"You have Won Money 🎉, Which is ₹ {money}")

    else:
        print("Wrong Answer! You Lose👎")
        break
