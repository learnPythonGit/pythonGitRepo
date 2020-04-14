# ....................................
# Python Assignment                 :
# Date      : 14/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Find Square and Cube  :
# Git Branch: D14042020saurav       :
# ...................................

# 1 while loop for a given number print the square & cube

num = int(input("Please enter a number for calculating its square or cube"))
count = 2

while count:
    if count ==2:
        print("Square of the number is {0}".format(num*num))
    else:
        print("Cube of the number is {0}".format(num*num*num))
    count -= 1

