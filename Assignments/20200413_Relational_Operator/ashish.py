# Assignment : for a given number get octal, binary, hex
decimal = int(input("Enter number to get OCTAL, HEX & BINARY  : "))
print("OCTAL value of DECIMAL {0} is {1}".format(decimal, oct(decimal)))
print("HEX value of DECIMAL {0} is {1}".format(decimal, hex(decimal)))
print("BINARY value of DECIMAL {0} is {1}".format(decimal, bin(decimal)))


# Assignment : convert temperature from celcius to farenheit
temp_in_celsius = float(input("Enter temperature in CELSIUS to convert to FARENHEIT  : "))
temp_in_farenheit = ((9/5)*temp_in_celsius) + 32
print("Temperature in FARENHEIT is {0:0.2f}".format(temp_in_farenheit))

