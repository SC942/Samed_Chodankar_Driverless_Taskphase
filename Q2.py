from selectionSorter import selectionSorter

n = int(input("Enter number of entries you wish to make: "))

words = []

for i in range(1 ,n+1):
    word = input("Enter word " + str(i) + ": ")
    words.append (word)


sort = selectionSorter()
sortedList = sort.sortStr(words)

print("Sorted list: ", sortedList)
