balance = 0

while True:
    print("Welcome to ATM!")
    operation = input("1 - Deposit\n2 - Withdraw\n3 - Balance \n4 - Exit\nPick operation: ")
    
    if operation == "1":
        amount = int(input("Enter deposit amount: "))
        if amount <= 0:
            print("Please enter valid amount next time")
        else:
            balance += amount
    elif operation == "2":
        amount = int(input("Enter deposit amount: "))
        if amount > balance:
            print("Not enough balance")
        else:
            balance -= amount
    elif operation == "3":
        print("Your balance: " + str(balance))
    elif operation == "4":
        print("Have a nice day!")
        break
    else:
        print("Invalid operation, please try again")
