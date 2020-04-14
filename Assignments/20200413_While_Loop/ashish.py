# Assignment : 1 while loop for a given number print the square & cube

decimal = int(input("Enter a number to derive SQUARE and CUBE  : "))
count = 2
while count != 0:
    count -= 1
    if count == 1:
        print("SQUARE of DECIMAL {0} is {1}".format(decimal, decimal**2))
    else:
        print("CUBE of DECIMAL {0} is {1}".format(decimal, decimal**3))



# Assignment : while loop for a given number add 3 for 7 times
decimal = int(input("Enter a number to add 3 for 7 times  : "))
output = 0
count = 0
while count < 7:
    if count == 0:
        output = decimal
    output += 3
    count += 1
print("Seven times of DECIMAL {0} is {1}".format(decimal, output))

