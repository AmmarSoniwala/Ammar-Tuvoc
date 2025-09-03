mydict = {
    "child1" : {
        "name" : "Ammar",
        "year" : 2004
    },
    "child2" : {
        "name" : "Subham",
        "year" : 2005
    },
    "child3" : {
        "name" : "Anil",
        "year" : 2006
    }
}

for x, y in mydict.items():
    for a, b in y.items():
        print(x, a, b)

print(mydict["child1"]["name"]) # prints the value of the specified key in the nested dictionary

keys = ("child1", "child2", "child3")
value = None

thisdict = dict.fromkeys(keys, value) # creates a new dictionary with the specified keys and value
print(thisdict)

x = mydict.setdefault("child3", {"name": "Asad" , "year": 2007})
print(x)