
# List Datatype

'''

List is a collection/sequence of same or different type of the data store in [] and separated by ','
Example: [1, "Tarun", 89.89, False, 3]

Like the array the list index start with 0

List item can be added, remove or changed and duplicate value can be stored. List also have different method by which we can perform certain
operations on list

Link: https://www.w3schools.com/python/python_lists.asp

'''

# Example
list1 = [1, "Tarun", 89.89, False, 3]
print(list1)

# -------------------------------------------------------------------------------------
# length() => It will provide the length of the list/no of items
print("Length of list1 is:", len(list1))      # 5

# -------------------------------------------------------------------------------------
# accessing the item of list using the index no
print("Value at 3 index is:", list1[3])      # False

# -------------------------------------------------------------------------------------
# accessing the item of list using negative index
print("Value stored at -3 is:", list1[-3])   # 89.89

# -------------------------------------------------------------------------------------
# accessing the item of list by range
print("Value stored from 0 to 4 are: ", list1[:4])
print("Value stored from 2 to end are:", list1[2:])

# changing the value of list
print("Current value stored in list:", list1)
list1[4] = 90
print("After changing the value:", list1)

# -------------------------------------------------------------------------------------
# adding the items in list using append(), insert() and extend()

# append() => add item at end of list
print("Before appending:", list1)
list1.append("this is append text")
print("After appending:", list1)

# insert() => insert item at specified index
print("Before insert operation:", list1)
list1.insert(0, "This value is been insert")
print("After inserting the value:", list1)

# extend() => extending the list using another list
print("Before extending the list:", list1)
list2 = ["list2", "Bhandari", 73]
print("List 2: ", list2)
list1.extend(list2)
print("Extending the list1 using the list2:", list1)

# -------------------------------------------------------------------------------------
# removing the items of list using remove(), pop()
 
# remove() => remove the first occurence 
print("List1: ", list1)
list1.remove(89.89)
print("List1 after removing the 89.89:", list1)

# pop() => remove the item using the index no
print("List1: ", list1)
list1.pop(5)
print("List1 after poping out the index value 5:", list1)

