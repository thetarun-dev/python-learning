
# Mini Project - Calculator

game_mode = 1

while game_mode:

    print("\n")
    print("=====================================================================================")
    print("=====================================================================================")
    print("     =========== Calculator ==========              ")
    print('''\n
            1. Enter the no on which you want to perform the operator
            2. Enter an operators, below are the operator symbol which you need to perform
                a. + = Add
                b. - = Sub
                c. * = Multiplication
                d. / = Divide
                e. // = Reminder
            3. For exist enter 'False', for continue press 'True'
            \n
    ''')
    print("=====================================================================================")
    print("=====================================================================================")

    num1 = float(input("Enter First No: "))
    num2 = float(input("Enter second No: "))
    operator = input("Enter an operator: ")

    print("\n")
    if operator == '+':
        print("Addition: ", num1 + num2)
    elif operator == '-':
        print("Subtraction:", num1 - num2)
    elif operator == '*':
        print("Multiplication:", num1 * num2)
    elif operator == "/":
        print("Divison:", num1 / num2)
    elif operator == "//":
        print("Reminder:", num1 // num2)
    else:
        print("Invalid Operation")

    game_mode = int(input("Want to continue: "))
    

    
