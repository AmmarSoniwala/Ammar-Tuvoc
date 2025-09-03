class Merge:
    def merge_sorted_list(self, list1, list2):
        merged_list = []
        i = j = 0

        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

        return merged_list

list1 = []
list2 = []

import samplesort as ss

n1 = int(input("Enter number of elements in first list: "))
ss.Sorting().take_input(list1, n1)

n2 = int(input("Enter number of elements in second list: "))
ss.Sorting().take_input(list2, n2)

ss.Sorting().bubble_sort(list1)
ss.Sorting().bubble_sort(list2)

m = Merge()
print("Merged Sorted List:", m.merge_sorted_list(list1, list2))