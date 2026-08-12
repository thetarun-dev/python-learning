
# Dictionary

'''

Dictionary is a key, value pair. 
It's does not allow duplicate key but the value of the key chan be duplicate

Link of source: https://www.w3schools.com/python/python_dictionaries.asp

'''

# -------------------------------------------------------------------------------------
# Dictionary 
thisdict = {"Name":"Tarun", "age": 22, "country": "India", "Male": "True"}
print(thisdict)

# -------------------------------------------------------------------------------------
# Accessing the Dictionary

# we can access the item of dict using it;s key value we can get using the dict.["key nane"] or get()
print("--\nName: ",thisdict["Name"])     # we are accessing the Name key value in dictionary

# using the get("key")
print("--\nName using the get(): ",thisdict.get("Name"))

# -------------------------------------------------------------------------------------
# we can get all the keys value using the keys()
print("--\nAll keys: ", thisdict.keys())

# -------------------------------------------------------------------------------------
# we can get all the values of inside dict using the values()
print("--\nAll values: ", thisdict.values())

# -------------------------------------------------------------------------------------
# we can get key and value pair in tuples form using the items()
print("--\nAll dictionary values: ", thisdict.items())

# -------------------------------------------------------------------------------------
# We can update the dictionary value using the update() or by accessing the key

# update()
print("---\nBefore updating the age value: ", thisdict.get("age"))
thisdict.update({"age": 23})
print("After updating the age value: ", thisdict.get("age"))

# using the dict["key"] = new value
print("---\nBefore updating the name value: ", thisdict.get("Name"))
thisdict["Name"] = "Tarun Bhandari"
print("After updating the name value using dict[key]: ", thisdict.get("Name"))

# -------------------------------------------------------------------------------------
# we can add item in dict using the update() or dict[new key] = new value

# update()
print("---\nBefore adding: ", thisdict)
thisdict.update({"Fav colors":"Red"})
print("After adding: ", thisdict)

# dic[key] = value
print("---\nBefore adding: ", thisdict)
thisdict["Date of birth"] = "10th july, 2003"
print("After adding: ", thisdict)

# -------------------------------------------------------------------------------------
# we can remove items using the pop(), popitem() and del

# pop(key)
print("---\nBefore removing: ", thisdict)
thisdict.pop("Date of birth")
print("After removing Date of birth", thisdict)

# popitem() => it will remove the latest inserted item
print("---\nBefore removing: ", thisdict)
thisdict.popitem()  # remove fav colors
print("After removing latest insert item: ", thisdict)

# del dict[""]
print("---\nBefore removing: ", thisdict)
del thisdict["Male"]
print("After removeing Male: ",thisdict)



