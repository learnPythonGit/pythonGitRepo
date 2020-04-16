# ....................................
# Python Assignment                 :
# Date      : 16/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : average and product of Given Numbers :
# Git Branch: D15042020saurav       :
# ...................................

# Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
#     Print average and product of all numbers.
summation = 0
count = 0
product =1
while True:
    userInput = input("Please enter a number and if you want to quit enter q")
    if userInput.lower() == "q":
        break
    else:
        summation = summation + int(userInput)
        count = count + 1
        product = product * int(userInput)
print("Average of all the numbers is {0}".format(int(summation/count)))
print("Product of all the numbers is {0}".format(product))