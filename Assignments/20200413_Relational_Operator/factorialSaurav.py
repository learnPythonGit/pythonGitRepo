# ....................................
# Python Assignment                 :
# Date      : 15/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Factorial of a number :
# Git Branch: D15042020saurav       :
# ...................................

# Write a Python Program to Find the Factorial of a Number (using relational operators and while/for loop)

#Finding factorial using While Loop
number = int(input("Please enter a number for finding it's factorial"))
x = number-1

while x:
    fact = number * x
    number = fact
    x = x-1
print("Factorial of number is {0}".format(fact))


# Finding factorial using For Loop
number = int(input("Please enter a number for finding it's factorial"))
x = number-1

for i in range(number):
    fact = number * x
    number = fact
    x = x-1
    if x == 0:
        break

print("Factorial of number is {0}".format(fact))


