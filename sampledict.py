thisdict = {
    "Owner": "Ammar",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "Color": "Red"
}
print(thisdict)

print(thisdict.keys()) # prints all the keys in the dictionary

print(thisdict.get("model")) # prints the value of the specified key

thisdict["year"] = 2020 # updates the value of the specified key
print(thisdict.get("year"))

thisdict.update({"year": 2025}) # updates the value of the specified key
print(thisdict.get("year"))

# thisdict.popitem() # removes the last inserted item
# print(thisdict)

# thisdict.pop("Owner") # removes the specified item
# print(thisdict)

# del thisdict[] # removes the whole dictionary
# print(thisdict)

# thisdict.clear() # empties the dictionary
# print(thisdict)

for x in thisdict:
    print(x) # prints all the keys in the dictionary

for x in thisdict:
    print(thisdict[x]) # prints all the values in the dictionary

for x in thisdict.values():
    print(x) # prints all the values in the dictionary

for x, y in thisdict.items():
    print(x, y) # prints all the key-value pairs in the dictionary
