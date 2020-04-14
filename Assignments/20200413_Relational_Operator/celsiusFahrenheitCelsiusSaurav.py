# ....................................
# Python Assignment                 :
# Date      : 14/04/2020            :
# Developer : Saurav Kumar          :
# Topic     : Number System         :
# Git Branch:                       :
# ...................................

# 2 convert temperature from celcius to farenheit to celsius

temp = input("Enter the temperature")

if (temp[-1].lower()) == 'f':
    print("Temperature entered by user is in degree Fahrenheit")
    newtemp = ((int(temp) - 32) * 5/9)
    print("Temperature in degree Celsius is " + newtemp +" C" )