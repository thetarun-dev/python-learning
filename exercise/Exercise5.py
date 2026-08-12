
'''

Given Employee records in  form ID, name and salary. 

[
    (101, "Tarun", 21000),
    (102, "Sachin", 15000),
    (103, "Varun", 5000),
    (104, "Dhoni", 95000),
]

Ask user to enter id and search it inisde the record

'''

Record = [
    (101, "Tarun", 21000),
    (102, "Sachin", 15000),
    (103, "Varun", 5000),
    (104, "Dhoni", 95000),
]

id = int(input("Enter the id: "))

for x in Record:
    if (x[0] == id):
        new_tup = x
        print("-----------------------------")
        print("You have search for:", id)
        print("Employee Name:", new_tup[1])
        print("Employee Salary:", new_tup[2])
        print("-----------------------------")
        break





