# ....................................
# Python Assignment                 :
# Date      : 15/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Find Second Largest Num         :
# Git Branch: D15042020saurav                      :
# ...................................

# Compare two number and find out the greater number (using if else)

lst = [3, 2, 7, 4, 6, 6, 5]
# sorting of list
newList = []
for i in lst:
    if i not in newList:
        newList.append(i)
newList.sort(reverse=True)
print(newList)
print("Second Largest number is {0}".format(newList[1]))


