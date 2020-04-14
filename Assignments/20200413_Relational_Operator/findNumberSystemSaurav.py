# ....................................
# Python Assignment                 :
# Date      : 14/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Number System         :
# Git Branch:                       :
# ...................................

# 1 for a given number get octal, binary, hex

number = input("Please enter a number")

if len(number) >= 4 and number[1] in ('o', 'b', 'x'):
    if (number[1] == 'x'):
        print("Number entered is %s and is a Hexa decimal number" %number)
    if (number[1] == 'o'):
        print("Number entered is %s and is an Octal number" %number)
    if (number[1] == 'b'):
        print("Number entered is %s and is a Binary number" %number)
else:
    print("%s is a Decimal Number system" %number)
