# num1 = 5
# num2 = '7'

# print(type(num1))
# print(type(num2))

# budget = 200
# expenses = "180"
# savings = budget - expenses


# data type conversion არსებობს 2 სახის:
# 1. implicit - ბუნებრივი
# 2. explicit - ხელით (int, float, str)

# print(10 / 2)

# print("Your balance is " + str(5 + 3))

# data that comes from input is alway string
# input-იდან მიღებული ინფორმაცია რიცხვიც რომ 
# ჩაწეროს მომხარებელმა იქნება სტრინგირგი

# item_quantity = int(input("Enter amount: "))
# item_price = 6
# total_price = item_quantity * 6
# print("Total bill: " + str(total_price))

# num1 = input()
# num2 = input()
# operation = input()

# quantity = int(input("quantity: "))
# price = int(input("price: "))

# total = quantity * price
# print("Total " + str(quantity * price))

# print(3 > 2) # True False

# or - ან
# and - და

# or operator
# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)

# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)

# cost_per_acre = 50
# total_land = 300

# offer = ((cost_per_acre * total_land)) < 20000 and total_land >= 100

# print(offer)

# grade = int(input("Score: "))

# პირობითი განცხადება იწერება შემდეგი ნაბიჯებით:
# 1. if
# 2. პირობა
# 3. :
# 4. კოდის ბლოკი
num1 = float(input("Enter first number: "))
operation = input("Pick operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    print(num1 + num2)

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")

# print("Task complete")