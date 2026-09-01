n = int(input("Enter number of entries you wish to make: "))

words = []

for i in range(1 ,n+1):
    word = input("Enter word " + str(i) + ": ")
    words.append (word)

count = {}

for word in words:
    word = word.lower()
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

print(count)
