
'''

Chapter 2

'''


'''

Type conversion and typecasting

'''

age = input("Your age: ")

# print(age, type(age))  # This will print str as whatever we take the i
# print(age + 1)         # Will shoot an error as the age variable hold the string data type due to which python will
                       # try to concatenate with 1 which is not possible due to which python will thorw an error as
                       # 1 is int type 
                       # See the assets/error/chpt2-error.png

# So to perform this we can converter the type of data which the variable is holding using the type conversion fun
# int() => to convert in integer data type
# float() => to convert in float data type
# str() => to convert in string data type
# bool() => to onvert in boolean data type


# This is known as type casting = done by the developer whereas the python/interpeter does something automatically does
# the conversion and that is known as type conversion

# Example of type casting
print(int(age) + 1)  # Now it will add +1 to the age given by the user

# Example of type conversion
print("Example of Type conversion \n1+0.5: ", 1+0.5) # Python interpeter automatically convert the 1 into float and perform
                                                     # the operations this is known as type conversion

                                            





