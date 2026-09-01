class selectionSorter:
    def sortStr(self, words):
        length = len(words)
        for current in range( length- 1):
            min = current

            for i in range(current+1, length ):
                if words[i].lower() < words[min].lower():
                    min = i

                temp = words[min]
                words[min] = words[current]
                words[current] = temp

        return words