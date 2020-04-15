# ....................................
# Python Assignment                 :
# Date      : 14/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Celsius to Fahrenheit :
# Git Branch: D14042020saurav       :
# ...................................

# 2 convert temperature from celcius to farenheit

temp = input("Enter the temperature in degree Celsius")

print("Temperature entered by user is {0} degree Celsius".format(temp))
newTemp = ((int(temp) * 9/5) + 32)
print("{0} degree Celsius after conversion in degree Fahrenheit is ".format(temp) + str(newTemp) +" F" )