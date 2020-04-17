# Assignment : For a given number get octal, binary, hex
print("\n" + "-"*80)
print("Assignment : for a given number get octal, binary, hex")
decimal = int(input("Enter number to get OCTAL, HEX & BINARY  : "))
print("OCTAL value of DECIMAL {0} is {1}".format(decimal, oct(decimal)))
print("HEX value of DECIMAL {0} is {1}".format(decimal, hex(decimal)))
print("BINARY value of DECIMAL {0} is {1}".format(decimal, bin(decimal)))



# Assignment : Convert temperature from celcius to farenheit
print("\n" + "-"*80)
print("Assignment : Convert temperature from celcius to farenheit")
temp_in_celsius = float(input("Enter temperature in CELSIUS to convert to FARENHEIT  : "))
temp_in_farenheit = ((9/5)*temp_in_celsius) + 32
print("Temperature in FARENHEIT is {0:0.2f}F.".format(temp_in_farenheit))



# Assignment : Write a Python Program to Find the Factorial of a Number (using relational operators and while/for loop)
print("\n" + "-"*80)
print("Assignment : Write a Python Program to Find the Factorial of a Number (using relational operators and while/for loop)")
number_one = int(input("Enter number for finding factorial :  "))
# Using WHILE loop
number_factorial = number_one
index = 1
while index < number_one:
    number_factorial *= index        
    index += 1
print("Factorial of the given number {0} is {1} using WHILE loop".format(number_one, number_factorial))
# Using FOR loop
number_factorial = number_one
index = 0
for index in range(1, number_one):
    number_factorial *= index
print("Factorial of the given number {0} is {1} using FOR loop".format(number_one, number_factorial))    



# Assignment : Write a Python Program to Find the Largest Among Three Numbers.(using relational operators)
print("\n" + "-"*80)
print("Assignment : Write a Python Program to Find the Largest Among Three Numbers.(using relational operators)")
number_1 = int(input("Enter 1st number :  "))
number_2 = int(input("Enter 2nd number :  "))
number_3 = int(input("Enter 3rd number :  "))
if number_1 == number_2 and number_1 == number_3:
    print("All the numbers provided {0}, {1}, {2} are equal".format(number_1, number_2, number_3))
elif number_1 >= number_2 and number_1 >= number_3:
    print("The greatest number among {0}, {1}, {2} is {3}".format(number_1, number_2, number_3, number_1))
elif number_2 >= number_1 and number_2 >= number_3:
    print("The greatest number among {0}, {1}, {2} is {3}".format(number_1, number_2, number_3, number_2))
else:
    print("The greatest number among {0}, {1}, {2} is {3}".format(number_1, number_2, number_3, number_3))

print("\n" + "-"*80)
