start = input("do you want to calculate your total expense: ")
total = 0

while start.lower() == "y":
    try:
        expense = int(input("please enter your amount: "))
        if expense <0:
            print("you can not enter a negative value")
            # break
    except ValueError:
        print("Invalid data please enter a valid data")

    else:
        total= total+ expense
    start=input("do you want to enter another amount: ")

print("your total amount is: ", total)