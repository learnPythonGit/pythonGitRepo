# Assignment : Using IF elif identify if the number is even or odd
print("\n" + "-"*80)
print("Assignment : Using IF elif identify if the number is even or odd")
input_number = int(input("Enter number to verify EVEN or ODD  : "))

if (input_number%2) != 0:
    print("Number entered is ODD")
else:
    print("Number entered is EVEN")



# Assignment : Compare two number and find out the greater number (using if else)
print("\n" + "-"*80)
print("Assignment : Compare two number and find out the greater number (using if else)")
number_one = int(input("Enter 1st number :  "))
number_two = int(input("Enter 2st number :  "))
if number_one > number_two:
    print("{0} is greater than {1}".format(number_one, number_two))
elif number_one < number_two:
    print("{1} is greater than {0}".format(number_one, number_two))
else:  
    print("{0} and {1} are equal".format(number_one, number_two))



# Assignment : Write a program to check if the given number is +ve or -Ve or its 0. (using if else)
print("\n" + "-"*80)
print("Assignment : Write a program to check if the given number is +ve or -Ve or its 0. (using if else)")
number_one = int(input("Enter a number :  "))
if number_one == 0:
    print("Number entered is a ZERO")
elif number_one >= 0:    
    print("Number entered is a POSITIVE number")
else:  
    print("Number entered is a NEGATIVE number")



# Assignment : Check if the given string is a palindrome sting/word.(using if...else and for/while loop)
print("\n" + "-"*80)
print("Assignment : Check if the given string is a palindrome sting/word.(using if...else and for/while loop)")
in_string = str(input("Enter a string :  ")).upper()
# using for loop
is_palindrome = True
string_length = len(in_string)
for i in range(string_length//2):
    if in_string[i] != in_string[string_length -i -1]:
        is_palindrome = False
        break
if is_palindrome:
    print("Entered string is palindrome")
else:
    print("Entered string is not palindrome")
    
# using string function
if in_string == in_string[::-1]:
    print("Entered string is palindrome")
else:  
    print("Entered string is not palindrome")



# Assignment : Count the number of vowels and consonants in the string/word. (using if...else, for/while loop)
print("\n" + "-"*80)
print("Assignment : Count the number of vowels and consonants in the string/word. (using if...else, for/while loop)")
in_string = str(input("Enter a string :  ")).upper()
i, vowels, consonents = 0,0,0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while i < len(in_string):
    if in_string[i] in alphabet:
        if in_string[i] in ('AEIOU'):
            vowels += 1
        elif in_string[i] != " ":
            consonents += 1
    i += 1
print("Entered string has {0} vovels and {1} consonants".format(vowels,consonents))

print("\n" + "-"*80)
