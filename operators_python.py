
# Python operators

'''

Arithmetics operators

Comparison Operators

Logical Operators

'''

# -------------------------------------------------------------------------------------
# Arithmetics

# add
print(15 + 20)

# Sub
print(15 - 20)

# Multuply
print(15 * 20)

# Divison
print(15 / 20)

# only give integer value in Divison
print(15 // 20)

# modulo => Reminder
print(15 % 20)

# power
print(5 ** 3)

# -------------------------------------------------------------------------------------
# Comparison Operators

# <
print(5 < 2)  # False

# >
print(5 > 2)  # True

# <=
print(5 <= 2) # False

# >=
print(5 >= 2) # True

# ==
print(5 == 5) # True

# !=
print(5 != 3) # True

# -------------------------------------------------------------------------------------
# Logical Operators

# and => it will show True if both statements are true, else False
print((5 == 5) and (5 >= 3))        # True
print((5 == 5) and (5 >= 6))        # False

# or => it will show False if both statements are False, else True
print((5 == 5) or (5 < 3))          # True
print((5 != 5) and (5 >= 6))        # False

# not => will change the True to False and False to True
print(not(5 == 5))                  # False
print(not(5 != 5))                  # True

# -------------------------------------------------------------------------------------
# Identify  Operators

# Link: https://www.w3schools.com/python/python_operators_identity.asp

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
#  with the same memory location. These are is and is not

# is => return True when both variable are return same objects
name = "Tarn"
name_y = name
name_z = "Tarun"

print("is name_z equal to name:", name_z is name) # False as it not pointing to same memory location
print("is name_y equal to name:", name_y is name) # True as it pointing to same memory location of name








