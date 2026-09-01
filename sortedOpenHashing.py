class sortedOpenHashing:
    def hash(self, numbers):
        hashTable = [[] for i in range(10)]

        for num in numbers:
            group = hashTable[num%10]
            
            min = 0
            max = len(group)
            while min<max:
                mid = (min + max)//2
                if group[mid]<num:
                    min = mid + 1
                else:
                    max = mid

            group.insert(min, num)    
        
        return hashTable