class Searching:
    def linear_search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    def binary_search(self, arr, target):
        min_i = 0
        max_i = len(arr) - 1
        while min_i <= max_i:
            mid_i = (min_i + max_i) // 2
            if arr[mid_i] == target:
                return mid_i
            elif arr[mid_i] < target:
                min_i = mid_i+1
            else:
                max_i = mid_i-1
        return -1
import samplesort as ss
lst = []
length = int(input("Enter number of elements: "))
ss.Sorting().take_input(lst, length)
ss.Sorting().bubble_sort(lst)
s = Searching()
target = int(input("Enter element to search: "))
result = s.binary_search(lst, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
