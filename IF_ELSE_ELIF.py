# Write a python program to accept and operator from the user and print the message based on the table

ask = input("Enter: ") # Gets an input

if ask == "+":   # Check if input is +, /, or *
    print("Addition")
elif ask == "*":
    print("Multiplication")
elif ask == "/":
    print("Division")
else:
    print("Incorrect Operator")   # if input not equal to the above one

# 24/20/23 TUT

# Exercise 01
ask = int(input("Enter age: "))

if ask >= 18:
    print("Can Vote")

# Exercise 02
read = int(input("Enter mark: "))

if read < 40:
    print("Fail")
else:
    print("Pass")

# Exercise 03
ask = int(input("Enter a number: "))

if ask % 2 == 0:
    print(ask3, "is Even")
elif ask == 0:
    print(ask, "is Zero")
else:
    print(ask, "is Odd")

# Exercise 04
print("Welcome! What would you like to do?")
print("Convert from F to C --> [1]")
print("Convert from C to F --> [2]")
ask = int(input("Enter 1 or 2: "))

print("\b")

if ask == 1:
    f = int(input("Enter Fahrenheit: "))
    c = (f - 32) / 1.8
    print("Temperature in Degree Celsius is:", round(c, 2))
elif ask == 2:
    c = int(input("Enter Celsius: "))
    f = (c * 1.8) + 32
    print("Temperature is Fahrenheit is:", round(f, 2))
else:
    print("Incorrect number")

# Exercise 05
num1 = int(input("Enter a number to compute: "))
num2 = int(input("Enter another number to compute: "))
operator = input("Enter which operator [/, +, *, -]: ")

print("\b")

if operator == "/":
    try:
        print(round(num1 / num2, 2))
    except ZeroDivisionError:
        print("Error!")
elif operator == "*":
    print(num1 * num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "+":
    print(num1 + num2)
else:
    print("Not an Option!")

# Exercise 06
cost = float(input("Enter the cost of the dinner: "))
print("Totally Satisfied [1]")
print("Satisfied [2]")
print("Dissatisfied [3]")
ask = int(input("Enter your satisfaction rate [1][2][3]: "))

print("\b")

if ask == 1:
    print("Bill:", cost * 0.2)
elif ask == 2:
    print("Bill:", cost * 0.15)
elif ask == 3:
    print("Bill:", cost * 0.1)
else:
    print("Not a valid option!")

