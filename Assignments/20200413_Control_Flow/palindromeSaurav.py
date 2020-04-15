# ....................................
# Python Assignment                 :
# Date      : 15/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Find if word is palindrome         :
# Git Branch: D15042020                      :
# ...................................

# Check if the given string is a palindrome sting/word.(using if...else and for/while loop)

word = input("Please Enter a word to identify if it is a palindrome")

count = -1
flag = True
for i in range(int((len(word)/2))):
    if word[i] == word[count]:
        count = count - 1
    else:
        flag = False
if flag:
    print("word is a palindrome")
else:
    print("word is not a palindrome")







