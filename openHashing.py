class openHashing:
    def hash(self, numbers):
        hashTable = [[] for i in range(10)]

        for num in numbers:
            group = num%10
            hashTable[group].append(num)
        
        return hashTable