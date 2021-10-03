"""
"""

class QwickSort:
    def partition(data, low, high):
        pivot = data[(low + high) // 2]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while data[i] < pivot:
                i += 1
            j -= 1
            while data[j] > pivot:
                j -= 1

            if i >= j:
                return j
            data[i], data[j] = data[j], data[i]
    
    def sort(data):
        def _sort(items, low, high):
            if low < high:
                split_index = QwickSort.partition(items, low, high)
                _sort(items, low, split_index)
                _sort(items, split_index + 1, high) 
        _sort(data, 0, len(data) - 1)
        return data

print(QwickSort.sort([1,35,6,1,2,3]))