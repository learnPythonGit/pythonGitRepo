# ....................................
# Python Assignment                 :
# Date      : 15/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Find Second Largest Num         :
# Git Branch: D15042020saurav                      :
# ...................................

# Compare two number and find out the greater number (using if else)
print("Assignment : Find second largest of the given numbers in list - Method 1")
lst = [3, 2, 7, 4, 6, 6, 5, 8]
# sorting of list
newList = []
for i in lst:
    if i not in newList:
        newList.append(i)
newList.sort(reverse=True)
print("Second Largest number is {0}".format(newList[1]))

# FInd the second Largest number from the list of Number- Ashish

print("Assignment : Find second largest of the given numbers in list - Method 2")
number_list = [1,2,3,4,2,1,5,6,8,4,1,5,1,5,4,8]
number_list = list(set(number_list))
number_list.sort(reverse=True)
print("Second Largest number is {0}".format(number_list[1]))
print("\n" + "-"*80)


