# -------------------------------------------------------------------------------------
# String opertation and formating


'''

In python String are immutable that mean the value will not be change, we can perform the operations with that variable
but the value of that variable remain the same, but a new variable is created which will hold that new value after
the operations is performed

'''

# -------------------------------------------------------------------------------------
# String formatting

'''

Python use the C style of string formatting to create new formatted strings. The % is used to format the a set of
variable enclosed in a tuple together within a formatted string

Special Symbol
%s                 -> string or any object with string operations
%d                 -> Integers
%f/%<no of digit>f -> float
%x/%X              -> Integers in hex representation

for details: https://www.learnpython.org/en/String_Formatting

'''

# Example

name = "Tarun"
print("My name is %s" %name)

# -------------------------------------------------------------------------------------
# String operations

'''

In Python there are various string operations/method which we can perform on the string but some common are
upper()
lower()
find(value, start, end)
isdigit()
repalce(value need to replace, value to be replace)


Link: https://www.w3schools.com/python/python_ref_string.asp

'''

# Examples


name = "taRun"

print("name variable value:", name)     # taRun

# upper()
print("upper():", name.upper())         # TARUN

# lower()
print("lower():", name.lower())         # tarun

