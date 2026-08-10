
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

# length() => It will provide the length of the list/no of items
print("Length of list1 is:", len(list1))      # 5

# accessing the item of list using the index no
print("Value at 3 index is:", list1[3])      # False

# accessing the item of list using negative index
print("Value stored at -3 is:", list1[-3])   # 89.89

# accessing the item of list by range
print("Value stored from 0 to 4 are: ", list1[:4])
print("Value stored from 2 to end are:", list1[2:])


