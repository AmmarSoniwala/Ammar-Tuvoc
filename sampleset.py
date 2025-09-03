thisset = {"apple", "banana", "cherry", "banana", "mango"}
tropical = {"pineapple", "papaya", "mango"}
print(thisset) # duplicates will be removed
print(len(thisset))

thisset.add("orange") # adds an element to the set
print(thisset)

thisset.update(tropical) # adds elements from another set (union)
print(thisset)

thisset.remove("banana") # removes the specified element, raises an error if the element is not found
print(thisset)

thisset.discard("banana") # removes the specified element, does not raise an error if the element is not found
print(thisset)

