from typing import Tuple

"""
In the worst case scenario (when the list is in reverse order), this algorithm would have to swap every single item of the array. 
Our swapped flag would be set to True on every iteration.
Therefore, if we have n elements in our list, we would have n iterations per item - thus Bubble Sort's time complexity is O(n^2).
"""

class BubbleSort:
    def sort(data, mode="asc"):
        swap = True
        
        while swap:
            swap = False
            for i in range(len(data)-1):
                if mode == "asc":
                    if data[i] > data[(i+1)]:
                        data[i], data[(i+1)] = data[(i+1)], data[i]
                        swap = True
                elif mode == "dsc":
                    if data[i] < data[(i+1)]:
                        data[i], data[(i+1)] = data[(i+1)], data[i]
                        swap = True
        return data