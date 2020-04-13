# :.........................................:
# : Python Assignment.                      :
# : Date        : 12/04/2020                :
# : Developer   : Kiran Lohar               :
# : Topic       : Python Loops: While, For. :
# : Git Branch  : D12042020/Kiran           :
# :.........................................:

# 1. Print table of 2 using While loop in Python.
x = 2
i = 1
print('Table of 2 using WHILE loop:')
while i <= 10:
    y = x * i
    print(str(x) + " * " + str(i) + " = " + str(y))
    i += 1

# 2. Print table or 2 using For loop in Python.
x = 2
print('Table of 2 using FOR loop:')
for j in range(1, 11):
    y = x * j
    print(str(x) + " * " + str(j) + " = " + str(y))

#3. Loop through characters of string using FOR loop
state = 'Maharashtra'
for m in state:
    print(m)

#4. Loop through characters of string using WHILE loop
state = 'Maharashtra'
n = 0
print(state)
while n <= len(state):
  #  print(state[n]) #This statement results in error though the result is printed correctly.
  # IndexError: string index out of range, Hence commented this statement
    n += 1

#4. Loop through list using for loop
cities = ['Pune', 'Mumbai', 'Satara', 'Kolhapur']
for k in cities:
    print(k)


