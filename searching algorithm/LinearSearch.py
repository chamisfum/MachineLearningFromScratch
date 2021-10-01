"O(n) linear time complexity, Unsorted searching algorithm"

class LinSearch:
    def LinearSearch(data, find):
        for index in range(len(data)):
            if data[index] == find:
                return find, index
        return -1

    def LinearSearchType2(data, find):
        lstIndex = []
        for index in range(len(data)):
            if data[index] == find:
                lstIndex.append(index)
        if lstIndex:
            return find, lstIndex
        else:
            return -1