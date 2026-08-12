
# Conditional Statements

'''

Conditional Statements are the statements in which some conditional are check to before performing a operations.

'''

# -------------------------------------------------------------------------------------
# if statements

# Let check whether the age is 18 or nots
my_age = int(input("Enter age: "))
if my_age >= 18:
    print("Yes, You are old enough to take my decision like a man")

'''

Here, first the conditional will be checked that whether the my_age is greater or equal to 18 and if yes then only it will
print else it will be ignoreds

'''

# -------------------------------------------------------------------------------------
# if-else statements

if my_age >= 18:
    print("Yes, You are old enough to take my decision like a man")
else: 
    print("You are child")

'''

Here, similar to if statements it will check the conditional and if conditional is true then print the "Yes you are old..." 
line else it will print the "You are child" 

'''

# -------------------------------------------------------------------------------------
# if-elif statements

percentage = float(input("Enter your percentage: "))

if percentage >= 80.00:
    print("You got Grade A")
elif percentage < 80.00 and percentage >= 60.00:
    print("You got Grade B")
elif percentage < 60.00:
    print("You got Grade C")


'''

Here, we are checking multiple conditions and on the basic of that we are deciding what to print

'''
