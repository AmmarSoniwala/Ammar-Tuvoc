my_list = [1,2,3,4,5,6]

print(my_list)

print(len(my_list))

print(my_list[-3:])

my_list[0:2] = ["Ammar"]

print(my_list)

my_list.append(7) # adds at the end of the list
print(my_list)

my_list.insert(1, "Soniwala") # adds at the specified index
print(my_list)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)
print(tropical)

thislist = ["apple", "banana", "mango", "banana", "cherry"]
thislist.remove("banana") # removes the first occurrence of the specified value
print(thislist)

thislist.pop() # removes the last item if index is not specified
print(thislist)

thislist.pop(1) # removes the item at the specified index
print(thislist)

del thislist[0] # removes the item at the specified index
print(thislist)

del thislist # deletes the entire list
# print(thislist) # this will raise an error because the list no longer exists

thislist = ["apple", "banana", "mango", "banana", "cherry"]
thislist.clear() # empties the list
print(thislist)

thislist = ["apple", "banana", "mango", "banana", "boat", "cherry"]
# newlist = []

# for x in thislist:
#     if "b" in x:
#         newlist.append(x)

# print(newlist)

newlist = [x for x in thislist if "b" in x] # list comprehension
print(newlist)

print(thislist.sort()) # sorts the list in ascending order
print(thislist)
print(thislist.sort(reverse=True)) # sorts the list in descending order
print(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print(list3 * 2) # repeats the list twice