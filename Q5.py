from openHashing import openHashing

n = int(input("Enter number of entries you wish to make: "))

numbers = []

for i in range(1 ,n+1):
    num = int(input("Enter number" + str(i) + ": "))
    numbers.append(num)


sort = openHashing()
hashTable = sort.hash(numbers)

print("Numbers sorted into their groups: ", hashTable)
