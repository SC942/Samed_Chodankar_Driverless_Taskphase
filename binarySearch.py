class binarySearch:
    def search(self, words, target):
        max = len(words) - 1
        min = 0

        while(min<=max):
            mid = (min + max)//2
            if words[mid].lower() == target.lower():
                return mid
            elif words[mid].lower()<target.lower():
                min = mid + 1
            elif words[mid].lower()>target.lower():
                max = mid - 1
        return -1

        