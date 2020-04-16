# ....................................
# Python Assignment                 :
# Date      : 15/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Find Large among 3 Numbers         :
# Git Branch: D15042020saurav                      :
# ...................................

# 1 for a given number get octal, binary, hex

num1 = int(input("Please enter the first number"))
num2 = int(input("Please enter the second number"))
num3 = int(input("Please enter the third number"))

lst = [num1,num2,num3]
x = 0
y = 1
largest = 0
for i in lst:
    if lst[x] > lst[y]:
        y = y + 1
        largest = lst[x]
        if y == len(lst):
            break
    else:
        largest = lst[y]
        x = y
        y = y + 1
        if y == len(lst):
            break

print("Largest among all is {}".format(largest) )


