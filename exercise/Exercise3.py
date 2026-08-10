
'''

Take the range from the user and check how many even number are there in those range

'''

start_ = int(input("Enter the starting range: "))
end_ = int(input("Enter the end value: "))
even_nu = 0

for i in range(start_, end_ + 1):
    if i % 2 == 0:
        even_nu += 1
        print(i)

print("There are %d even number from %d to %d" %(even_nu, start_, end_))
