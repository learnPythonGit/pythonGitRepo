#  :................................................................................:
#  : Python Assignment.                                                             :
#  :................................................................................:
#  : Date        : 18/04/2020                                                       :
#  : Developer   : Kiran Lohar                                                      :
#  : Topic       : Relational Operation Assignment.                                 :
#  : Git Branch  : Assignments/ControlFlow                                          :
#  :................................................................................:

# 1. Write a Python Program to Find the Factorial of a Number (using relational operators and while/for loop)
print("Find the Factorial of a Number....")
def factorial_of_number():
    print("Enter a number:")
    number = int(input())
    i = 1
    factorial = 1
    while i <= number:
        factorial = factorial * i
        i += 1
    print("Factorial of " + str(number) + ' is ' + str(factorial))
factorial_of_number()
print('Continue to find factorial of another number? (y/n)')
continue_input = str(input())
if continue_input == 'Y' or continue_input == 'y':
   factorial_of_number()

# 2. Write a Python Program to Find the Largest Among Three Numbers.(using relational operators)
print('--------------------------------------------------------')
print('Enter three numbers to find the largest number: ')
number_one = int(input())
number_two = int(input())
number_three = int(input())

if number_one > number_two:
    if number_one > number_three:
        print(str(number_one) + ' is largest number among three inputs')
    else:
        print(str(number_three) + ' is largest number among three inputs')
elif number_two > number_three:
    print(str(number_two) + ' is largest number among three inputs')
else:
    print(str(number_three) + ' is largest number among three inputs')

print('End of the assignment')