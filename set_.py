
# Set

'''

Set is a collection of items store in a single variables but it's unchangeable, unordered and unindexed and they don't allow
duplicate value

They are enclosed with {}

Link: https://www.w3schools.com/python/python_sets_methods.asp

'''

# -------------------------------------------------------------------------------------
# set 
thisset = {"apple", "banana", "cherry"}
print(thisset)

# -------------------------------------------------------------------------------------
# adding new item in a set using the add()
# even though we cannot change the value which is already store in set we can add new and remove value to the set
print("---\nBefore updating the set: ", thisset)
thisset.add("watermelon")
print("After updating the set:", thisset)

# we can also use the update() to add more items in the set
print("---\nBefore updating the set: ", thisset)
alist = ["pineapple", "mango"]   # we can use an iterate type object instead of another set
thisset.update(alist)
print("After updating the set:", thisset)

# -------------------------------------------------------------------------------------
# Removing an item in set using the remove() and discard()

# using the remove()  => is the item doesn't exist then it will raise an error
print("---\nBefore removing the mango from set", thisset)
thisset.remove("mango")
print("after removing the mango from set: ", thisset)

#thisset.remove("mango") will raise an error as mango is not found in the set

# using the discard() => it will not raise an error if the item is not found in the set
print("---\nBefore removing the pineapple from set", thisset)
thisset.remove("pineapple")
print("after removing the pineapple from set: ", thisset)

'''
We can use the pop() to remove an item from the set but the pop() will remove an random item and will output the remove item
so we can not confirm which item it will remove

We can use clear() to clear a entire set()

'''

# -------------------------------------------------------------------------------------
# Link for more set method: https://www.w3schools.com/python/python_sets_methods.asp

