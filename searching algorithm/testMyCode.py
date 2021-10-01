from LinearSearch import LinSearch
from BinarySearch import BinSearch

testdata = [1,23,4,4,12,4,123,51]
sentences = "this is python searching and sorting algorithm module"
word = "python"
find = 4

# Linear Search Algorithm Test
print("Linear Search Test Begin!")
assert LinSearch.LinearSearch(testdata, find) == (4,2)
assert LinSearch.LinearSearchType2(testdata, find) == (4, [2, 3, 5])
print("Linear Search Test Done!")

# Binary Search Algorithm Test
print("Binary Search Test Begin!")
assert BinSearch.BinarySearch(testdata, find)==(4, 3)
assert BinSearch.BinarySearchType2(testdata, find)==(4, [3, 1, 1])
print("Binary Search Test Done!")
