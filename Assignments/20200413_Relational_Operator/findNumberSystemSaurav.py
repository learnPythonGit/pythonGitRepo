# ....................................
# Python Assignment                 :
# Date      : 14/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Number System         :
# Git Branch:                       :
# ...................................

# 1 for a given number get octal, binary, hex

number = int(input("Please enter a decimal number to be converted to different number system"))

print("Decimal number entered by user is {0}\n".format(number))
print("Octal representation of {0} is {1}".format(number, oct(number)))
print("Hexa Decimal representation of {0} is {1}".format(number, hex(number)))
print("Binary representation of {0} is {1}".format(number, bin(number)))