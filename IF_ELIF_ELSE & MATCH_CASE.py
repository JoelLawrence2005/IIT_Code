# Write a python program to accept and operator from the user and print the message based on the table

ask = input("Enter: ")

if ask == "+":
    print("Addition")
elif ask == "*":
    print("Multiplication")
elif ask == "/":
    print("Division")
else:
    pass

# -----------------------------
# 24/20/23 TUT

# Exercise 01
ask2 = int(input("Enter age: "))

if ask2 >= 18:
    print("Can Vote")

# Exercise 02
read = int(input("Enter mark: "))

if read < 40:
    print("Fail")
else:
    print("Pass")
