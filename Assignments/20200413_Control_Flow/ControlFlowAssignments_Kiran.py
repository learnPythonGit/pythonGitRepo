#  :................................................................................:
#  : Python Assignment.                                                             :
#  :................................................................................:
#  : Date        : 15/04/2020                                                       :
#  : Developer   : Kiran Lohar                                                      :
#  : Topic       : Python Loops: Control flow.                                      :
#  : Git Branch  : Assignments/ControlFlow                                          :
#  :................................................................................:

#1. Compare two number and find out the greater number (using if else)
print("Find out the greater number....")
print("Enter two numbers: ")
number_one = int(input())
number_two = int(input())
if number_one > number_two:
    print(str(number_one) + ' is greater than ' + str(number_two))
elif number_two > number_one:
    print(str(number_two) + ' is greater than ' + str(number_one))
else:
    print('Both numbers are EQUAL')

#2. Write a program to check if the given number is +ve or -Ve or its 0. (using if else)
print('-----------------------------------------------------------------')
print("Check the number is positive or negative....")
print('Please enter a number of your choice: ')
number = int(input())
if number < 0:
    print(str(number) + ' is negative number')
elif number > 0:
    print(str(number) + ' is positive number')
else:
    print('The number entered is ZERO')

#3. Check if the given string is a palindrome sting/word.(using if...else and for/while loop)
print('-----------------------------------------------------------------')
print("Test if the sting is palindrome string....")
print('Enter string/word: ')
input_string = str(input())
upper_string = input_string.upper()
i = 0
j = len(input_string)-1
k = '0'
while i != j:
    if upper_string[i] != upper_string[j]:
        k = '1'
    i += 1
    j -= 1
if k != '1':
    print('The string \"' + input_string + '\" is palindrome')
else:
    print('The string \"' + input_string + '\" is not palindrome')
    
#4. Count the number of vowels and consonants in the string/word. (using if...else, for/while loop)
print('-----------------------------------------------------------------')
print('Count the number of vowels and consonants....')
input_string = 'My daughters name is Ojaswi'
print('String is: ' + input_string)
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
vowels_count = 0
consonants_count = 0
for i in input_string:
    if i in vowels:
        vowels_count += 1
    elif i != ' ':
        consonants_count += 1
print("Vowels count = " + str(vowels_count))
print("Consonants count = " + str(consonants_count))

