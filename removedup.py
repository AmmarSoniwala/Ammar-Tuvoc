class Remove:
    def remove_duplicates(self, arr):
        lst = []
        for i in arr:
            if i not in lst:
                lst.append(i)
        return lst
    
arr = [0,0,1,1,2,3,2,1,3,2,1,3,2,1]

rem = Remove()
print(rem.remove_duplicates(arr))