# Assignment : while loop for a given number print the square & cube
print("\n" + "-"*80)
print("Assignment : 1 while loop for a given number print the square & cube")
decimal = int(input("Enter a number to derive SQUARE and CUBE  : "))
count = 2
while count != 0:
    count -= 1
    if count == 1:
        print("SQUARE of DECIMAL {0} is {1}".format(decimal, decimal**2))
    else:
        print("CUBE of DECIMAL {0} is {1}".format(decimal, decimal**3))



# Assignment : while loop for a given number add 3 for 7 times
print("\n" + "-"*80)
print("Assignment : while loop for a given number add 3 for 7 times")
decimal = int(input("Enter a number to add 3 for 7 times  : "))
output = 0
count = 0
while count < 7:
    if count == 0:
        output = decimal
    output += 3
    count += 1
print("Seven times of DECIMAL {0} is {1}".format(decimal, output))



# Take 10 integers from keyboard using loop and print their average value on the screen.
print("\n" + "-"*80)
print("Assignment : Take 10 integers from keyboard using loop and print their average value on the screen.")
index = 1
numbers = 0
while index <= 10:
    numbers += int(input("Enter number " + str(index) + " :  "))
    index += 1
if (numbers%10) == 0:
	print("The average value of the provided 10 numbers is " + str(numbers//10))
else:
	print("The average value of the provided 10 numbers is " + str(numbers/10))



# Assignment : Print the following patterns using loop :
#	*
#	**
#	***
#	****
print("\n" + "-"*80)
print("Assignment : Print the following patterns using loop")
print("             *")
print("             **")
print("             ***")
print("             ****")
number = int(input("Enter a number :  "))
index = 1
while index <= number:
    print("*"*index)
    index += 1



# Assignment : Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). 
#              Print average and product of all numbers.
print("\n" + "-"*80)
print("Assignment : Take integer inputs from user until user presses q ( Ask to press q to quit after every integer input )")
number_product = 1
number_sum = 0
counter = 0
while True:
    input_string = str(input("Key in a number or key in \"q\" to quit :  "))
    if input_string != "":
        if input_string.upper() == "Q":
            break
        else:
            number_product *= int(input_string)
            number_sum += int(input_string)
            counter += 1
print("The product of provided numbers is " + str(number_product))
if (number_sum%counter) == 0:
    print("The average of provided numbers is " + str(number_sum//counter))
else:
    print("The average of provided numbers is " + str(number_sum/counter))

print("\n" + "-"*80)
