'''

Exercise 2

1. Take the price of 3 product as input and print total price and average price

2. Take superhero name and check wehther it is start with S or s 

'''

# 1

num1 = int(input("Enter amount: "))
num2 = int(input("Enter amount: "))
num3 = int(input("Enter amount: "))

Sum = num1 + num2 + num3
average = Sum / 3

print("Total bill amount:", Sum)
print("Average price:", average)

# 2

name = input("Enter name: ")

print(name.lower().find('s'))

