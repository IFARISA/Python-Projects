numbers = {}
size = int(input('Enter size of the dictionary: '))
for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter teh value: ")
    numbers[key] = value

print('Keys are: ', numbers.keys())
print('Values are: ', numbers.values())
print(25*"_")
numbers.clear()
print('Keys are: ', numbers.keys())
print('Values are: ', numbers.values())
print(25*"_")
