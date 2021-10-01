"""
The binary search algorithm can be written either recursively or iteratively. 
Recursion is generally slower in Python because it requires the allocation of new stack frames.
We can only pick one possibility per iteration, and our pool of possible matches gets divided by two in each iteration. 
This makes the time complexity of binary search O(log n).

One drawback of binary search is that if there are multiple occurrences of an element in the array, 
it does not return the index of the first element, but rather the index of the element closest to the middle:
"""
class BinSearch:
    def BinarySearch(data, find):
        data.sort()
        first = 0
        last = len(data) - 1
        index = -1

        while first <= last and index == -1:
            middle = (first + last) // 2 # int devided result

            if find == data[middle]:
                index = middle
            else:
                if find < data[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
                    
        return find, index

    def BinarySearchType2(data, find):
        data.sort()
        first = 0
        last = len(data) - 1
        index = []
        while first <= last:
            middle = (first + last) // 2
            if find == data[middle]:
                index.append(middle)
                data.remove(data[middle]) # remove middle element
                last = len(data) - 1
            else:
                if find < data[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
        if not index:
            return -1
        return find, index