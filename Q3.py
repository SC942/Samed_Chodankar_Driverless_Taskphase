from selectionSorter import selectionSorter
from binarySearch import binarySearch

n = int(input("Enter number of entries you wish to make: "))

words = []

for i in range(1 ,n+1):
    word = input("Enter word " + str(i) + ": ")
    words.append (word)


sort = selectionSorter()
sortedList = sort.sortStr(words)

print("Sorted list: ", sortedList)

toSearch = input("Enter a word in the array to search for: ")

search = binarySearch()
foundIndex = search.search(words, toSearch)

if foundIndex == -1:
    print(toSearch + " is not present in the list.")
else:
    print("Word found at index " + str(foundIndex))