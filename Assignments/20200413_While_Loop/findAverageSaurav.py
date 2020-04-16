# ....................................
# Python Assignment                 :
# Date      : 16/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : find Average of 10 numbers     :
# Git Branch: D15042020saurav       :
# ...................................

# Take 10 integers from keyboard using loop and print their average value on the screen.
num = int(input("Enter the count of numbers whose average is to be calculated"))
sum = 0
count = num
while count > 0:
    number = int(input("Please enter a number"))
    sum = sum + number
    count -= 1

print("Average of all {0} numbers is {1}".format(count,int((sum/num))))



