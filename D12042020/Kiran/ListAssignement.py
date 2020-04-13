#....................................
# Python Assignment                 :
# Date      : 12/04/2020            :
# Developer : Kiran Lohar           :
# Topic     : Python List           :
# Git Branch: D12042020/Kiran       :
# ...................................

# 1. Loop through vehicles list and print corresponding manufacturer from manufacturers list.
vehicles = ['Tiago', 'Harrier', 'Seltos', 'Creta', 'i20', 'Innova', 'Fortuner', 'Kwid', 'Duster']
manufacturers = ['TATA', 'KIA', 'HYUNDAI', 'TOYOTA', 'RENAULT']

for x in vehicles:
    if x == 'Tiago' or x == 'Harrier':
        if 'TATA' in manufacturers:
            print(x + ' is a \'TATA\' vehicle')
        else:
            print("Manufacturer TATA is not present in the Manufacturers List")
    if x == 'Seltos':
        if 'KIA' in manufacturers:
            print(x + ' is a KIA vehicle')
        else:
            print("Manufacturer KIA is not present in the Manufacturers List")
    if x == 'Creta' or x == 'i20':
        if 'HYUNDAI' in manufacturers:
            print(x + ' is a HYUNDAI vehicle')
        else:
            print("Manufacturer HYUNDAI is not present in the Manufacturers List")
    if x == 'Innova' or x == 'Fortuner':
        if 'TOYOTA' in manufacturers:
            print(x + ' is a TOYOTA vehicle')
        else:
            print("Manufacturer TOYOTA is not present in the Manufacturers List")
    if x == 'Kwid' or x == 'Duster':
        if 'RENAULT' in manufacturers:
            print(x + ' is a RENAULT vehicle')
        else:
            print("Manufacturer RENAULT is not present in the Manufacturers List")

# 2. Find the second largest number in the list.
# Testing done with below various numbers list
#numbers = [2, 4, 1, 6, 5, 8]
#numbers = [4, 4, 1, 5, 8]
#numbers = [4, 4]
numbers = [4, ]

unique_numbers = []
if len(numbers) < 2:
    print("List must have at least two numbers to find the second largest number.")
elif len(numbers) == 2:
    if numbers[0] == numbers[1]:
        print("List has only two numbers and both are same.")
else:
    for x in numbers:
        if x not in unique_numbers:
            unique_numbers.append(x)
unique_numbers.sort()
print(unique_numbers[-2])

#