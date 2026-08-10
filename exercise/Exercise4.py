
'''

Take the range from user and print the odd number in that range

'''

start_ = int(input("Enter start range: "))
end_ = int(input("Enter end value: "))
odd_nu = 0

for num in range(start_, end_ + 1):
    if num % 2 == 0:
        continue
    print(num)
    odd_nu += 1

print("There are %d odd  number from %d to %d" %(odd_nu, start_, end_))

