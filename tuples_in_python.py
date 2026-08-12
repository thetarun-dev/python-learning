
# Tuples

'''

A Tuple is similar to list, it a collection of value stored in a single variables but it's immutable i.e there value can be changed
so for storing new value we have to create a new variable

Tuples are unchangeable, but allow duplicate value

Similar to list, it index start with 0

Link: https://www.w3schools.com/python/python_tuples.asp

'''

# -------------------------------------------------------------------------------------
# Tuple
mytuple = ("Hello", "Best Day of my life", 12)
print(mytuple)

# we can also make tuples without using the ()
mytuple1 = "Hello", "Apple", 34, 58
print(mytuple1)

# -------------------------------------------------------------------------------------
# Looping through the tuple

# for loop
for num in mytuple:
    print(num)
print("\nend of loop")

# while loop
counter = 0
while counter <  len(mytuple):
    print(mytuple[counter])
    counter += 1
print("\nend of loop")

# -------------------------------------------------------------------------------------
# count() => will give us the count of the specified value occured in tuple
newtuples = ("Tarun", "Tarun", 12, 33, 12, 99)
print(newtuples.count(12))



