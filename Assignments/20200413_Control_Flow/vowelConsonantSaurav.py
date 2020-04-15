# ....................................
# Python Assignment                 :
# Date      : 15/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Find Vowel Consonant Count in a word:
# Git Branch: D15042020saurav                      :
# ...................................

# Count the number of vowels and consonants in the string/word. (using if...else, for/while loop)

word = input("Please enter a string in which we need to count Vowel or Consonant")
vowelList = ['a', 'e', 'i', 'o', 'u']

vowelCount = 0
consCount = 0
for i in word:
    if i in vowelList:
        vowelCount += 1
    else:
        consCount += 1
print("Vowel count in word \'{0}\' is {1}".format(word, vowelCount))
print("Consonant count in word \'{0}\' is {1}".format(word, consCount))



