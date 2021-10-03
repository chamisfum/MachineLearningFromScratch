"""
We can easily get the time complexity by examining the for loops in the Selection Sort algorithm.
For a list with n elements, the outer loop iterates n times.
The inner loop iterate n-1 when i is equal to 1, and then n-2 as i is equal to 2 and so forth.
The amount of comparisons are (n - 1) + (n - 2) + ... + 1, which gives Selection Sort a time complexity of O(n^2).
"""

class SelectionSort:
    def sort(data, mode="asc"):
        for i in range(len(data)):
            lowerBound = i
            for j in range(i + 1, len(data)):
                if mode == "asc":
                    if data[j] < data[lowerBound]:
                        lowerBound = j
                elif mode == "dsc":
                    if data[j] > data[lowerBound]:
                        lowerBound = j
            data[i], data[lowerBound] = data[lowerBound], data[i]
        return data

print(SelectionSort.sort([1,35,6,1,2,3], "dsc"))