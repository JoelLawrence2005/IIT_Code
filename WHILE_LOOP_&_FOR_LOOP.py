# FOR LOOP

# Example 01
print(*range(5)) # Prints all the numbers from 0 to 4, the * in this is called a "Unpacking Operator"
print(*range(5, 20, 3))  # The numbers inside the brackets are called "Arguments"
                         # the first argument gives the starting value
                         # second argument gives the stopping value
                         # third argument gives the step value, basically by how much the sequence should change

# Example 02
for i in range(3): # Goes through the loop thrice, to print the string "Hello" thrice
  print("Hello")

# Example 03
for i in range(2):    # Goes through loop 1, at the start i = 0
  for j in range(4):  # Goes through loop 2, i = 0 and j = 0
    print(i, j)       # Prints (i, j) = 0 0, this repeats until the first loop is finished

# WHILE LOOP

#Example 01
i = 0
while i <= 10:
  print("hello")
  i += 1

# Example 02
while True:
  print("Yes")

# Example 03
count = 0
while True:
  if count < 10:
    continue
  print(count)
