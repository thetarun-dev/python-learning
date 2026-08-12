
# Loops in python

# range(start, stop, steps) => range() will provide a sequence of number starting from start /0(by default) to end-1
num = range(5)
print(num)

# -------------------------------------------------------------------------------------
# while loop

'''

Syntax

while condition:
    do something...

Example
'''
counter = 0

while counter <= 5: # condition is counter should be smaller or equal to 5
    print(counter)  # print counter value
    counter += 1    # then increase counter value

# which will print numbers from 0 to 5 in new line

# -------------------------------------------------------------------------------------
# for loop

'''

Syntax

for i in sequence:
    do something

We used the for loop when we want to iterate it through some sequence/data/list, dicitonary, set data type etc
'''

# Example
for i in range(6):  # by giving an range from 1 to 5 it will iterate the value and store it in i and unless the sequence 
                    # end loop will continue
    print(i)        # which we are gonna print



