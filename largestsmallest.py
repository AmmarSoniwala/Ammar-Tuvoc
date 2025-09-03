class LargestSmallest:
    def find_largest_smallest(self, arr):
        if not arr:
            return None, None
        largest = smallest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
            elif num < smallest:
                smallest = num
        return largest, smallest
    
import samplesort as ss

lst = []
length = int(input("Enter number of elements: "))
ss.Sorting().take_input(lst, length)

ls = LargestSmallest()
largest, smallest = ls.find_largest_smallest(lst)

print(f"Largest element is: {largest}")
print(f"Smallest element is: {smallest}")