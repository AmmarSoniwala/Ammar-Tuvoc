class Sorting:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_i = i
            for j in range(i+1, n):
                if arr[j] < arr[min_i]:
                    min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]
        return arr
    def take_input(self, arr, l):
        for i in range(l):
            arr.append(int(input("Enter element: ")))
# lst = []
# length = int(input("Enter number of elements: "))
# x= Sorting()
# x.take_input(lst, length)
# x.selection_sort(lst)
# print(lst)
