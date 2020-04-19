#  :................................................................................:
#  : Python Assignment.                                                             :
#  :................................................................................:
#  : Date        : 18/04/2020                                                       :
#  : Developer   : Kiran Lohar                                                      :
#  : Topic       : Python Loops: while loop.                                        :
#  : Git Branch  : Assignments/WhileLoopsAssignments_Kiran                          :
#  :................................................................................:

# 1. Take 10 integers from keyboard using loop and print their average value on the screen.
print("Enter 10 integers from keyboard....")
i = 1
numbers = []
total = 0
while i <= 10:
    numbers.append(int(input('Enter ' + str(i) + ' number: ')))
    i += 1
print('List of numbers: ' + str(numbers))
x = 0
for x in numbers:
    total += x
average = total/len(numbers)
print('Average of the entered numbers: ' + str(average))

# 2. Print the following patterns using loop :
#	*
#	**
#	***
#	****
#   *****
print('-------------------------------------------------')
print('Print the given pattern using *.....')
row_count = int(input('Enter the number of rows to be printed: '))
i = 1
while i <= row_count:
    j = 1
    while j <= i:
        print('*', end=" ")
        j += 1
    i += 1
    print('\n')

# 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
#    Print average and product of all numbers.
print('Enter Number to find the product: ')
n = int(input())
product = 1
while (n != 0):
    product = product * (n % 10)
    n = n // 10
print('Product on given number is: ' + str(product))


