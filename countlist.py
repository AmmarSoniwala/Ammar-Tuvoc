class Count:
    def count(self, arr):
        mydict = {}
        for i in arr:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        return mydict
    def count_str(self, s):
        arr = s.split(" ")
        return self.count(arr)

lst = []
length = int(input("Enter number of elements: "))

import samplesort as ss
ss.Sorting().take_input(lst, length)

input_str = str(input("Enter the string to be counted: "))

c = Count()
print(c.count_str(input_str))
print(c.count(lst))
